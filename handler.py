import jenkins_utils as utils
from flask import Flask, jsonify


app = Flask('jenkins_job_executor')
jenkins_server_instance = utils.get_server_instance()

@app.route('/jobs')
def list_jobs_handler():
    reports_list = list()
    jobs = utils.get_job_details(jenkins_server_instance)
    for _, job_instance in jobs:
        #if '#report' in job_instance.get_description():
        d = {
            'job_name': job_instance.name,
            'job_desc': job_instance.get_description()}
        reports_list.append(d)
    return jsonify(reports_list)