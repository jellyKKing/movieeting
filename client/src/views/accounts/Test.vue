<template>
  <div>
    <h1>확인용</h1>
    <button @click="getTest">확인</button>
    {{ res }}

  </div>
</template>

<script>
export default {
  name: 'Test',
  data(){
    return{
      res : this.$route.params.res
    }
  },
  methods : {
    getTest() {
      console.log($.cookie)
    }
  }
}
</script>
