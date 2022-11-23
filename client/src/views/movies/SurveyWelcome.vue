<template>
  <div>
    <h1>{{username}} 님, 좋아하는 콘텐츠를 5개 선택하세요.</h1>
    <MovieListSurvey/>
  </div>
</template>

<script>
import MovieListSurvey from '@/components/MovieListSurvey'

export default {
  name: 'SurveyWelcome',
  components: {
    MovieListSurvey,
  },
  method: {

  },
  computed : {
    username () {
      return this.$cookies.get("username")
    },
  }
}
</script>

<style lang="scss" scoped>
#surveyBox {
  height: auto;
}
</style>