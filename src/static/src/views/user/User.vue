<template>
  <div>
    <b-row>
      <b-col sm="10">
        <b-form-group>
          <label for="nmUser">Nome</label>
          <b-form-input v-model.trim="nmUser" type="text" id="nmUser" placeholder="Fabio Silva"></b-form-input>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="10">
        <b-form-group>
          <label for="nmUser">E-mail</label>
          <b-form-input v-model.trim="nmEmail" type="text" id="nmEmail" placeholder="exemplo@papada.com"></b-form-input>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="10">
        <b-form-group>
          <label for="nmUser">Password</label>
          <b-form-input v-model.trim="password" type="password" id="password" placeholder="Sua palavra passe"></b-form-input>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="10">
        <b-form-group>
          <label for="userType">Tipo</label>
          <b-form-select id="userType" v-model="userType" :options="userTypeList" class="mb-3">
            <template slot="first">
              <option :value="null" selected>Selecione uma opção</option>
            </template>
          </b-form-select>
        </b-form-group>
      </b-col>
    </b-row>
    <b-row>
      <b-col sm="8">
        <b-form-group>
          <b-form-checkbox-group id="is_blocked" name="isBlock" :plain="true">
            <b-form-checkbox :plain="true" value="0" v-model="isBlocked">Bloqueado</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
      </b-col>
    </b-row>
    <div slot="footer">
      <b-button size="sm" variant="success" @click="save"><i class="fa fa-dot-circle-o"></i> Salvar</b-button>
      <b-button type="reset" size="sm" variant="danger"><i class="fa fa-ban"></i> Cancelar</b-button>
    </div>    
  </div>
</template>

<script>
export default {
  name: 'user',
  data () {
    return {
      nmUser: null,
      nmEmail: null,
      userType: null,
      isBlocked: null,
      password: null,
      userTypeList: [
        { value: 'SUDO', text: 'Super User' },
        { value: 'NORMAL', text: 'Normal User' }
      ],

      userData: {
        nmUser: null,
        nmEmail: null,
        password: null,
        userType: null,
        isBlocked: null
      }
    }
  },
  methods: {
    save: function () {
      return this.$parent.$emit('save', this.userData)
    }
  },
  watch: {
    nmUser: function (newValue, oldValue) {
      this.userData.nmUser = newValue
    },
    isBlocked: function (newValue, oldValue) {
      this.userData.isBlocked = newValue
    },
    userType: function (newValue, oldValue) {
      this.userData.userType = newValue
    },
    nmEmail: function (newValue, oldValue) {
      this.userData.nmEmail = newValue
    },
    password: function (newValue, oldValue) {
      this.userData.password = newValue
    }
  }
}
</script>