import os
import jenkins

JENKINS_HOST = os.environ['JENKINS_HOST']
JENKINS_PORT = os.environ['JENKINS_PORT']
JENKINS_USER = os.environ['JENKINS_USER']
JENKINS_PASS = os.environ['JENKINS_PASS']

#def get_server_instance():
#    jenkins_url = JENKINS_HOST + ':' + JENKINS_PORT
#    server = Jenkins(jenkins_url, username=JENKINS_USER, password=JENKINS_PASS)
#    return server

def get_job_details(server):
    jobs = server.get_jobs()
    r_jobs = list()
    for job in jobs:
        job_info = get_job_information(server, job['name'])
        r_jobs.append(job_info_to_dict(job_info))
    return r_jobs
        

def build_job(server, job_name, params=None):
    server.build_job(job_name, params)

def get_server_instance():
    jenkins_url = JENKINS_HOST + ':' + JENKINS_PORT
    server = jenkins.Jenkins(jenkins_url, username=JENKINS_USER, password=JENKINS_PASS)
    return server

def get_job_information(server, name):
    return server.get_job_info(name, depth=0, fetch_all_builds=False)

def job_info_to_dict(job_info):
    return {'jobName': job_info['name'], \
            'jobDesc': job_info['description'], \
            'isInExec': False}