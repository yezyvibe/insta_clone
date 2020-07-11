<template>
  <div>
    <h1>Profile</h1>
    <MyInfo/>
    <ArticleList/>
  </div>
</template>

<script>
import MyInfo from '@/components/profiles/MyInfo.vue'
import ArticleList from '@/components/profiles/ArticleList.vue'

export default {
  name: 'ProfileView',
  data() {
    return {
      
    }
  },
  components: {
    ArticleList,
    MyInfo
  },
  methods: {

  }
}
</script>

<style>

</style>