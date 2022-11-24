<template>
  <div>
    <h3>{{username}} 님, 좋아하는 콘텐츠를 선택하세요.</h3>
    <p class="opacity-50">선택하신 결과를 바탕으로 무비 큐레이터가 취향맞춤 영화를 추천해드립니다.</p>
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
p {
  border-bottom: 1px solid hsla(210,16.7%,97.6%, 0.1);
  padding-bottom: 1rem;
}
</style>