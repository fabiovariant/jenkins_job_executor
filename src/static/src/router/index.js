import Vue from 'vue'
import Router from 'vue-router'
import JobCard from '@/views/JobCard'
import Home from '@/views/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/reports',
      name: 'Jobs',
      component: JobCard
    }
  ]
})
