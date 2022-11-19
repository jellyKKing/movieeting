<template >
  <div>
    <div id="noiseImg">
      <img :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`" width="500px">
    </div>
    <h1>Detail</h1>
    {{ movie.title }}
    <br>
    <div>
      <div
        v-for="actor in movie.actors"
        :key=actor.id
        class="btn btn-primary m-1 rounded-pill"
      >
        {{ actor.name }}
      </div>
    </div>
    <div>
      <div
        v-for="keyword in movie.keywords"
        :key=keyword.id
        class="btn btn-success m-1 rounded-pill"
      >
        {{ keyword.name }}
      </div>
    </div>
    <div>
      <div
        v-for="director in movie.directors"
        :key=director.id
        class="btn btn-primary m-1 rounded-pill"
      >
        {{ director.name }}
      </div>
    </div>

    
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
const bodyElem = document.querySelector('body')

export default {
  name: 'MovieDetail',
  data() {
    return {
      movie_id: this.$route.params.movie_id,
      movie: null,
    }
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie_id}/`,
      })
        .then(res => {
          console.log(res)
          this.movie = res.data
          // bodyElem.style.backgroundImage= `url(https://image.tmdb.org/t/p/original${this.movie.backdrop_path})`
        })
        .catch(err => {
          console.log(err)
        })
    }
  },
  mounted() {
    this.getMovieDetail()
    console.log(bodyElem)
  }
}
</script>

<style>
/* body {
  background-repeat: no-repeat;
  background-size: cover;
} */
</style>