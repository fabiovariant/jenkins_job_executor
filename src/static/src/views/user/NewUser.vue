<template>
  <div>
    <b-form>
      <div role="tablist">
        <b-container fluid>
          <b-card title="Cadastro Usuário">
            <user />
          </b-card>
        </b-container>
      </div>
    </b-form>
  </div>
</template>

<script>
import User from './User'
import calls from '../api_calls'

export default {
  name: 'NewUser',
  components: {
    User
  },
  methods: {
    save: function (userData) {
      calls.addNewCustomer(userData)
      .then(response => {
        console.log('ok')
      }).catch(e => {
        console.log('Error saving new user' + e)
      })
    }
  },
  created () {
    this.$on('save', this.save)
  }
}
</script>
