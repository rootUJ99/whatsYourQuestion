<template>
  <input type="text" class="" placeholder="{{placeholder}}" 
    @input="change"
  />
</template>
<script lang="ts">
import {defineComponent, ref} from 'vue'
export default defineComponent({
  name: 'Input',
  props: {
    value: String,
  },
  setup: ({value}, {emit}) => {
    // const input = ref(value)
    console.log('input');
    const change = (e) => {
    console.log('value',value)
        emit('input', value)
    }
    return {
      change,
    }
  }
})
</script>
<style scoped>

</style>