<template>
<div>
  <button class="vote-button" @click="handleVote('UPVOTE')">
    <span class="material-icons">
      arrow_circle_up
    </span> 
  </button>
  <button class="vote-button" @click="handleVote('DOWNVOTE')">
    <span class="material-icons">
      arrow_circle_down
    </span> 
  </button>
</div>
</template>

<script>
import { defineComponent } from 'vue';
import { useAxios } from '../hooks/useAxios'
export default defineComponent({
  name: 'Vote',
  components: {},
  props: ['section', 'section_id'],
  setup: () => {
    const handleVote = async (flag) => {
      try {
        const res = await useAxios(
          `http://localhost:8000/api/vote`,{
            flag: flag
          }
        );
        console.log(res?.data);
      } catch (err) {
        console.log(err);
      }
    }
    return {
      handleVote,
    }
  }
});
</script>

<style>
.vote-button{
  border: none;
  background: transparent;
  outline: none;
}
</style>