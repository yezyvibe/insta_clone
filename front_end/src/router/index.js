import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'
import ProfileView from '../views/accounts/ProfileView.vue'

import CreateView from '../views/articles/CreateView.vue'
import ListView from '../views/articles/ListView.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: SignupView,
  },
  {
    path: '/articles/create',
    name: 'Create',
    component: CreateView,

    // vue router navigation guard 참고!!!
    // beforeEnter(from, to, next) {
    //   if (!Vue.$cookies.isKey('auth-token')) {
    //     next('/accounts/login')
    //   } else {
    //     next()
    //   }
    // }
  },
  {
    path: '/articles',
    name: 'List',
    component: ListView,
  },
  {
    //dynamic route matching
    path:'/:username', // 동적 세그먼트는 콜론부터 시작
    name: 'Profile',
    component: ProfileView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
