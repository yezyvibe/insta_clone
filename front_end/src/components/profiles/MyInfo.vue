<template>
  <div>
    <h1>MyInfo</h1>
    <span>
      게시글 
      팔로워
      팔로우
    </span>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'MyInfo',
  data() {
    return {

    }
  },
  methods: {
    fetchInfo() {
      axios.get(SERVER_URL + '/accounts/profile/')
        .then(res => console.log(res.data))
        .catch(err => console.error(err))
    },
  },
  created() {
    this.fetchInfo()
  }
}
</script>

<style>

</style>