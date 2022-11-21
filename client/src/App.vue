<template>
  <div id="app" class="position-relative">
    <!-- nav bar -->
    <div id="nav" class="sticky-top">
      <div class="container-fluid">
        <div class="d-flex flex-row justify-content-between">
          <!-- left -->
          <div style="text-align: left;">
            <router-link class="me-auto" :to="{ name: 'Home' }" style="text-decoration:none;">Home</router-link>
          </div>
          <!-- center -->
          <div>
          </div>
          <!-- right -->
          <div>
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
    </div>
    <!-- header bg -->
    <div id="header-overlay"></div>
    <div id="header-bg"></div>
    <!-- router-view -->
    <div style="position: relative; min-height: 100%; padding-bottom: 100px">
      <div class="container-fluid d-flex justify-content-center">
        <div id="body">
          <router-view />
        </div>
      </div>
    <!-- footer -->
      <footer>
        <div class="container d-flex flex-row">
          <div class="d-flex align-items-center mt-3 fw-bold opacity-50">
            <span>팀명</span>
          </div>
          <div class="vstack gap-3 mt-3">
            <div class="hstack gap-3 opacity-50 d-flex w-100 justify-content-end" style="width: 150px;">
              <p class="m-0">송단샘</p>
              <div class="vr"></div>
              <a href="mailto:s2770853@gmail.com"><i class="bi bi-envelope-fill"></i></a>
              <a href="https://github.com/Song-d-s"><i class="bi bi-github"></i></a>
            </div>
            <div class="hstack gap-3 opacity-50 d-flex w-100 justify-content-end" style="width: 150px;">
              <p class="m-0">정민지</p>
              <div class="vr"></div>
              <i class="bi bi-envelope-fill"></i>
              <a href="https://github.com/jellyKKing"><i class="bi bi-github"></i></a>
            </div>
          </div>
        </div>
      </footer>
    </div>
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

*{
  margin: 0;
  padding: 0;
}

#app {
  font-family: IBMPlexSansKR-Regular, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  width: 100%;
  display: flex;
  flex-direction: column;
  // overflow: hidden;
}

#nav {
  padding: 1rem;
  // position: sticky;
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
  margin: 0px;
  padding: 0px;
  margin-top: 50px;
  background-repeat: no-repeat;
  background-position: center top; 
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
    background: linear-gradient(0deg, #212529 0%, hsla(210, 11%, 15%, 0.2) 25%, hsla(210, 11%, 15%, 0) 50%, hsla(210, 11%, 15%, 0.2) 75%, #212529 100%);
    // background: linear-gradient(180deg, #212529 -20.19%, rgba(33, 37, 41, 0.8) 18.31%, rgba(33, 37, 41, 0) 75%);
  }
}

#header-overlay{
  position: relative;
  margin-bottom: 350px
}

#body {
  width: 80%;
  min-width: 342px;
  background-color: #212529;
  border: 1px solid hsla(210,16.7%,97.6%, 0.1);
  padding: 1rem 0rem;
}


footer{
  border-top: 1px solid hsla(210,16.7%,97.6%, 0.1);
  position: absolute;
  bottom: -100px;
  background-color: #1b1f22;
  width: 100%;
  height: 100px;
}
</style>