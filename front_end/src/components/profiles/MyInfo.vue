<template>
  <div>
    <h1>MyInfo</h1>
    <span>
      {{ info }}
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
      username : this.$route.params.username,
      info: []    
    }
  },
  methods: {
    fetchInfo() {
      axios.get(SERVER_URL + '/accounts/'+ this.username)
        .then(res => this.info = res.data)
        .catch(err => console.error(err))
    }
  },
  created() {
    this.fetchInfo()
  }
}
</script>

<style>

</style>