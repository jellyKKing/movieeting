<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    createTodo: function () {
      const token = localStorage.getItem('jwt')
      // 2번 문제
      axios({
        method: 'post',
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        url: `${API_URL}/todos/`,
        data: {
          title: this.title,
          is_completed: false,
        }
      })
        .then(()=>{
          this.$router.push({ name: 'TodoList' })
        })
    }
  },
  created () {
  }
}
</script>
