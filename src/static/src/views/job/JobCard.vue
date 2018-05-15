<template>
  <div>
    <b-card-group deck>
      <div v-for="(job, i) in jobs" :key="i">
        <job 
            :job-name=job.jobName 
            :job-desc=job.jobDesc 
            :job-exec-call=job.jobExecCall
            :is-in-exec=job.isInExec />
      </div>
    </b-card-group>
  </div>
</template>

<script>
import Job from './Job'
import calls from '../api_calls'

export default {
  name: 'jobCard',
  components: {
    Job
  },
  data () {
    return {
      jobs: []
    }
  },
  methods: {
    listJobs: function () {
      calls.listJobs()
      .then(response => {
        this.jobs = response.data
      }).catch(e => {
        console.log('Error getting jobs' + e)
      })
    }
  },
  mounted () {
    this.listJobs()
  }
}
</script>
