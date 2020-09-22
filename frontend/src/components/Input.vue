<template>
  <input type="text" class="input_style" :placeholder="placeholder" 
    :value="value" 
    @input="$emit('update:value', $event.target.value)"
  />
</template>
<script lang="ts">
import {defineComponent, ref} from 'vue'
export default defineComponent({
  name: 'Input',
  props: ["value", "placeholder"],
  // model: {
  //   prop: "value",
  //   event: "update"
  // },
  setup: (props, {emit}) => {
    console.log('props', props);
    // const input = ref(value)
    // console.log('input');
    // const change = (e) => {
    // console.log('value',value)
    //     emit('input', value)
    // }
    return {
      // change,
    }
  }
})
</script>
<style scoped>
  .input_style {
    border-radius: 0.4rem;
    padding: 0.7rem;
    border: none;
    outline: none;
  }
</style>