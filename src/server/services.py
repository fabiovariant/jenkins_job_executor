import sys
import time

from .dao import JobDAO
from .jenkins_utils import JenkinsUtils
from .utils import *

# Classe responsável pelas lógicas envolvendo os Jobs.
class JobService(object):

    def __init__(self):
        try:
            self.jenkins_server = JenkinsUtils()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    # Executa um job, salva informações sobre a execução e dispara uma Thread que irá verificar
    # e salvar informações sobre o build.
    # params:
    # user: Informações sobre o usuário que executou o job.
    # job_name: Nome do Job.
    # params: Parametros para execução do job.
    def exec_job(self, user, job_name, params):
        try:
            conn = get_connection()
            dao = JobDAO(conn)
            next_build_number = self.jenkins_server.get_job_info(job_name)['nextBuildNumber']
            self.jenkins_server.build_job(job_name, params)
            # Salva apenas considerando que tentou executar, não se preocupa se executou ou não.
            # a thread disparada depois faz esse trabalho.
            id_exec = dao.save(job_name, user)
            
            t = threading.Thread(target=self.__keep_job_build_verification, args=(job_name, next_build_number, user, id_exec,))
            t.start()
            conn.commit()
        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise
        finally:
            conn.close()

    # Verifica informações sobre o build de um job.
    # Quando o build é finalizado, persiste informações sobre o build.
    def __keep_job_build_verification(self, job_name, build_number, user, id_exec):
        try:
            conn = get_connection()
            dao = JobDAO(conn)
            build_info = server.get_build_info('build_name', next_build_number)
            if build_info['building']:
                time.sleep(60)
                self.__keep_job_build_verification(job_name, build_number)
            else:
                job = {
                    'name': job_name,
                    'sucess': True if 'SUCCESS' == build_info['result'] else False,
                    'finished': True,
                }
                success = True if 'SUCCESS' == build_info['result'] else False
                dao.update_exec(id_exec, job, user, str(build_info), success)
        finally:
            conn.close()
    
    # Lista os jobs permitidos para execução do usuário.
    def get_user_jobs(self, user):
        try:
            conn = get_connection()
            dao = JobDAO(conn)
            return dao.getUserJobs(user)
            conn.commit()
        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise
        finally:
            conn.close()

    # Pega os detalhes de um job para exeução na tela.
    # retorna os parametros de execução se esses existirem.
    def get_job_details(self, job_name):
        try:
            job_info = {
                'parameters': self.jenkins_server.get_job_parameters(job_name),
                'job_config': self.jenkins_server.get_job_config(job_name)
            }
            return job_info
        except:
            raise

    def get_jenkins_jobs(self):
        jobs = self.jenkins_server.get_all_jenkins_job()
        return jobs