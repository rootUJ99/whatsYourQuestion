<template>
  <div class="card" :class="class">
    <div>
      <slot/>
    </div>
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
    padding: 3rem 3rem;
    color: #ffffff;
    border-radius: 0.5rem;
  }
</style>