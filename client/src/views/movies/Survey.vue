<template>
  <div>
    <h1>Welcome Survey</h1>
    <div id="surveyBox">
      <MovieListSurvey/>
    </div>
  </div>
</template>

<script>
import MovieListSurvey from '@/components/MovieListSurvey'

export default {
  name: 'Survey',
  components: {
    MovieListSurvey,
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