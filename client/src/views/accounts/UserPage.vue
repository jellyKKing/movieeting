<template>
  <div class="container">
    ddkjflkjdljsk
    <div class="row position-relative">
      <!-- left -->
      <div id="left" class="d-flex flex-column col-sm-12 col-md-6 col-lg-5 col-xl-4 col-xxl-3">
        <div class="d-flex flex-column align-items-center w-100">
          <div class="profile-overlay"></div>
          <div class="profile">
            <img :src="imgUrl" alt="">
          </div>
          <div id="username-bar" class="hstack gap-2 justify-content-center pb-1 mb-2">
            <div style="font-size: 2rem" class="text-truncate">{{ username }}</div>
            <div id="gender" :class="gender">
              <i v-if="gender === 'male'" class="bi bi-gender-male"></i>
              <i v-if="gender === 'female'" class="bi bi-gender-female"></i>
            </div>
          </div>
          <p class="opacity-50">{{ email }}</p>
        </div>
        <br>
        <div id="profile-card" class="row">
          <div class="col">
            <div class="vstack gap-2 m-2">
              <i class="bi bi-heart-fill"></i>
              <hr>
              <p>0</p>
            </div>
          </div>
          <div class="col">
            <div class="vstack gap-2 m-2">
              <i class="bi bi-pencil-fill"></i>
              <hr>
              <p>0</p>
            </div>
          </div>
          <div class="col">
            <div class="vstack gap-2 m-2">
              <i class="bi bi-person-fill" style="scale: 1.2"></i>
              <hr>
              <p>0</p>
            </div>
          </div>
        </div>
      </div>
      <!-- right -->
      <div class="col-sm-12 col-md">
        <!--좋아요, 내가 쓴 리뷰, 써클, 메신저, 칭구-->
        여긴 내용<br>
        -- 좋아요 한 영화들 -- <br>
        {{ user_like_movies }} <br>
        <br>
        -- 사용자가 쓴 리뷰들 -- <br>
        {{ user_created_comments }} 
      </div>
    </div>
    <br>
    <br>

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
const USER_ID = '2527552786'

export default {
  name: 'Test',
  data(){
    return{
      user_like_movies : null,
      user_created_comments : null,
      username : null,
      email : null,
      gender : null,
      imgUrl : null,
    }
  },
  methods : {
    getTest2 () {
      
    }
  },
  computed : {
  },
  mounted(){
    axios({
      method: 'post',
      url: `${API_URL}/accounts/user/${USER_ID}/`,
    })
      .then((res) => {
        console.log(res.data)
        this.username = res.data.username
        this.email = res.data.email
        this.gender = res.data.gender
        this.imgUrl = res.data.imgUrl
        this.user_like_movies = res.data.user_like_movies
        this.user_created_comments = res.data.user_created_comments
      })
  }
}
</script>

<style lang="scss" scoped>
*{
  margin:0;
  padding:0;
}

#left {
  padding: 1rem;
  border-right: 1px solid hsla(210,16.7%,97.6%, 0.1);
  justify-content: center;
  align-items: center;
}
.profile {
  position: absolute;
  top: -6rem;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  width: 10rem;
  min-height: 10rem;
  border: 1px solid hsla(210,16.7%,97.6%, 0.1);
  box-shadow: rgba(0, 0, 0, 0.4) 0px 20px 30px;
  border-radius: 50%;
  margin-bottom: 1rem;
  img{
    width: 100%;
    aspect-ratio: 1/1;
    object-fit: cover;
  }
}
.profile-overlay{
  width: 100%;
  min-height: 5rem;
}

#gender{
  padding: 0;
  margin: 0;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-weight: bolder;
  font-size: 1rem;
  overflow: hidden;
  border: 1px solid hsla(210,16.7%,97.6%, 0.2);
  box-shadow: rgba(0, 0, 0, 0.4) 0px 20px 30px;
  i{
    margin-top: 3px;  
    // margin-right: 2px;
  }
  &.male{
  background-color: #01baef;
  }
  &.female{
  background-color: #e5383b;
  }
}
#username-bar {
  width: 100%;
  border-bottom: 1px solid hsla(210,16.7%,97.6%, 0.2);
}

#profile-card {
  width: 100%;
  border: 1px solid hsla(210,16.7%,97.6%, 0.2);
  border-radius: 5px;
}
</style>