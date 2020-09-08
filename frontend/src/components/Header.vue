<template>
<div>
  <div class="headContainer">
    <div class="profile-dropdown">
      <button class="profile-button" @click="handleToggle">
        <span class="material-icons">
          person
        </span>
      </button>
      <div class="dropdown-list" v-if="toggle===true && token">
        <button class="dropdown-button" @click="handleLogout">Sign Out</button>
      </div>
      <div class="dropdown-list" v-if="toggle===true && token===null">
        <button class="dropdown-button" @click="handleLogin">Sign In</button>
      </div>
    </div>
    <Search/>
  </div>
</div>
</template>
<style scoped>
  .headContainer {
    width: 5rem;
    padding: 1rem;
    background-color: blueviolet;
    width: 100%;
    display: flex;
    flex-direction: row-reverse;
  }
  .profile-dropdown {
    position: relative;
    display: flex;
    /* flex-direction: row-reverse; */
  }
  .profile-button {
    border-radius: 50%;
    border: 0.1rem solid white;
    background: var(--card-background);
    outline: none;
  }
  .dropdown-list {
    position: absolute;
    z-index: 5;
    display: none;
    top: 2rem;
    width: 200px;
    background: white;
    display: flex;
    flex-direction: column;
  }
  .dropdown-list {
    position: absolute;
    z-index: 5;
    top: 2.5rem;
    right: 0;
    width: 8rem;
    padding: 0.5rem;
    background: white;
  }
  .dropdown-button {
    background: white;
    padding: 0.2rem;
    border: 0.1rem solid gray;
    border-radius: 0.2rem;
  }
</style>
<script>
import { ref, watchEffect } from 'vue';
import { useRouter } from 'vue-router';
import Search from './Search.vue';

import { getToken, removeToken, } from '../utils';
export default {
  name: 'Header',
  components: {
    Search,
  },
  setup() {
    const router = useRouter();
    const toggle = ref(false);
    const token = ref(getToken());
    const handleToggle = () => {
      console.log('man you are pushing it hard')
      toggle.value = !toggle.value
    }
    const handleLogin = () => {
      router.push('auth');
    }
    const handleLogout = () => {
      removeToken();
    }
    return {
      token,
      toggle,
      handleLogin,
      handleLogout,
      handleToggle,
    }
  }
}
</script>