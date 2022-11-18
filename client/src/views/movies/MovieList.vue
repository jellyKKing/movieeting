<template>
  <div class="">
    <h1>Movies</h1>
    <div class="row">
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie=movie
      />
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
      getMovies: function () {
        // const token = localStorage.getItem('jwt')
        axios({
          method: 'get',
          url: `${API_URL}/movies/`,
          // headers: {
          //   'Authorization': `Bearer ${token}`,
          // },
        })
          .then(res => {
            console.log(res)
            this.movies = res.data
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    mounted() {
      this.getMovies()
    }
}
</script>

<style>

</style>