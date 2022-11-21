import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/movies/Home'
import MovieDetail from '@/views/movies/MovieDetail'

import Test from '@/views/accounts/Test'
import MyPage from '@/views/accounts/MyPage'

// swiper
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.min.css'

Vue.use(VueRouter, VueAwesomeSwiper,)

const routes = [
  {
    path: '/movies',
    name: 'Home',
    component: Home,
  },
  {
    path: '/movies/:movie_id',
    name: 'MovieDetail',
    component: MovieDetail,
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
