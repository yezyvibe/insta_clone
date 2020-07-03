<template>
  <div>
    <h1>New Article</h1>
    <div>
      <label for="title">title: </label>
      <input v-model="articleData.title" id="title" type="text">
    </div>
    <div>
      <label for="content">content: </label>
      <textarea v-model="articleData.content" id="content" cols="30" rows="10"></textarea>
    </div>
    <div>
      <button @click="createArticle">작성완료</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = "http://localhost:8000"

export default {
  name: 'CreateView',
  data() {
    return {
      articleData: {
        title: null,
        content: null,
      }
    }
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }

      // article 생성은 Header: Token , Body: {title: , content: } 두 가지 있어야 함
      axios.post(SERVER_URL + '/articles/create/', this.articleData, config) // 장고 서버로 요청하는 url
        .then(res => {
          this.$router.push({ name: 'List'})
          console.log(res.data)
        })
        .catch(err => console.log(err.response.data))
    },
  },

  // CreateView가 처음 생성될 때 로그인 되어 있는지 확인하기
  created() {
    if (!this.$cookies.isKey('auth-token')) {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style>

</style>