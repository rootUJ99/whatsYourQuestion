<template>
  <div class="card">
    <div>
      {{body}}
    </div>
  </div>
</template>
<script>
import {defineComponent} from 'vue';
export default defineComponent({
  name: 'Card',
  props: {
    body: String,
  },
  setup: (props) => {
    console.log(props);
  }
})
</script>
<style scoped>
  .card {
    background: #394C60;
    padding: 10% 7%;
    color: #ffffff;
    border-radius: 0.5rem;
  }
</style>