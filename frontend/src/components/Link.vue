<template>
  <button class="link" :class="class" @click="click()">
    <slot />
  </button>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "Link",
  props: {
    handleClick: Function,
    class: String,
  },
  setup(_, { emit }) {
    const click = () => {
      emit("handleClick");
    };
    return {
      click,
    };
  },
});
</script>

<style scoped>
.link {
  outline: none;
  border: none;
  background: transparent;
  font-weight: bold;
  cursor: pointer;
  color: var(--accent);
}
</style>