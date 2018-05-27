import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/views/Home'
// Jobs
import JobCard from '@/views/job/JobCard'
import BuildHistory from '@/views/job/BuildHistory'
// Users
import ListUsers from '@/views/user/ListUsers'
import NewUser from '@/views/user/NewUser'
// Cadastro de novos Jobs
import NewJob from '@/views/job_cad/NewJob'

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
      component: {
        render (c) { return c('router-view') }
      },
      children: [
        {
          path: '/reports/new',
          name: 'JobExec',
          component: JobCard
        },
        {
          path: '/reports/history',
          name: 'BuildsHistory',
          component: BuildHistory
        }
      ]
    },
    {
      path: '/user',
      name: 'User',
      component: {
        render (c) { return c('router-view') }
      },
      children: [
        {
          path: '/user/new',
          name: 'NewUser',
          component: NewUser
        },
        {
          path: '/user/list',
          name: 'ListUser',
          component: ListUsers
        }
      ]
    },
    {
      path: '/job',
      name: 'Job',
      component: NewJob
    }
  ]
})
