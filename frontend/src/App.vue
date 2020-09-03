<template>
  <div>
    <Header/>
    <router-view/>
  </div>
</template>

<script>
import Home from './Pages/Home.vue'
import Header from './components/Header.vue'
import { onMounted } from 'vue'

export default {
  name: 'App',
  components: {
    Home,
    Header,
  },
  setup(props, context) {
    onMounted(()=>{
      console.log(props, 'and ', context);
    })
  }
}
</script>
