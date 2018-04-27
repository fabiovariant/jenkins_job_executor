from jenkinsapi.jenkins import Jenkins
import os

JENKINS_HOST = os.environ['JENKINS_HOST']
JENKINS_PORT = os.environ['JENKINS_PORT']
JENKINS_USER = os.environ['JENKINS_USER']
JENKINS_PASS = os.environ['JENKINS_PASS']

def get_server_instance():
    jenkins_url = JENKINS_HOST + ':' + JENKINS_PORT
    server = Jenkins(jenkins_url, username=JENKINS_USER, password=JENKINS_PASS)
    return server

def get_job_details(server):
    return server.get_jobs()

def build_job(server, job_name, params):
    server.build_job(job_name, params)
