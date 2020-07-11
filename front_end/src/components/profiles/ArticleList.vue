<template>
  <div>
    <h1>ArticleList</h1>
    <span>
      {{ articles }}
    </span>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'ArticleList',
  data() {
    return {
      username : this.$route.params.username,
      articles: []
    }
  },
  methods: {
    fetchArticles() {
      axios.get(SERVER_URL + '/articles/' + this.username)
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    }
  },
  created() {
    this.fetchArticles()
  }
}
</script>

<style>

</style>