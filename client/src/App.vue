<template>
  <div id="app">
    <KakaoLogin
      api-key="9e3e0da3c4e60e3fff9e0174f6fca7b1"
      image="kakao_login_btn_large"
      :on-success=onSuccess
      :on-failure=onFailure
      />

    <div id="nav">
      <span>
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> | 
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
      </span>
      <span>
        <router-link :to="{ name: 'Login' }">Login</router-link> |
        <router-link :to="{ name: 'Logout' }">Logout</router-link> 
      </span>
    </div>
    <router-view @login="login"/>
  </div>
</template>

<script>
import KakaoLogin from 'vue-kakao-login'
import axios from'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data: function () {
    return {
      isLogin : localStorage.getItem('jwt') ? localStorage.getItem('jwt') : false
    }
  },
  components:{
    KakaoLogin
  },
  methods: {
    login() {
      console.log('애미야')
      this.isLogin = true
      console.log(this.isLogin)
    },
    onSuccess (res) {
      console.log("success")
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          res : res,
        }
      })
        .then(()=>{
          this.$router.push({ name: 'Test' })
        })
    },
    onFailure (data) {
      console.log(data)
      console.log("failure")
    },
  },
  created(){
    
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
