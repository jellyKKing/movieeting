import Vue from 'vue'
import VueRouter from 'vue-router'
import TodoList from '@/views/todos/TodoList'
import CreateTodo from '@/views/todos/CreateTodo'
import Login from '@/views/accounts/Login'
import Logout from '@/views/accounts/Logout'
import Test from '@/views/accounts/Test'
import MyPage from '@/views/accounts/MyPage'

Vue.use(VueRouter)

const routes = [
  {
    path: '/todos',
    name: 'TodoList',
    component: TodoList,
  },
  {
    path: '/todos/create',
    name: 'CreateTodo',
    component: CreateTodo,
  },
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
  {
    path: '/accounts/mypage',
    name: 'MyPage',
    component: MyPage,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
