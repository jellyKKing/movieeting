<template>
  <div>
    <h1>확인용</h1>
    <button @click="getTest">확인</button>
    <button @click="getTest2">확인2</button>
    <br>
    {{ res }}

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Test',
  data(){
    return{
      
    }
  },
  methods : {
    getTest() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/test/`,
      })
        .then((res) => {
          console.log(res)          
        })
    },
    getTest2 () {
      const token = this.$cookies.get('jwt')
      // 4번 문제
      axios({
        method: 'get',
        url: `${API_URL}/accounts/mypage/`,
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
        .then((res)=>{
          console.log(res)
        })
        .catch((err)=>{
          console.log(err)
        })
    }
  },
  computed : {
    res (){
      return this.$route.params.res
    } 
  }
}
</script>
