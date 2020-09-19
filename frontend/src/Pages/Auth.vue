<template>
  <div class="hcenter">
      <div v-if="authType===LOGIN" class="card form_box">
        Login
        <input class="form_input" name="username" type="text" placeholder="UserName" v-model="login.username"/>
        <input class="form_input" name="password" type="password" placeholder="Password" v-model="login.password"/>
        <button type="submit" class="ask_button" @click="handleLogin">Login</button>
        <button class="secondry_button" @click="handleChange(REGISTER)">or register</button>
      </div>
      <div v-if="authType===REGISTER" class="card form_box">
        Register
        <input class="form_input" name="email" type="text"  placeholder="Email" v-model="register.email"/>
        <input class="form_input" name="username" type="text" placeholder="UserName" v-model="register.username"/>
        <input class="form_input" name="password" type="password" placeholder="Password" v-model="register.password"/>
        <input class="form_input" name="password2" type="password" placeholder="Confirm Password" v-model="register.password2"/>
        <button type="submit" class="ask_button" @click="handleRegister">Register</button>
        <button class="secondry_button" @click="handleChange(LOGIN)">or Login</button>
      </div>
  </div>
</template>
<style scoped>
  .secondry_button {
    background: white;
    padding: 0.5rem;
    border: 0.1rem solid gray;
    border-radius: 0.2rem;
  }
</style>
<script>
import axios from 'axios';
import { defineComponent, ref, reactive } from "vue";
import { useRouter } from 'vue-router';
import { setToken } from '../utils';
export default defineComponent({
  setup() {
    const LOGIN = "login";
    const REGISTER = "register";
    const token = ref(null);
    const router = useRouter();
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
        router.push('/')
      } catch(err) {
        console.log(err, 'error');
      }
    } 
    const handleRegister = async () => {
      try {
        const res = await axios.post('http://localhost:8000/api/auth/register', {
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
      handleRegister,
      login,
      register,
    };
  },
});
</script>