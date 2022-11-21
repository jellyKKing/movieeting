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
            <div v-if="!isLogin">
              <KakaoLogin
                api-key="9e3e0da3c4e60e3fff9e0174f6fca7b1"
                image="kakao_login_btn_small"
                :on-success=onSuccess
                :on-failure=onFailure
                />
            </div>
            <div v-if="isLogin">
              <div class="vr"></div>
              
              <div class="vr"></div>
              <img :src="imgUrl" alt="" width="40px;">
              <router-link :to="{ name: 'MyPage' }" style="text-decoration:none;">{{ username }}님</router-link> 

              <a href="https://kauth.kakao.com/oauth/logout?client_id=19909bfbfb8745d6172a4ab6b541c7e8&logout_redirect_uri=http://localhost:8080/movies" @click="logout">Logout</a>
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
          <router-view @change="change"/>
        </div>
      </div>
      <!-- footer -->
      <modals-container />
      <div v-if="modalShow">hi~</div>
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
import LoginModal from '@/components/LoginModal'
import KakaoLogin from 'vue-kakao-login'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  data: function () {
    return {
      modalShow : false,
    }
  },
  components: {
    KakaoLogin,
    // LoginModal
  },
  methods: {
    change () {
      console.log('에밋 쓰리 됨')
      this.modalShow = true
      console.log(this.modalShow)
      
      this.$modal.show(LoginModal,{
        hot_table : 'data',
        modal : this.$modal },{
            name: 'dynamic-modal',
            width : '330px',
            height : '130px',
            draggable: true,
      })
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
        .then((response)=>{
          console.log('로그인 성공띠')
          this.loginToken(response)
        })
    },
    onFailure (data) {
      console.log(data)
      console.log("failure")
    },
    loginToken: function (res) {
      axios({
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
        },
        url: `${API_URL}/api/token/`,
        data: {
          username: res.data.serializer.username,
          password: res.data.serializer.id,
        }
      })
        .then((res) => {
          console.log('쿠키끗')
          const token = res.data.access 
          this.$cookies.set("jwt", token)
          this.$store.commit('ISLOGIN_CHANGE')

          window.Kakao.API.request({
            url: '/v2/user/me',
            data: {
              property_keys: ['kakao_account.email', 'kakao_account.gender', 'kakao_account.profile'],
            },
          })
          .then((response) => {
            console.log(response)
            this.$store.commit('LOGINDATA_IN', response)
          })
          .catch(function(error) {
            console.log(error)
          })
        })
    },
    logout (){
      this.$cookies.set("jwt", '')
      this.$store.commit('ISLOGIN_CHANGE')
    }
  },
  computed : {
    isLogin () {
      return this.$store.state.isLogin
    },
    username () {
      return this.$store.state.loginData.username
    },
    imgUrl () {
      return this.$store.state.loginData.imgUrl
    },
  }
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

@keyframes jump {
  0%   {transform: translate3d(0,0,0) scale3d(1,1,1);}
  25%  {transform: translate3d(0,30%,0) scale3d(.7,1.5,1);}
  50% {transform: translate3d(0,100%,0) scale3d(1.5,.7,1);}
  75%  {transform: translate3d(0,30%,0) scale3d(.7,1.5,1);}
  100%   {transform: translate3d(0,0,0) scale3d(1,1,1);}
}

body.modal-open {
  padding: 0px !important;
  overflow: auto;
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