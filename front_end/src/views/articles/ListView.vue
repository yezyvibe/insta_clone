<template>
  <div>
    <h1>Article List</h1>
    <ul>
      <li v-for="article in articles" :key="`article_${article.id}`">
        {{ article.title }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://localhost:8000' 

export default {
  name: 'ListView',
  data() {
    return {
      articles: []
    }
  },
  methods: {
    // 외부에 있는 것들을 가져올 때는 주로 fetch
    fetchArticles() {
      axios.get(SERVER_URL + '/articles/') //get 요청은 token, body 필요없다 
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    },
  },
  created() {
    this.fetchArticles() // 비동기 요청
  }
};
</script>

<style>

</style>