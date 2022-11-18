import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieList from '@/views/movies/MovieList'
// import CreateTodo from '@/views/todos/CreateTodo'
import Login from '@/views/accounts/Login'
import Logout from '@/views/accounts/Logout'
import Test from '@/views/accounts/Test'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList,
  },
  // {
  //   path: '/todos/create',
  //   name: 'CreateTodo',
  //   component: CreateTodo,
  // },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/logout',
    name: 'Logout',
    component: Logout,
  },
  {
    path: '/accounts/test',
    name: 'Test',
    component: Test,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
