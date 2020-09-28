<template>
  <button class="primary-button" :class="class" @click="click()">
    <slot/>
  </button>
</template>
<script lang="ts">
import {defineComponent} from 'vue'
export default defineComponent({
  name: 'Button',
  props: {
    handleClick: Function,
    class: String,
  },
  setup: (_, {emit}) => {
    const click =() =>{
      emit('handleClick')
    }
    return{
      click,
    }
  }
})
</script>
<style scoped>
  .primary-button {
    padding: 0.7rem;
    background: var(--accent);
    color: var(--font-color);
    border: none;
    border-radius: 0.4rem;
  }
</style>