import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/home',
    name:'home',
    component: () => import('@/views/MyHome')
  },
  {
    path: '/',
    redirect:'home'
  },
  {
    path: '/taocan',
    name:'taocan',
    component: () => import('@/views/TaoCan'),
  },
  {
    path: '/jishi',
    name:'jishi',
    component: () => import('@/views/JiShi'),
  },
  {
    path: '/user',
    name:'user',
    component: () => import('@/views/User'),
  },

]

const router = new VueRouter({
  routes
})

export default router
