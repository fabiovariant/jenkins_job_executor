import axios from 'axios'
import constants from './constants'

const API_URL = constants.API_BASE_URL + ':' + constants.API_BASE_PORT

export default {
  listJobs: function () {
    return axios.get(API_URL + '/jobs')
  },
  exec: function (exJobName) {
    return axios.post(API_URL + '/jobs', {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      },
      crossDomain: true,
      data: {
        jobName: exJobName
      }
    })
  },
  getAllCustomers: function () {
    return axios.get(API_URL + '/user')
  },
  addNewCustomer: function (userData) {
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
}
