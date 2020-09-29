<template>
  <div class="hcenter">
    <div class="flex_column">
      <Card class="card_list">
        {{ list?.question?.question }}
      </Card>
      <div v-if="list?.answers?.length">
        <Card v-for="(a,index) in list?.answers" class="card_list" :key="a.id">
          <div>
          <p>{{ a.answer }}</p>
          <div v-if="a.comment.length">
            <div v-for="c in a.comment" :key="c.id">
              <div class="comment_container">
                <div class="veritcal_hr" />
                {{ c.comment }}
              </div>
            </div>
          </div>
          <Input 
            type="textarea" 
            class="input_answer" 
            name="comment" 
            :value="comment[index]"
            @input="e => comment[index] = e.target.value"
           />
          <Button @handleClick="onSubmitComment(a.id, index)">
            Comment
          </Button>
          </div>
        </Card>
      </div>
      <Card class="card_list">
        <Input 
          type="textarea" 
          class="input_answer" 
          name="answer" 
          :value="answer" 
          @input="e => comment[answer] = e.target.value"
        />
        <Button @handleClick="onSubmit">Answer</Button>
      </Card>
    </div>
  </div>
</template>
<style scoped>
.comment_container {
  padding: 0.7rem;
  margin: 0.5rem;
  border-left: 0.1rem solid gray;
}
</style>
<script>
import axios from "axios";
import {ref, onMounted, watchEffect, defineComponent} from 'vue';
import {useAxios} from '../hooks/useAxios';
import Card from '../components/Card.vue';
import Button from '../components/Button.vue';
import Input from '../components/Input.vue';
export default defineComponent ({
  name: "Question",
  props: ['id'],
  components: {
    Card,
    Button,
    Input,
  },
  setup(props, ctx){
    const list = ref(null);
    const answer = ref(null);
    const comment = ref([]);
    const getDetails = async ()=>{
      try {
        const res = await useAxios(
        `http://localhost:8000/api/question-answer-list/${props.id}/`
      );
        console.log(res.data);
        list.value = res?.data;
      } catch (err) {
        console.log("err", err);
      }
    }
    // onMounted(getDetails);
    watchEffect(getDetails);
    const onSubmit = async () => {
      try {
        console.log(ctx, 'router');
        const res = await useAxios("http://localhost:8000/api/post-answer", {
          answer: answer.value,
          question_id: list.value.question.id,
          user_id: list.value.question.user_id,
        });
        list.value = res?.data;
        answer.value = null;
      } catch (err) {
        console.log("err", err);
      }
      // answer.value=null;
    };

    const onSubmitComment = async (answer_id, index) => {
      try {
        const res = await useAxios("http://localhost:8000/api/post-comment", {
          comment: comment.value[index],
          answer_id,
          user_id: list.value.question.user_id,
          question_id: list.value.question.id,
        });
        list.value = res?.data;
        delete comment.value[index]
      } catch (err) {
        console.log("err", err);
      }
    };

    return {
      list,
      answer,
      comment,
      onSubmit,
      onSubmitComment,
    }
  },
});
</script>
