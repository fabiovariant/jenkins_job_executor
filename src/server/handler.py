import json
import sys
import os

from .services import JobService, UserServices
from .dao import JobDAO
from flask_restful import Resource
from .jenkins_utils import JenkinsUtils
from flask import Flask, jsonify, request

class JobsExec(Resource):

    def __init__(self):
        self.service = JobService()

    def post(self):
        try:
            data = request.get_json()['data']
            r = self.service.exec_job(data['id_user'], data['job_name'], data['params'])
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
        except:
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
    
class JobHistory(Resource):

    def __init__(self):
        self.service = JobService()

    def get(self, id_user):
        try:
            print('oxi')
            r = self.service.get_job_exec_history(id_user)
            print(r)
            return r, 200, {'ContentType':'application/json'}
        except:
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

class JobsList(Resource):

    def __init__(self):
        self.service = JobService()

    def get(self, id_user):
        try:
            print(id_user)
            jobs = self.service.get_user_jobs(id_user)
            return jobs, 200, {'ContentType':'application/json'}
        except:
            return json.dumps({'success': False}), 500, {'ContentType':'application/json'}

class JobDetails(Resource):

    def __init__(self):
        self.service = JobService()

    def get(self, job_name):
        try:
            job_details = self.service.get_job_details(job_name)
            return job_details, 200, {'ContentType':'application/json'}
        except:
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

class User(Resource):

    def post(self):
        data = request.get_json()['data']
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

    def get(self):
        data = request.get_json()['data']
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

    def put(self):
        data = request.get_json()['data']
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

    def delete(self):
        data = request.get_json()['data']
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

class JobCad(Resource):

    def __init__(self):
        self.service = JobService()

    def get(self):
        try:
            jenkins_jobs = self.service.get_jenkins_jobs()
            return jenkins_jobs, 200, {'ContentType':'application/json'}
        except:
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
    
    def post(self):
        try:
            data = request.get_json()['data']
            print(data)
            nm_job = data['newJob']['nmJob']
            tp_user = data['newJob']['tpUser']
            self.service.insert_new_job(nm_job, tp_user)
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
        except:
            print('Unexpected error 2:', sys.exc_info()[0])
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

class UserType(Resource):

    def __init__(self):
        self.service = UserServices()

    def get(self):
        try:
            r = self.service.get_user_types()
            print(r)
            return r, 200, {'ContentType':'application/json'}
        except:
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}
