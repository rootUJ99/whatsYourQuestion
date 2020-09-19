<template>
  <div>
    this is profile
  </div>
</template>

<script>
import {defineComponent, onMounted} from 'vue';
export default defineComponent({
  name: 'Profile',
  setup: ()=> {
    onMounted(()=> {
      console.log('holla molla boy');
    })
  }
})
</script>