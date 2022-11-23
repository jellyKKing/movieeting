<template>
  <div>
    <h1>MovieListSurvey</h1>
    <!-- {{ movies }} -->
    <swiper ref="filterSwiper" :options="swiperOption" role="tablist">
      <swiper-slide role="tab" v-for="movie in movies" :key=movie.id>
        <MovieListItem :movie=movie @change="change"/>
      </swiper-slide>
      <div class="swiper-scrollbar" slot="scrollbar"></div>
    </swiper>
  </div>
</template>

<script>
import axios from 'axios'
import { swiper, swiperSlide } from 'vue-awesome-swiper'

import MovieListItem from '@/components/MovieListItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieListSurvey',
  components: {
    swiper,
    swiperSlide,
    MovieListItem,
  },
  data() {
    return {
      movies: null,
      moviesSelected: null,
      swiperOption: {
        direction: 'vertical',
        slidesPerView: '3',
        // slidesPerColumn: 4,
        spaceBetween: 35, // swiper-slide 사이의 간격 지정
        slidesOffsetBefore: 0, // slidesOffsetBefore는 첫번째 슬라이드의 시작점에 대한 변경할 때 사용
        slidesOffsetAfter: 0, // slidesOffsetAfter는 마지막 슬라이드 시작점 + 마지막 슬라이드 너비에 해당하는 위치의 변경이 필요할 때 사용
        freeMode: false, // freeMode를 사용시 스크롤하는 느낌으로 구현 가능
        mousewheel: true,
        // centerInsufficientSlides: true, // 컨텐츠의 수량에 따라 중앙정렬 여부를 결정함
        // autoplay: {
        //   disableOnInteraction: true,
        // },
        scrollbar: {
          el: '.swiper-scrollbar'
        },
      }
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
  },
  created() {
    this.getRandom()
  },
}
</script>


<style lang="scss" scoped>
  .swiper-container {
    .swiper-wrapper {
      .swiper-slide {
        width: auto; // auto 값을 지정해야 슬라이드의 width값이 텍스트 길이 기준으로 바뀜
        height: auto;
        min-width: 56px; // min-width를 지정하지 않을 경우 텍스트가 1개 내지는 2개가 들어갈 때 탭 모양이 상이할 수 있으므로 넣어준다.
        // padding: 0px 14px;
        font-size: 14px;
        line-height: 36px;
        text-align: center;
        // color: #84868c;
        border: 0;
        // border-radius: 18px;
        appearance: none;
        cursor: pointer;
        justify-content: center;
        display: flex;
      }
    }
  }
</style>