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
    <p>{{ movie.id }}</p>
    {{ movie.comments }}
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
      axios({
        method: 'post',
        url: `${API_URL}/movies/${this.movie.id}/comment/`,

        data: {
          content: this.reviewInput,
        }
      })
        .then(res=>{
          console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    }
  }
}
</script>

<style lang="scss" scoped>
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
</style>