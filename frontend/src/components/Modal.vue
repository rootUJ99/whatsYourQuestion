<template>
  <div v-if="toggle" class="modal">
    <div class="content">
      <slot />
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default {
  name: "Modal",
  props: {
    toggle: Boolean,
  },
  setup() {},
};
</script>

<style scoped>
.modal {
  position: fixed;
  z-index: 100;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  overflow: auto;
  background-color: rgb(0, 0, 0);
  background-color: rgba(0, 0, 0, 0.4);
  display: grid;
  place-items: center;
}
.content {
  width: 60%;
  height: 60%;
  background: var(--primary);
  border-radius: 2rem;
}
</style>