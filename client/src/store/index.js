import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loginData : {
      username: '',
      email : '',
      imgUrl : '',
      gender : '',
    },
    isLogin : false,
  },
  getters: {
  },
  mutations: {
    ISLOGIN_CHANGE(state) {
      state.isLogin = !state.isLogin
    },
    LOGINDATA_IN(state, response){
      console.log('뀹')
      console.log(response)
      state.loginData.username = response.kakao_account.profile.nickname
      state.loginData.email = response.kakao_account.email
      state.loginData.imgUrl = response.kakao_account.profile.profile_image_url
      state.loginData.gender = response.kakao_account.gender
    }
  },
  actions: {
  },
  modules: {
  }
})
