<template>
  <textarea
    v-if="type === 'textarea'"
    class="input_style"
    :value="value"
    :class="class"
    :placeholder="placeholder"
    @input="change"
  />
  <input
    v-else-if="typeof type === 'undefined'"
    type="text"
    :value="value"
    class="input_style"
    :class="class"
    :placeholder="placeholder"
    @input="change"
  />
  <input
    v-else
    :value="value"
    :type="type"
    class="input_style"
    :class="class"
    :placeholder="placeholder"
    @input="change"
  />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
export default defineComponent({
  name: "Input",
  props: {
    value: String,
    placeholder: String,
    class: String,
    type: String,
  },
  model: {
    prop: "value",
    event: "update",
  },
  setup: (props, { emit }) => {
    const change = (e) => {
      emit("update:value", props.value);
      console.log("value", props.value);
    };
    return {
      change,
    };
  },
});
</script>

<style scoped>
.input_style {
  border-radius: 0.4rem;
  padding: 0.7rem;
  border: none;
  outline: none;
}
</style>