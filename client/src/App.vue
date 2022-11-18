<template>
  <div id="app">
    <div id="nav">
        <router-link :to="{ name: 'MovieList' }">Movie List</router-link> | 
        <router-link :to="{ name: 'Login' }">Login</router-link> |
        <router-link :to="{ name: 'Logout' }">Logout</router-link> |
        <router-link :to="{ name: 'MyPage' }">MyPage</router-link> 
    </div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin : localStorage.getItem('jwt') ? localStorage.getItem('jwt') : false
    }
  },
  methods: {
    
  },
  created(){
    
  },
}
</script>


<style>
@font-face {
    font-family: 'GmarketSansMedium';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

#app {
  font-family: GmarketSansMedium, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #1D3557;
  padding: 2rem;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #457B9D;
}

#nav a.router-link-exact-active {
  color: #A8DADC;
}

h1 {
  font-weight: bold;
}
</style>
