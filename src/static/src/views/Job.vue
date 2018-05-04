<template>
  <b-card :title="jobName"
          img-src="/static/report_icon.png"
          img-alt="Relatório"
          img-top
          tag="article"
          style="max-width: 15rem;"
          class="mb-2">
    <p class="card-text">
      {{jobDesc}}
    </p>
    <b-button @click="exec" variant="primary" :disabled=isInExec >Executar</b-button>
  </b-card>
</template>

<script>
import calls from './api_calls'

export default {
  name: 'job',
  props: ['jobName', 'jobDesc', 'jobExecCall', 'isInExec'],
  methods: {
    exec: function () {
      calls.exec(this.jobName)
      .then(response => {
        console.log(response)
      }).catch(e => {
        console.log('Error saving airport' + e)
      })
    }
  }
}
</script>
