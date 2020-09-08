<template>
<div>
  <div class="headContainer">
    <div class="profile-dropdown">
      <button class="profile-button">
        <span class="material-icons">
          person
        </span>
      </button>
      <div class="dropdown-list" v-if="token">
        <button @click="handleLogout">Sign Out</button>
      </div>
      <div class="dropdown-list" v-if="token===null">
        <button @click="handleLogin">Sign In</button>
      </div>
    </div>
    <Search/>
  </div>
</div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Search from './Search.vue';

import { getToken, removeToken } from '../utils';
export default {
  name: 'Header',
  components: {
    Search,
  },
  setup() {
    const router = useRouter();
    const handleLogin = () => {
      router.push('auth');
    }
    const handleLogout = () => {
      removeToken();
    }
    const token = ref(getToken());
    return {
      token,
      handleLogin,
      handleLogout,
    }
  }
}
</script>