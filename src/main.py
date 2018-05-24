from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from server import handler

app = Flask(__name__)
CORS(app)
api = Api(app)

# app.config['JWT_SECRET_KEY'] = 'jenkins-job-executor-super-secret'
# jwt = JWTManager(app)
# 
# app.config['JWT_BLACKLIST_ENABLED'] = True
# app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
# 
# @jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#     jti = decrypted_token['jti']
#     return models.RevokedTokenModel.is_jti_blacklisted(jti)

api.add_resource(handler.JobsExec, '/jobsexec')
api.add_resource(handler.User, '/user')
api.add_resource(handler.JobDetails, '/job/<string:job_name>')


if __name__ == '__main__':
    app.run(port=8076, debug=True)