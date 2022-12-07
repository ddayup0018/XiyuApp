<template>
  <div id="app">
    <BasePages/>
  </div>
</template>

<script>
import BasePages from '@/components/BasePages.vue'
  export default {
    components:{
      BasePages
    },
    created(){
      document.title = '技师妈咪管理系统'
    },
  }
</script>

<style>
  body {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
</style>
