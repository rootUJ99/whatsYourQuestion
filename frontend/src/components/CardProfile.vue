<template>
  <div
    tabindex="0"
    role="button"
    aria-pressed="false"
    class="profile"
    @click="click()"
  >
    {{ name }}
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "CardProfile",
  props: {
    handleClick: Function,
    name: String,
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

<style>
.profile {
  text-decoration: none;
  outline: none;
  cursor: pointer;
  font-weight: 500;
  padding-bottom: 0.5rem;
  font-size: 0.8rem;
}
</style>