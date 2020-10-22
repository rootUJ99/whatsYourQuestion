<template>
  <div class="hcenter">
    <Card v-if="authType === LOGIN" class="card_width">
      <div class="form_box">
        Login
        <Input
          name="username"
          type="text"
          placeholder="UserName"
          :value="login.username"
          @input="(e) => (login.username = e.target.value)"
        />
        <Input
          name="password"
          type="password"
          placeholder="Password"
          :value="login.password"
          @input="(e) => (login.password = e.target.value)"
        />
        <Button @handleClick="handleLogin">Login</Button>
        <Button @handleClick="handleChange(REGISTER)">or register</Button>
      </div>
    </Card>
    <Card v-if="authType === REGISTER" class="card_width">
      <div class="form_box">
        Register
        <Input
          name="email"
          type="text"
          placeholder="Email"
          :value="register.email"
          @input="(e) => (register.email = e.target.value)"
        />
        <Input
          name="username"
          type="text"
          placeholder="UserName"
          :value="register.username"
          @input="(e) => (register.username = e.target.value)"
        />
        <Input
          name="password"
          type="password"
          placeholder="Password"
          :value="register.password"
          @input="(e) => (register.password = e.target.value)"
        />
        <Input
          name="password2"
          type="password"
          placeholder="Confirm Password"
          :value="register.password2"
          @input="(e) => (register.password2 = e.target.value)"
        />
        <Button @handleClick="handleRegister">Register</Button>
        <Button @handleClick="handleChange(LOGIN)">or Login</Button>
      </div>
    </Card>
  </div>
</template>

<style scoped>
.secondry_button {
  background: white;
  padding: 0.5rem;
  border: 0.1rem solid gray;
  border-radius: 0.2rem;
}
.card_width {
  display: flex;
  justify-content: center;
  width: 80%;
}
.form_box {
  display: grid;
  grid-template-rows: 1fr;
  grid-gap: 0.5rem;
  width: 20rem;
}
</style>

<script>
import axios from "axios";
import { defineComponent, ref, reactive } from "vue";
import { useRouter } from "vue-router";
import { setToken } from "../utils";
import Card from "../components/Card.vue";
import Button from "../components/Button.vue";
import Input from "../components/Input.vue";
export default defineComponent({
  name: "Auth",
  components: {
    Card,
    Button,
    Input,
  },
  setup() {
    const LOGIN = "login";
    const REGISTER = "register";
    const token = ref(null);
    const router = useRouter();
    const login = reactive({
      username: null,
      password: null,
    });
    const register = reactive({
      email: null,
      password: null,
      password2: null,
      username: null,
    });
    const authType = ref(LOGIN);
    const handleChange = (value) => {
      authType.value = value;
    };
    const handleLogin = async () => {
      try {
        const res = await axios.post("http://localhost:8000/api/auth/login", {
          username: login.username,
          password: login.password,
        });
        setToken(res?.data?.token);
        router.push({ name: "home" });
      } catch (err) {
        console.log(err, "error");
      }
    };
    const handleRegister = async () => {
      try {
        const res = await axios.post(
          "http://localhost:8000/api/auth/register",
          {
            email: register.email,
            username: register.username,
            password: register.password,
            password2: register.password2,
          }
        );
        setToken(res?.data?.token);
      } catch (err) {
        console.log(err, "error");
      }
    };
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