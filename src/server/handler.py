import json
import sys
import os
import pymongo
from .jenkins_utils import *

from flask import Flask, jsonify, request
from flask_restful import Resource

JENKINS_INSTANCE = get_server_instance()

class Jobs(Resource):

    def post(self):
        data = request.get_json()['data']
        build_job(JENKINS_INSTANCE, data['jobName'])
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

    def get(self):
        return jsonify(get_job_details(JENKINS_INSTANCE))

    def __to_dict(self, job):
        return {'jobName': job.name, \
            'jobDesc': job.get_description(), \
            'isInExec': job.is_running()}

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