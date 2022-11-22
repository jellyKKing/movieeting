<template>
  <div>
    <div class="row">
      <div class="col">
        <input type="text"
          v-model="reviewInput"
        >
        <div id="review-btn" @click="createReview">
          <i class="bi bi-pencil-fill" style="font-size: 20px;"></i>
        </div>
      </div>
      <div class="col">
      </div>
    </div>
    <div class="d-flex flex-column">
      <div class="vstack gap-3">
        <div id="review-box"
          v-for="comment in movie.comments"
          :key="comment.id"
        >
          <div id="review-prof" class="row p-0 pb-2 mb-2">
            <div class="hstack gap-3">
              <div id="profile-pic" class="p-0">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/1200px-Cat03.jpg">
              </div>
              <div class="vstack">
                <div class="d-flex align-items-center">
                  {{ comment.username }}
                </div>
                <div id="review-date" class="col">
                  {{ new Date(comment.created_at).toDateString() }}
                </div>
              </div>

            </div>
          </div>
          <div class="row pb-2" style="border-bottom: 1px solid hsla(210,16.7%,97.6%, 0.1);">
            <div class="col">
              {{comment.content}} / 테스트 재미없어요 보지 마세요~
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieReview',
  props: {
    movie: Object,
  },
  data() {
    return {
      reviewInput: '',
    }
  },
  methods: {
    createReview(){
      const token = this.$cookies.get('jwt')
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie.id}/comments/`,
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        data: {
          // user_id: this.$store.state.user_id,
          content: this.reviewInput,
        }
      })
        .then(res=>{
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getUserData() {

    },
  }
}
</script>

<style lang="scss" scoped>
  * {
    margin: 0;
    padding: 0;
  }
  #review-btn{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #212529;
    width: 3rem;
    height: 3rem;
    border: 1px solid hsla(210,16.7%,97.6%, 0.1);
    box-shadow: rgba(0, 0, 0, 0.2) 0px 20px 30px;    
    border-radius: 50%;
    transition: scale 0.3s;
    &:hover{
      cursor: pointer;
      scale: 103%;
    }
  }
  #review-box {
    border-radius: 5px;
    border: 1px solid hsla(210,16.7%,97.6%, 0.1);
    padding: 1rem;
  }

  #profile-pic {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    width: 3rem;
    // min-height: 3rem;
    border: 1px solid hsla(210,16.7%,97.6%, 0.1);
    box-shadow: rgba(0, 0, 0, 0.4) 0px 20px 30px;
    border-radius: 50%;
    img{
      width: 100%;
      aspect-ratio: 1/1;
      object-fit: cover;
    }
  }
  
  #review-prof {
    border-bottom: 1px solid hsla(210,16.7%,97.6%, 0.1);
  }

  #review-date {
    font-size: 11px;
    opacity: 50%;
  }
</style>