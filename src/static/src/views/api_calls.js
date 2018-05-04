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
      body: {
        jobName: exJobName
      }
    })
  }
}
