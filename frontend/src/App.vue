<template>
  <div>
    <Header/>
    <router-view></router-view>
  </div>
</template>

<script>
import Home from './Pages/Home.vue'
import Header from './components/Header.vue'

export default {
  name: 'App',
  components: {
    Home,
    Header,
  }
}
</script>
