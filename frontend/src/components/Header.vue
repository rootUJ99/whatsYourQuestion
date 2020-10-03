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
        <button class="dropdown-button" @click="handleProfile">Profile</button>
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
    background-color: var(--primary);
    width: 100%;
    display: flex;
    flex-direction: row-reverse;
    margin-bottom: 2rem;
    border-bottom-left-radius: 1rem;
    border-bottom-right-radius: 1rem;
    position: sticky;
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
    top: 2.5rem;
    right: 0;
    width: 8rem;
    padding: 0.5rem;
    background: var(--background);
    border: 0.2rem solid var(--primary);
    border-radius: 0.2rem;
    display: flex;
    flex-direction: column;
  }
  .dropdown-button {
    background: var(--background);
    padding: 0.2rem;
    border: none;
    outline: none;
    color: var(--accent);
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
      toggle.value = !toggle.value
    }
    const handleLogin = () => {
      router.push({ name:'auth' });
      handleToggle();
    }
    const handleLogout = () => {
      removeToken();
      handleToggle();
      router.push({ name:'auth' });
    }
    const handleProfile = () => {
      router.push({ 
        name: 'profile', 
        params: {id: 1} 
      });
      handleToggle();
    }
    return {
      token,
      toggle,
      handleLogin,
      handleLogout,
      handleToggle,
      handleProfile,
    }
  }
}
</script>