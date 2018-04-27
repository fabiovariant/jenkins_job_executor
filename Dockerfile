FROM tiangolo/uwsgi-nginx-flask:flask-python2.7

# Create app directory
RUN mkdir -p /usr/src/app
RUN pip install jenkinsapi
WORKDIR /usr/src/app
# Bundle app source
COPY . /usr/src/app

ENV JENKINS_HOST "http://localhost"
ENV JENKINS_PORT "40009"
ENV JENKINS_USER "python_executor"
ENV JENKINS_PASS "python_executor"

CMD ["python", "main.py"]