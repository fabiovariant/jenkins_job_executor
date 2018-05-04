import jenkins_utils as utils
import json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask('jenkins_job_executor')
CORS(app)
jenkins_server_instance = utils.get_server_instance()

@app.route('/jobs', methods=['GET'])
def list_jobs_handler():
    jobs = utils.get_job_details(jenkins_server_instance)
    reports_list = [__to_dict(j) for _, j in jobs if '#report' in j.get_description()]
    return jsonify(reports_list)

@app.route('/jobs', methods=['POST'])
def execute_job():
    data = request.get_json()['data']
    utils.build_job(jenkins_server_instance, data['jobName'])
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

def __to_dict(job):
    return {'jobName': job.name, 'jobDesc': job.get_description(), 'isInExec': job.is_running()}

@app.after_request
def after(response):
  # todo with response
  print response.status
  print response.headers
  print response.get_data()
  return response