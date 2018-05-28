import sys
import time
import threading
import traceback
import json

from jenkins import JenkinsException
from .dao import JobDAO, UserDAO
from .jenkins_utils import JenkinsUtils
from .utils import *

# Classe responsável pelas lógicas envolvendo os Jobs.
class JobService(object):

    def __init__(self):
        try:
            self.jenkins_server = JenkinsUtils()
        except:
            print("Unexpected error 1:", sys.exc_info()[0])
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
            print(id_exec)
            print('oxi')
            t = threading.Thread(target=self.__keep_job_build_verification, args=(job_name, next_build_number, user, id_exec,))
            t.start()
            conn.commit()
        except NameError as e:
            print('Unexpected error:', e)
            print('Rollback')
            conn.rollback()
            raise
        except:
            print('Unexpected error:', sys.exc_info()[0])
            print('Rollback')
            conn.rollback()
            raise
        finally:
            conn.close()

    # Verifica informações sobre o build de um job.
    # Quando o build é finalizado, persiste informações sobre o build.
    def __keep_job_build_verification(self, job_name, build_number, user, id_exec):
        try:
            conn = get_connection()
            dao = JobDAO(conn)
            print(job_name)
            build_info = self.jenkins_server.get_server().get_build_info(job_name, build_number)
            if build_info['building']:
                time.sleep(10)
                self.__keep_job_build_verification(job_name, build_number, user, id_exec)
            else:
                success = True if 'SUCCESS' == build_info['result'] else False
                dao.update_exec(id_exec, job_name, user, str(build_info), success)
            conn.commit()
        except JenkinsException as e:
            print('Erro', e)
            time.sleep(10)
            self.__keep_job_build_verification(job_name, build_number, user, id_exec)
        except:
            print('Unexpected error:', sys.exc_info()[0])
            time.sleep(10)
            self.__keep_job_build_verification(job_name, build_number, user, id_exec)
        finally:
            conn.close()
    
    # Lista os jobs permitidos para execução do usuário.
    def get_user_jobs(self, user):
        try:
            conn = get_connection()
            dao = JobDAO(conn)
            print('ok')
            return dao.get_user_jobs(user)
        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise
        finally:
            conn.close()

    # Pega os detalhes de um job para exeução na tela.
    # retorna os parametros de execução se esses existirem.
    def get_job_details(self, job_name):
        try:
            print(job_name)
            job_info = {
                'parameters': self.jenkins_server.get_job_parameters(job_name),
                'job_config': self.jenkins_server.get_job_config(job_name)
            }
            return job_info
        except:
            traceback.print_exc(file=sys.stdout)
            print('Unexpected error:', sys.exc_info()[0])
            raise

    def get_jenkins_jobs(self):
        jobs = self.jenkins_server.get_all_jenkins_job()
        print(jobs)
        conn = get_connection()
        dao = JobDAO(conn)
        r_jobs = dao.get_registred_jobs()
        for job in jobs:
            j_nm = job['name']
            for r_job in r_jobs:
                if j_nm == r_job['nm_Job']:
                    jobs.remove(job)
        return jobs

    def insert_new_job(self, nm_job, tp_user):
        try:
            print(nm_job)
            print(tp_user)
            conn = get_connection()
            dao = JobDAO(conn)
            r_id = dao.insert_new_job(str(nm_job))
            for u_type in tp_user:
                dao.insert_job_user_permission(r_id, u_type)
            conn.commit()
        except:
            print('Unexpected error:', sys.exc_info()[0])
            conn.rollback()
            raise
        finally:
            conn.close()
    
    def get_job_exec_history(self, user_id):
        try:
            conn = get_connection()
            dao = JobDAO(conn)
            r = dao.get_job_exec_history(user_id)
            return r
        except:
            print('Unexpected error:', sys.exc_info()[0])
            conn.rollback()
            raise
        finally:
            conn.close()


class UserServices(object):

    def get_user_types(self):
        try:
            conn = get_connection()
            dao = UserDAO(conn)
            r = dao.getUserTypes()
            conn.commit()
            return r
        except:
            print('Unexpected error:', sys.exc_info()[0])
            conn.rollback()
            raise
        finally:
            conn.close()