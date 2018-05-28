<template>
  <div>
    <b-card :title="jobName"
            img-src="/static/report_icon.png"
            img-alt="Relatório"
            img-top
            tag="article"
            style="max-width: 15rem;"
            class="mb-2">
      <p class="card-text">
      </p>
      <b-button @click="showModal(jobName)">
        Executar
      </b-button>
      <b-modal ref="myModalRef" hide-footer :title=jobName>
        <div class="d-block text-center">
          {{jobDetails}}
          <br/>
          <div v-for="(value, key) in jobParam" :key=key>
            {{value}}
            <b-form-group>
              <label :for=key>{{value.name}}</label>
              <b-form-input :id=key :name=key type="text" placeholder="Sua palavra passe"></b-form-input>
            </b-form-group>
          </div>
          <b-btn class="mt-3" variant="success" block @click="exec">Executar</b-btn>
        </div>
        <b-btn class="mt-3" variant="outline-danger" block @click="hideModal">Close Me</b-btn>
      </b-modal>
    </b-card>
  </div>
</template>


<script>
import calls from '../api_calls'

export default {
  name: 'job',
  props: ['jobName'],
  data () {
    return {
      jobDetails: null,
      jobParam: null,
      params: []
    }
  },
  methods: {
    exec: function () {
      calls.exec(this.jobName)
      .then(response => {
        console.log(response)
      }).catch(e => {
        console.log('Error saving airport' + e)
      })
    },
    showModal (jobName) {
      calls.getJobDeatils(jobName)
      .then(response => {
        console.log(response.data.parameters)
        const elem = JSON.parse(response.data.job_config)
        this.jobDetails = elem.project.description
        this.jobParam = response.data.parameters
        console.log(this.jobDetails)
      }).catch(e => {
        console.log('Error saving airport' + e)
      })
      this.$refs.myModalRef.show()
    },
    hideModal () {
      this.$refs.myModalRef.hide()
    }
  }
}
</script>
