<template>
  <div>
    {{ username }}
    <br>
    {{ email }}
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Test',
  data(){
    return{
      username : '',
      email : '',
    }
  },
  methods : {
    getTest2 () {
      
    }
  },
  computed : {
  },
  mounted(){
    const token = this.$cookies.get('jwt')

    axios({
      method: 'get',
      url: `${API_URL}/accounts/mypage/`,
      headers: {
        'Authorization': `Bearer ${token}`,
      },
    })
      .then((res)=>{
        console.log(res)
        this.username = res.data[0].username
        this.email = res.data[0].email
      })
      .catch((err)=>{
        console.log(err)
      })
  }
}
</script>
