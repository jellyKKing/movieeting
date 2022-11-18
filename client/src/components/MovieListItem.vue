<template>
  <div class="card">
    <img
      class="card-img-top"
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
      alt="poster"
    >
    <div class="focus-content">
      <h3>{{ movie.original_title }}</h3>
      <p>{{ movie.title }}</p>
      <p>{{ movie.overview }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style scoped>
.card {
  width: 15rem;
  height: 30rem;
  padding: 0;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,0.1);
  border-radius: 8px;
  box-sizing: border-box;
  overflow: hidden;
}

.card * {
  transition: 0.3s ease all;
}

.card img {
  margin: 0;
  /* width: 300px; */
  height: 450px;
  object-fit: cover;
  display: block;
}

.card h3 {
  margin: 0;
  padding: 12px 12px 48px;
  line-height: 32px;
  font-weight: 500;
  font-size: 20px;
}

.card .focus-content {
  display: block;
  padding: 8px 12px;
}

.card p {
  margin: 0;
  line-height: 1.5;
}

.card:hover img, .card:focus-within img {
  margin-top: -80px;
}

.card:hover h3, .card:focus-within h3 {
  padding: 8px 12px 0;
}
</style>