import axios from 'axios'
import constants from './constants'

const API_URL = constants.API_BASE_URL + ':' + constants.API_BASE_PORT

function listJobs () {
  return axios.get(API_URL + '/jobsexec/ROOT')
}

function exec (exJobName, formData) {
  return axios.post(API_URL + '/jobsexec', formData, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'multipart/form-data'
    },
    crossDomain: true
  })
}

function getAllCustomers () {
  return axios.get(API_URL + '/user')
}

function addNewCustomer (userData) {
  return axios.post(API_URL + '/user', {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json'
    },
    crossDomain: true,
    data: {
      userData: userData
    }
  })
}

function addNewJob (job) {
  return axios.post(API_URL + '/job', {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json'
    },
    crossDomain: true,
    data: {
      newJob: job
    }
  })
}

function getUserTypesList () {
  return axios.get(API_URL + '/user_types')
}

function listJenkinsJobs () {
  return axios.get(API_URL + '/job')
}

function listUserJobs (userId) {
  return axios.get(API_URL + '/job_hist/' + userId)
}

function getJobDeatils (jobName) {
  return axios.get(API_URL + '/job/' + jobName)
}

export default {
  listJobs,
  exec,
  getAllCustomers,
  addNewCustomer,
  listJenkinsJobs,
  getUserTypesList,
  addNewJob,
  listUserJobs,
  getJobDeatils
}
