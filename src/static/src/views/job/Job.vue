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
        <form enctype="multipart/form-data" novalidate>
          <div class="d-block text-center">
            {{jobDetails}}
            <br/>
            <br/>
            <div v-for="(value, key) in jobParam" :key=key>
              <div v-if="value.type != 'file'">
                <b-form-group>
                  <label :for=key>{{value.name}}</label>
                  <b-form-input :id=key :name=key :ref="'param_' + key" v-model="value.field_value" type="text" placeholder="Digite..."></b-form-input>
                </b-form-group>
              </div>
              <div v-if="value.type === 'file'">
                <label :for=key>{{value.decription}}</label>
                <b-form-file :id=key :name="value.name" :ref="'param_' + key" placeholder="Escolha um arquivo"
                    @change="filesChange($event.target.name, $event.target.files);">
                </b-form-file>
              </div>
            </div>
            <b-btn class="mt-3" variant="success" block @click="exec">Executar</b-btn>
          </div>
          <b-btn class="mt-3" variant="outline-danger" block @click="hideModal">Cancelar</b-btn>
        </form>
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
      params: [],
      error: false,
      fileCount: null,
      formDataSend: new FormData()
    }
  },
  methods: {
    exec: function () {
      this.formDataSend.append('id_user', 1)
      this.formDataSend.append('job_name', this.jobName)
      this.formDataSend.append('params', JSON.stringify(this.jobParam))
      console.log(this.formDataSend)
      calls.exec(this.jobName, this.formDataSend)
      .then(response => {
        console.log(response)
      }).catch(e => {
        console.log('Error saving airport' + e)
      })
      this.formDataSend = new FormData()
    },
    showModal: function (jobName) {
      calls.getJobDeatils(jobName)
      .then(response => {
        const elem = JSON.parse(response.data.job_config)
        this.jobDetails = elem.project.description
        this.jobParam = response.data.parameters
        console.log(this.jobParam)
      }).catch(e => {
        this.error = true
      })
      this.$refs.myModalRef.show()
    },
    hideModal: function () {
      this.$refs.myModalRef.hide()
    },
    filesChange: function (fieldName, fileList) {
      // handle file changes
      Array
        .from(Array(fileList.length).keys())
        .map(x => {
          this.formDataSend.append(fieldName, fileList[x], fileList[x].name)
        })
    }
  }
}
</script>
