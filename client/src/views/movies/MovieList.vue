<template>
  <div class="w-90">
    <h1>Movies</h1>
    <div class="d-flex row g-4 justify-content-center">
      <div
        class="d-flex col-3 justify-content-center"
        v-for="movie in movies"
        @click="goToDetail(movie)"
        :key="movie.id"
      >
        <MovieListItem :movie=movie />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/MovieListItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'MovieList', 
    components: {
      MovieListItem,
    },
    data: function () {
      return {
        movies: null,
      }
    },
    methods: {
      getMovies() {
        // const token = localStorage.getItem('jwt')
        axios({
          method: 'get',
          url: `${API_URL}/movies/`,
          // headers: {
          //   'Authorization': `Bearer ${token}`,
          // },
        })
          .then(res => {
            // console.log(res)
            this.movies = res.data
          })
          .catch(err => {
            console.log(err)
          })
      },
      goToDetail(movie) {
        // console.log('클릭', movie.id)
        this.$router.push({name: 'MovieDetail', params: {movie_id: movie.id}})
      }
    },
    mounted() {
      this.getMovies()
    }
}
</script>

<style>

</style>