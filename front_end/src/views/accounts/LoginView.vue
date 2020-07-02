<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">아이디: </label>
      <input v-model="loginData.username" id="username" type="text">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input v-model="loginData.password" id="password" type="password">
    </div>
    <div>
    <button>로그인 하기</button>
    </div>
  </div>
</template> 

<script>
export default {
  name: 'LoginView',
  data () {    // data modeling하기
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  }

}
</script>

<style>

</style>