<template>
<div>
  <Search/>
  <div class="headContainer">
    <div class="profile-dropdown">
      <button class="profile-button">
        <span class="material-icons">
          person
        </span>
      </button>
      <div class="dropdown-list">
        <a href="#">My Profile</a>
        
        <a href="#">Sign Out</a>
        
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Search from './Search.vue';
export default {
  name: 'Header',
  components: {
    Search,
  }
}
</script>