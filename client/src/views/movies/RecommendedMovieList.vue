<template>
  <div>
    <h1>Welcome RecommendedMovieList</h1>
    <div id="surveyBox">
      <RecommendedMovieItem/>
    </div>
  </div>
</template>

<script>
import RecommendedMovieItem from '@/components/RecommendedMovieItem'

export default {
  name: 'Survey',
  components: {
    RecommendedMovieItem,
  },
  method: {

  },
  created() {
  },
}
</script>

<style lang="scss" scoped>
#surveyBox {
  height: auto;
}
</style>