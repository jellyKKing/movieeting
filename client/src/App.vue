<template>
  <div id="app" class="position-relative">
    <!-- nav bar -->
    <div id="nav" class="sticky-top">
      <div class="row">
        <!-- left -->
        <div class="col-1" style="text-align: left;">
          <router-link class="me-auto" :to="{ name: 'Home' }" style="text-decoration:none;">Home</router-link>
        </div>
        <!-- center -->
        <div class="col-8">
        </div>
        <!-- right -->
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
    <!-- header bg -->
    <div id="header-overlay"></div>
    <div id="header-bg"></div>
    <!-- router-view -->
    <div class="container-fluid d-flex justify-content-center">
      <div id="body">
        <router-view />
      </div>
    </div>
    <!-- footer -->
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


<style lang="scss">
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
  display: flex;
  flex-direction: column;
  /* overflow: hidden; */
}

#nav {
  padding: 1rem;
  position: sticky;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid hsla(210,16.7%,97.6%, 0.1);
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

#header-bg {
  position: absolute;
  height: 500px;
  max-height: 500px;
  width: 100%;
  margin-top: 50px;
  background-repeat: no-repeat;
  background-size: cover;
  transition: background-image 1s ease;
  z-index: -1;
  &:before,
  &:after {
    display: block;
    position: absolute;
    top: 0;
    width: 100%; // container에 준 여백값보다 크지 않게 사이즈 지정하기 (swiper-slide의 클릭 이벤트에 영향을 주지 않고, 이렇게 지정해야 그라데이션이 영역 내부에 있는 탭이 스크롤 하기 전엔 영향을 주지 않음)
    height: 100%;
    z-index: 0;
    content: "";
  }
  &:before{
    background-color: hsla(210, 11%, 15%, 0.3);
  }
  &:after {
    bottom: 0;
    background: linear-gradient(0deg, #212529 0%, hsla(210, 11%, 15%, 0.2) 25%, hsla(210, 11%, 15%, 0) 50%, hsla(210, 11%, 15%, 0.2) 75%, #212529 100%);
    // background: linear-gradient(180deg, #212529 -20.19%, rgba(33, 37, 41, 0.8) 18.31%, rgba(33, 37, 41, 0) 75%);
  }
}

#header-overlay{
  margin-bottom: 350px
}

#body {
  width: 90%;
  background-color: #212529;
  border: 1px solid hsla(210,16.7%,97.6%, 0.1);
  padding: 1rem 0rem;
}

</style>