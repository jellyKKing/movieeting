import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from "vue-cookies"
// import "../node_modules/bootstrap/dist/css/bootstrap.css";
// import "../node_modules/bootstrap/dist/js/bootstrap.bundle";
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

//쿠키를 사용한다.
Vue.use(VueCookies);

//쿠키의 만료일은 7일이다. (글로벌 세팅)
Vue.$cookies.config("7d");
 

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

window.Kakao.init('9e3e0da3c4e60e3fff9e0174f6fca7b1')