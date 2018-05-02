import jenkins_utils as utils
import json
from flask import Flask, jsonify, request

app = Flask('jenkins_job_executor')
jenkins_server_instance = utils.get_server_instance()

@app.route('/jobs', methods=['GET'])
def list_jobs_handler():
    jobs = utils.get_job_details(jenkins_server_instance)
    reports_list = [__to_dict(j) for _, j in jobs if '#report' in j.get_description()]
    return jsonify(reports_list)

@app.route('/jobs', methods=['POST'])
def execute_job():
    data = request.get_json()
    utils.build_job(jenkins_server_instance, data['job_name'])
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

def __to_dict(job):
    return {'job_name': job.name, 'job_desc': job.get_description()}