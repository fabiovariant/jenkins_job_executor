<template>
  <div>
    <b-card-group deck>
      <div v-for="(job, i) in jobs" :key="i">
        <job 
            :job-name=job.jobName />
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
        console.log(response.data)
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
