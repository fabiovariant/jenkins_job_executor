import sys
import time

from .dao import JobDAO
from .jenkins_utils import JenkinsUtils

# Classe responsável pelas lógicas envolvendo os Jobs.
class JobService(object):

    def __init__(self):
        self.jenkins_server = JenkinsUtils()
        self.dao = JobDAO('')

    # Executa um job, salva informações sobre a execução e dispara uma Thread que irá verificar
    # e salvar informações sobre o build.
    # params:
    # user: Informações sobre o usuário que executou o job.
    # job_name: Nome do Job.
    # params: Parametros para execução do job.
    def exec_job(self, user, job_name, params):
        try:
            next_build_number = self.jenkins_server.get_job_info(job_name)['nextBuildNumber']
            self.jenkins_server.build_job(job_name, params)
            # Salva apenas considerando que tentou executar, não se preocupa se executou ou não.
            # a thread disparada depois faz esse trabalho.
            self.dao.save(job_name, user)
            
            t = threading.Thread(target=self.__keep_job_build_verification, args=(job_name, next_build_number, user,))
            t.start()
            return 0
        except:
            print('Unexpected error:', sys.exc_info()[0])
            return -1

    # Verifica informações sobre o build de um job.
    # Quando o build é finalizado, persiste informações sobre o build.
    def __keep_job_build_verification(self, job_name, build_number, user):
        build_info = server.get_build_info('build_name', next_build_number)
        if build_info['building']:
            time.sleep(60)
            self.__keep_job_build_verification(job_name, build_number)
        else:
            job = {
                'name': job_name,
                'exec_return': str(build_info),
                'sucess': True if 'SUCCESS' == build_info['result'] else False,
                'finished': True,
            }
            self.dao.update_exec(job, user)
    
    # Lista os jobs permitidos para execução do usuário.
    def get_user_jobs(self, user):
        dao = JobDAO('')
        return dao.getUserJobs(user)
