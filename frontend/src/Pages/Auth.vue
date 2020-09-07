<template>
  <div class="hcenter">
      <div v-if="authType===LOGIN" class="card form_box">
        Login
        <input class="form_input" name="username" placeholder="UserName" v-model="login.username"/>
        <input class="form_input" name="password" placeholder="Password" v-model="login.password"/>
        <button type="submit" class="ask_button" @click="handleLogin">Login</button>
        <button @click="handleChange(REGISTER)">or register</button>
      </div>
      <div v-if="authType===REGISTER" class="card form_box">
        Register
        <input class="form_input" name="email" placeholder="Email" v-model="register.email"/>
        <input class="form_input" name="username" placeholder="UserName" v-model="register.username"/>
        <input class="form_input" name="password" placeholder="Password" v-model="register.password"/>
        <input class="form_input" name="password2" placeholder="Confirm Password" v-model="register.password2"/>
        <button type="submit" class="ask_button">Register</button>
        <button @click="handleChange(LOGIN)">or Login</button>
      </div>
  </div>
</template>
<style scoped>
</style>
<script>
import axios from 'axios';
import { defineComponent, ref, reactive } from "vue";
import { setToken } from '../utils';
export default defineComponent({
  setup() {
    const LOGIN = "login";
    const REGISTER = "register";
    const token = ref(null);
    const login = reactive({
      username: null, password: null
    });
    const register = reactive({
      email: null, password: null, password2: null, username: null,
    })
    const authType = ref(LOGIN);
    const handleChange = (value) => {
      authType.value = value
    }
    const handleLogin = async () => {
      try {
        const res = await axios.post('http://localhost:8000/api/auth/login', {
          username: login.username,
          password: login.password,
        });
        setToken(res?.data?.token)
      } catch(err) {
        console.log(err, 'error');
      }
    } 
    const handleRegister = async () => {
      try {
        const res = await axios.post('http://localhost:8000/api/auth/login', {
          email: register.email,
          username: register.username,
          password: register.password,
          password2: register.password2,
        });
        setToken(res?.data?.token)
      } catch(err) {
        console.log(err, 'error');
      }
    } 
    return {
      authType,
      LOGIN,
      REGISTER,
      handleChange,
      handleLogin,
      login,
      register,
    };
  },
});
</script>