import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/views/Home'
import JobCard from '@/views/job/JobCard'
import ListUsers from '@/views/user/ListUsers'
import NewUser from '@/views/user/NewUser'

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
    }
  ]
})
