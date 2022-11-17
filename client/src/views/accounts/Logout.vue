<template>
  <div>
  </div>
</template>

<script>
// import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'Logout',
  data: function () {
    return {
    }
  },
  methods: {
  },
  created() {
    const token = localStorage.getItem('jwt')
    console.log(token)
    if (token) {
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>
