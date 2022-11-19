<template>
  <div id="app">
    <div id="nav">
      <div class="row">
        <div class="col-1" style="text-align: left;">
          <router-link class="me-auto" :to="{ name: 'Home' }" style="text-decoration:none;">Home</router-link>
        </div>
        <div class="col-8">
          <!-- center -->
        </div>
        <div class="col-3">
          <div class="hstack gap-3">
            <router-link class="ms-auto" :to="{ name: 'Login' }" style="text-decoration:none;">Login</router-link>
            <div class="vr"></div>
            <router-link :to="{ name: 'Logout' }" style="text-decoration:none;">Logout</router-link>
            <div class="vr"></div>
            <router-link :to="{ name: 'MyPage' }" style="text-decoration:none;">MyPage</router-link> 
          </div>
        </div>
      </div>
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
  components: {

  },
  methods: {
    
  },
}
</script>


<style>
@font-face {
    font-family: 'IBMPlexSansKR-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/IBMPlexSansKR-Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

#app {
  font-family: IBMPlexSansKR-Regular, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  overflow: hidden;
}

#nav {
  padding: 1rem;
}

#nav a {
  font-weight: bold;
  color: #FFFFFF;
}

/* #nav a.router-link-exact-active {
  color: #FCA311;
} */

router-link {
  text-decoration: none;
}

h1 {
  font-weight: bold;
}

</style>