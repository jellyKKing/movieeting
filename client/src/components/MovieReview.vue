<template>
  <div>
    <div class="row">
      <div id="review-form" class="col d-flex flex-row">
        <!-- create review -->
        <div id="review-btn" @click="setRating(5)">
          <i id="review-btn" class="bi bi-hand-thumbs-up-fill"></i>
        </div>
        <div id="review-btn" @click="setRating(0)">
          <i id="review-btn" class="bi bi-hand-thumbs-down-fill"></i>
        </div>
        <input type="text"
          v-model="reviewInput"
        >
        <div id="review-btn" @click="createReview">
          <i class="bi bi-pencil-fill" style="font-size: 20px;"></i>
        </div>
      </div>
    </div>
    <!-- comment box -->
    <div class="d-flex flex-column">
      <div class="vstack gap-3">
        <div id="review-item"
          v-for="comment in reverseComments"
          :key="comment.id"
        >
          <div id="review-prof" class="row p-0 pb-2 mb-2">
            <div class="col">
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
            <div class="col">
              <i v-show="comment.rating!=0" id="review-btn" class="bi bi-hand-thumbs-up-fill"></i>
              <i v-show="comment.rating===0" id="review-btn" class="bi bi-hand-thumbs-down-fill"></i>
            </div>
            <!-- delete -->
            <div class="col" @click="deleteReview(comment)">
              <i class="bi bi-x-lg"></i>
            </div>
            <!-- edit -->
            <div class="col" @click="editReview(comment)">
              <i class="bi bi-pencil-square"></i>
            </div>
          </div>
          <!-- edit from -->
          <div id="review-form" class="col d-flex flex-row">
            <input type="text" style="width: 100%"
              
            >
          </div>
          <div class="row pb-2" style="border-bottom: 1px solid hsla(210,16.7%,97.6%, 0.1);">
            <div class="col">
              {{ comment.id }}
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
      rating: null,
    }
  },
  methods: {
    createReview(){
      const token = this.$cookies.get('jwt')
      if (this.rating === null || this.reviewInput === '') {
        alert('입력하세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie.id}/comments/`,
        headers: {
          'Authorization': `Bearer ${token}`,
        },
        data: {
          content: this.reviewInput,
          rating: this.rating,
        }
      })
        .then(res=>{
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
      this.rating = null
      this.reviewInput = null
      this.$emit('refresh-request')
    },
    setRating(score) {
      this.rating = score
      console.log(this.rating)
    },
    deleteReview(comment) {
      const token = this.$cookies.get('jwt')
      console.log(this.movie.comments)
      console.log(typeof(this.movie.comments))
      // const idx = this.movie.comments.findIndex(function(item) {return item.id === comment.id}) // findIndex = find + indexOf
      const idx = this.movie.comments.indexOf(comment) // findIndex = find + indexOf
      if (idx > -1) this.movie.comments.splice(idx, 1)
      axios({
        method: 'delete',
        url: `${API_URL}/movies/comments/${comment.id}/`,
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
      // this.$emit('refresh-request')
    },
    // editReview(comment) {
    //   const token = this.$cookies.get('jwt')

    // },
  },
  computed: {
    reverseComments() {
      return this.movie.comments.slice().reverse()
    }  
  }
}
</script>

<style lang="scss" scoped>
  * {
    margin: 0;
    padding: 0;
  }
  #review-form{

    input {
      background-color: #212529;
      color: white;
      border: 1px solid hsla(210,16.7%,97.6%, 0.1);
      border-radius: 5px;
      box-shadow: rgba(0, 0, 0, 0.2) 0px 20px 30px;  
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
      overflow: hidden;
      &:hover{
        cursor: pointer;
        scale: 103%;
      }
    }
  }

  #review-item {
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