<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="userLogin">
      <label for="inputId">아이디</label>
      <input type="text" id="inputId" v-model="username">
      <br>
      <label for="inputPw1">비밀번호</label>
      <input type="password" id="inputPw1" v-model="password">
      <br>
      <input type="submit" value="로그인">
    </form>
  </div>
</template>

<script>
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
  methods: {
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
