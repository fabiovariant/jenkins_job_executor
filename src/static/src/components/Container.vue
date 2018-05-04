<template>
  <div class="app">
    <AppHeader/>
    <div class="app-body">
      <Sidebar :navItems="nav"/>
      <main class="main">
        <div class="container-fluid">
          <router-view></router-view>
        </div>
      </main>
    </div>
    <AppFooter/>
  </div>
</template>

<script>
import { Header as AppHeader, Sidebar, Footer as AppFooter } from '../components/'
import nav from '../_nav'

export default {
  name: 'container',
  components: {
    AppHeader,
    Sidebar,
    AppFooter
  },
  data () {
    return {
      nav: nav.items
    }
  }
}
</script>