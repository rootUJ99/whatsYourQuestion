<template>
  <div class="card" :class="class">
    <slot name="header" />
    <slot/>
  </div>
</template>
<script>
import {defineComponent} from 'vue';
export default defineComponent({
  name: 'Card',
  props: {
    body: String,
    class: String,
  },
  setup: (props) => {
    // console.log(props);
  }
})
</script>
<style scoped>
  .card {
    background: var(--primary);
    padding: 2rem 2rem;
    color: #ffffff;
    border-radius: 0.5rem;
  }
</style>