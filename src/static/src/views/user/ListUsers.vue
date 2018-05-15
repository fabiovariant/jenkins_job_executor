<template>
  <div>
    <b-form>
      <div role="tablist">        
        <b-card>
          <b-row sm="10">
            <b-col sm="3" id="wrapper">
              <b-form-select id="tp_seach" v-model="selectedSearch" :options="searchBy" class="mb-3" />
            </b-col>
            <b-col sm="6" id="wrapper">
              <b-form-input type="text" id="tx_search" v-model="txSearch" placeholder="Digite sua busca" class="mb-3" />
            </b-col>
            <b-col sm="2" id="wrapper">
              <b-button id="searchBtn" size="lg" variant="success" class="mb-3" @click="search">
                <i class="fa fa-search"></i> Buscar
              </b-button>
            </b-col>
          </b-row>
          <b-row sm="10">
            <b-table 
                id="listTable"
                ref="listTable"
                striped 
                hover 
                style="cursor: pointer;"
                :items="items"
                :fields="fields"
                v-model="shownItems"
                @row-clicked="rowClickSelector"
              >
            </b-table>
          </b-row>
          <div slot="footer">
            <router-link :to="{path: 'user/new'}" style="color: white">
              <b-button type="reset" size="sm" variant="primary">
                  <i class="fa fa-plus-circle"></i> Cadastrar novo
              </b-button>
            </router-link>
            <b-button type="reset" size="sm" variant="danger"><i class="fa fa-ban"></i> Limpar</b-button>
          </div>
        </b-card>
      </div>
    </b-form>
  </div>
</template>

<script>
import calls from '../api_calls'

export default {
  data () {
    return {
      selectedSearch: null,
      txSearch: null,
      shownItems: null,
      fields: [
        {key: 'name', label: 'Nome'},
        {key: 'type', label: 'Tipo'},
        {key: 'isActive', label: 'Ativo?'}
      ],
      items: [],
      searchBy: [
        { value: null, text: 'Selecione um tipo de busca' },
        { value: 'NM', text: 'Por Nome' }
      ]
    }
  },
  methods: {
    rowClickSelector (record, index, object) {
      let customerName = record.customerName
      this.$router.push({ path: `/users/${customerName}` })
    },
    search: function (event) {
      if (this.selectedSearch === 'NM') {
        calls.getAllCustomers(this.txSearch)
        .then(response => {
          this.items = [response.data]
        }).catch(e => {
          console.log(e)
        })
      }
    }
  }
}
</script>

<style>
  #wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>
