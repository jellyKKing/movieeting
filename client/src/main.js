import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

window.Kakao.init('9e3e0da3c4e60e3fff9e0174f6fca7b1')