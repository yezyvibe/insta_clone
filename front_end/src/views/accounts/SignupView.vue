<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">아이디: </label>
      <input v-model="signupData.username" id="username" type="text">
    </div>
    <div>
      <label for="password1">비밀번호: </label>
      <input v-model="signupData.password1" id="password1" type="password">
    </div>
    <div>
      <label for="password2">비밀번호 확인: </label>
      <input v-model="signupData.password2" id="password2" type="password">
    </div>
    <div>
    <button @click="signup">가입하기</button>
    </div>
  </div>
</template> 

<script>
export default {
  name: 'SignupView',
  data () {    // data modeling하기
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null,
      }
    }
  },
  methods: {
    signup() {
      this.$emit('submit-signup-data', this.signupData)
    }
  }

}
</script>

<style>

</style>