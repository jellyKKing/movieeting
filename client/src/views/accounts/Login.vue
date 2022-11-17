<template>
  <div>
    <KakaoLogin
      api-key="9e3e0da3c4e60e3fff9e0174f6fca7b1"
      image="kakao_login_btn_large"
      :on-success=onSuccess
      :on-failure=onFailure
      />
  </div>
</template>

<script>
import KakaoLogin from 'vue-kakao-login'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Login',
  data: function () {
    return {
      username: null,
      password: null,
    }
  },
  components:{
    KakaoLogin
  },
  methods: {
    onSuccess (res) {
      console.log("success")
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          res : res,
        }
      })
        .then((response)=>{
          console.log("success2")
          this.$router.push({ name: 'Test', params: {'res' : response}})
        })
    },
    onFailure (data) {
      console.log(data)
      console.log("failure")
    },
    userLogin: function () {
      axios({
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
        },
        url: `${API_URL}/api/token/`,
        data: {
          username: this.username,
          password: this.password,
        }
      })
        .then((res) => {
          console.log(res)
          const token = res.data.access 
          localStorage.setItem('jwt', token)
          this.$router.push({name:'TodoList'})
          this.$emit('login')
        })
    }
  }
}
</script>
