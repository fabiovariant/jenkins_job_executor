# jenkins_job_executor

Python and Flask.

REST API to wraper Jenkins API calls.

Will have a Vue.js interface with the jobs list and execution option.


In your jenkins, anote the job's Description you want to be visible from the interface with the string '#report'.


Add the environment variables (~/.bashrc):

```
export JENKINS_HOST={{your_jenkins_host}}
export JENKINS_PORT={{your_jenkins_port}}
export JENKINS_USER={{your_user_name}}
export JENKINS_PASS={{your_secret}}
```

### Init the python backend:
```
python src/main.py
```

### Init the Vue.js interface
```
npm install --prefix src/static
npm run dev --prefix src/static
```

The interface will automatically open.