<template>
  <div class="overlay">
    <div class="container">
      <div class="d-flex row gx-3 row-cols-auto justify-content-center">
        <div class="d-flex col justify-content-center"
          v-for="movie in movies"
          :key=movie.id
        >
          <MovieListSurveyItem 
          :movie=movie 
          @click.native="cardSelect"
          />
        </div>
      </div>
    </div>
    
    <button @click="selectDone">확인</button>
  </div>
</template>

<script>
import axios from 'axios'

import MovieListSurveyItem from '@/components/MovieListSurveyItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieListSurvey',
  components: {
    MovieListSurveyItem,
  },
  data() {
    return {
      movies: null,
      moviesSelected: null,
    }
  },
  methods: {
    getRandom() {
      axios({
          method: 'get',
          url: `${API_URL}/movies/random`,
      })
        .then(res => {
          this.movies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    selectDone () {
      
    },
    cardSelect(event) {
      const selectedCard = event.currentTarget
      selectedCard.classList.toggle('selected')
      // 선택 / 선택 취소 에밋으로 올려보내주기 위에서 종합할 것.
    },
  },
  mounted() {
    this.getRandom()
  },
}
</script>


<style lang="scss" scoped>
.container{
  // position: relative;
  width: 100%;
  max-height: 850px;
  padding: 20px 0px;
  overflow: scroll;
  overflow-x: hidden;
  // &:before,
  // &:after {
  //   display: block;
  //   position: absolute;
  //   top: 0; // container에 준 여백값보다 크지 않게 사이즈 지정하기 (swiper-slide의 클릭 이벤트에 영향을 주지 않고, 이렇게 지정해야 그라데이션이 영역 내부에 있는 탭이 스크롤 하기 전엔 영향을 주지 않음)
  //   height: 30px;
  //   z-index: 4;
  //   content: "";
  // }
  // &:before {
  //   top: 0;
  //   // background: linear-gradient(0deg, #212529 0%, hsla(210, 11%, 15%, 0.2) 10%, hsla(210, 11%, 15%, 0) 15%, hsla(210, 11%, 15%, 0) 85%, hsla(210, 11%, 15%, 0.2) 90%, #212529 100%);
  //   background: linear-gradient(180deg, #212529 -10%, rgba(33, 37, 41, 0.8) 18.31%, rgba(33, 37, 41, 0) 75%);
  // }
  // &:after {
  //   bottom: 0;
  //   background: linear-gradient(0deg, red -10%, rgba(33, 37, 41, 0.8) 18.31%, rgba(33, 37, 41, 0) 75%);
  // }
}

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: transparent;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: hsla(210,16.7%,97.6%, 0.2);
  border-radius: 5px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: hsla(210,16.7%,97.6%, 0.5);
}
</style>