import axios from 'axios'
import constants from './constants'

const API_URL = constants.API_BASE_URL + ':' + constants.API_BASE_PORT

function listJobs () {
  return axios.get(API_URL + '/jobsexec')
}

function exec (exJobName) {
  return axios.post(API_URL + '/jobsexec', {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Content-Type': 'application/json'
    },
    crossDomain: true,
    data: {
      jobName: exJobName
    }
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

function listJenkinsJobs () {
  return axios.get(API_URL + '/job')
}

export default {
  listJobs,
  exec,
  getAllCustomers,
  addNewCustomer,
  listJenkinsJobs
}
