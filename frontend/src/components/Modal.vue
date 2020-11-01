<template>
  <div v-if="toggle" class="modal">
    <div class="content">
      <div 
        class="close-button-container"
        @click="handleClose()"
      > 
        <button class="close-button">x</button>
      </div>
      <h4>{{title}}</h4>
      <slot />
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "Modal",
  props: {
    toggle: Boolean,
    onClose: Function,
    title: String,
  },

  setup(_, {emit}) {
    const handleClose = () => {
      console.log
      emit('onClose');
    };
    return {
      handleClose,
    };
  },

});
</script>

<style scoped>
.modal {
  position: fixed;
  height: 100%;
  margin: 0;
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
  overflow: hidden;
}
.content {
  width: 60%;
  height: 60%;
  background: var(--primary);
  border-radius: 2rem;
  padding: 2rem;
  overflow: scroll;
}

@media(max-width: 600px) {
  .modal {
    align-items: flex-end;
  }
  .content{
    width: 100%;
    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
  }
}

.close-button-container{
  display: flex;
  justify-content: flex-end;
  cursor: pointer;
}

.close-button{
  background-color: var(--accent);
  border: none;
  border-radius: 50%;
  width: 1.5rem;
  height: 1.5rem;
}

</style>