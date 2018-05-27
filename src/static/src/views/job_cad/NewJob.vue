<template>
  <div>
    <b-form>
      <div role="tablist">
        <b-container fluid>
          <b-card title="Cadastro Usuário">
            <b-row>
              <b-col sm="10">
                <b-form-group>
                  <label for="userType">Job/Processo</label>
                  <b-form-select id="userType" v-model="jobData.nmJob" :options="jobsList" class="mb-3">
                    <template slot="first">
                      <option :value="null" selected>Selecione uma opção</option>
                    </template>
                  </b-form-select>
                </b-form-group>
              </b-col>
            </b-row>
            <b-row>
              <b-col sm="5">
                <label for="basicMultiSelect">Tipo de usuário com permissão (CTRL + Click)</label>
                <b-form-select id="basicMultiSelect"
                  :plain="true"
                  :multiple="true"
                  :options=userTypeList
                  v-model="jobData.tpUser">
                </b-form-select>
              </b-col>
            </b-row>
            <div slot="footer">
              <b-button size="sm" variant="success" @click="save"><i class="fa fa-dot-circle-o"></i> Salvar</b-button>
              <b-button type="reset" size="sm" variant="danger"><i class="fa fa-ban"></i> Cancelar</b-button>
            </div>
          </b-card>
        </b-container>
      </div>
    </b-form>
  </div>
</template>

<script>
import calls from '../api_calls'

export default {
  name: 'user',
  data () {
    return {
      jobsList: [
      ],
      userTypeList: [
        {value: 'ROOT', text: 'Root'},
        {value: 'ADM', text: 'Administrador'},
        {value: 'VEND', text: 'Vendas'}
      ],
      jobData: {
        nmJob: null,
        tpUser: [

        ]
      }
    }
  },
  methods: {
    save: function () {
      console.log(this.jobData.tpUser)
    }
  },
  created: function () {
    calls.listJenkinsJobs()
    .then(response => {
      console.log(response.data)
      for (let i = 0; i < response.data.length; i++) {
        const element = response.data[i]
        const job = {value: element.name, text: element.name}
        this.jobsList.push(job)
      }
    }).catch(e => {
      console.log('Error saving new user' + e)
    })
  }
}
</script>