<template>
  <div>
    {{ username }}
    <br>
    {{ email }}
    <br>
    {{ gender }}
    <div class="profile">
      <img :src="imgUrl" alt="">
    </div>
  </div>
  <!--좋아요, 내가 쓴 리뷰, 써클, 메신저, 칭구-->
</template>

<script>

export default {
  name: 'Test',
  data(){
    return{
      
    }
  },
  methods : {
    getTest2 () {
      
    }
  },
  computed : {
    username () {
      return this.$store.state.loginData.username
    },
    email () {
      return this.$store.state.loginData.email
    },
    gender () {
      return this.$store.state.loginData.gender
    },
    imgUrl () {
      return this.$store.state.loginData.imgUrl
    },
  },
  mounted(){
  }
}
</script>

<style lang="scss" scoped>
.profile {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  width: 5rem;
  min-height: 5rem;
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
</style>