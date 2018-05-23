import json
import sys
import os

from .services import JobService
from .dao import JobDAO
from flask_restful import Resource
from .jenkins_utils import JenkinsUtils
from flask import Flask, jsonify, request

JENKINS_INSTANCE = get_server_instance()

class JobsExec(Resource):

    def __init__(self):
        self.service = JobService()

    def post(self):
        data = request.get_json()['data']
        r = self.service.exec_job(data['id_user'], data['job_name'], data['params'])
        if r == 0:
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
        else:
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

    def get(self):
        try:
            data = request.get_json()['data']
            jobs = self.service.get_user_jobs(data['id_user'])
            return json.dumps(jobs), 200, {'ContentType':'application/json'}
        except:
            return json.dumps({'success': False}), 500, {'ContentType':'application/json'}

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
