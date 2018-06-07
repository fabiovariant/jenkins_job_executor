import jenkins
import sys
import time
import xmltodict
import json
import re
import requests
import os
from jenkinsapi.jenkins import Jenkins


def get_job_details(server):
    jobs = server.get_jobs()
    r_jobs = list()
    for job in jobs:
        r_jobs.append(job_info_to_dict(job))
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
            'jobDesc': '', \
            'isInExec': False}

 
class JenkinsUtils(object):
 
    def __init__(self):
        try:
            self.JENKINS_HOST = os.environ['JENKINS_HOST']
            self.JENKINS_PORT = os.environ['JENKINS_PORT']
            self.JENKINS_USER = os.environ['JENKINS_USER']
            self.JENKINS_PASS = os.environ['JENKINS_PASS']
            self.server = self.__connect()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
    def get_server(self):
        return self.server

    def __connect(self):
        #w_url = re.sub( '\/$', '', self.JENKINS_HOST)
        #w_url = w_url + ':' + str(self.JENKINS_PORT)
        jenkins_url = self.JENKINS_HOST + ':' + self.JENKINS_PORT
        return jenkins.Jenkins(jenkins_url, username=self.JENKINS_USER, password=self.JENKINS_PASS)
 
    def get_job_config(self, job_name):
        w_job_config = self.server.get_job_config(job_name)
        w_job_config = json.dumps(xmltodict.parse(w_job_config))
        w_job_config = w_job_config.replace("'", '"')
        return w_job_config
 
    def get_job_details(self, job_name):
        w_job_config  = self.get_job_config(job_name)
        jobDef = json.loads(w_job_config)
        return jobDef
 
    def get_job_info(self, job_name):
        return self.server.get_job_info(job_name)

    def build_job(self, job_name, params=None, files=None):
        jenkins_url = self.JENKINS_HOST + ':' + self.JENKINS_PORT
        jenkins = Jenkins(jenkins_url, username=self.JENKINS_USER, password=self.JENKINS_PASS)
        job = jenkins[job_name]
        qi = job.invoke(build_params=params, files=files)


    def get_all_jenkins_job(self):
        return self.server.get_jobs()
 
    def get_job_parameters(self, job_name):
        print(job_name)
        def get_param_structure(paramDefinition, order, paramType):
            param_elem_dict = {}
            param_elem_dict['name'] = paramDefinition['name']
            param_elem_dict['decription'] = paramDefinition['description']
 
            w_param_type = "unidentified"
            if paramType == "hudson.model.ChoiceParameterDefinition":
                param_elem_dict['choices'] = paramDefinition['choices']['a']['string']
                w_param_type = "choice"
 
            if paramType == "hudson.model.FileParameterDefinition":
                w_param_type = "file"
            elif paramType == "hudson.model.StringParameterDefinition":
                w_param_type = "string"
 
            param_elem_dict['type'] = w_param_type
 
            return param_elem_dict
 
        def parse_parameters(params):
            params_elem_dict = {}
            w_order = 0
 
            for paramDefs in params:
                params_elem_dict[w_order] = {}
                w_param_type = paramDefs
 
                if type(params[paramDefs]) == list:
                    for paramList in params[paramDefs]:
                        params_elem_dict[w_order] = get_param_structure(paramList, order=w_order, paramType=w_param_type)
                        w_order += 1
                else:
                    params_elem_dict[w_order] = get_param_structure(params[paramDefs], order=w_order, paramType=w_param_type)
                    w_order += 1
            return params_elem_dict
 
        w_job_config = self.get_job_config(job_name)
        jobDef = json.loads(w_job_config)
 
        try:
            if 'hudson.model.ParametersDefinitionProperty' in  jobDef['project']['properties']:
                params = jobDef['project']['properties']['hudson.model.ParametersDefinitionProperty']['parameterDefinitions']
                parsed_params = parse_parameters(params)
        except:
            parsed_params = ""
 
        return parsed_params
 
