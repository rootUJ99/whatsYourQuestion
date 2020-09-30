<template>
  <button class="primary-button" :class="class" @click="click()" :disabled="disabled">
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
    disabled: Boolean,
  },
  setup: (_, {emit}) => {
    console.log(_);
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
  .primary-button:disabled{
    background: #667d8a;
    color: #f0f0f0;
  }
</style>