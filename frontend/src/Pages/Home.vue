<template>
  <div>
    <div class="hcenter">
      <Card>
        <div class="grid_wrapper">
        <p class="header_text">Be curious ask Questions</p>
          <Input
            name="input_question"
            placeholder="What is speed of light??"
            class="ask_input"
            :value="question" @input="e => question = e.target.value"
          />
          <Button class="ask_button" 
          @handleClick="onSubmitQuestion">
            Ask
          </Button>
        </div>
      </Card>
    </div>
    <div class="card_flex">
        <Card class="card_list" v-for="q in questions" :key="q.id" >
          <div @click="getDataFromParam(q.id)" tabindex="0" role="button" aria-pressed="false" class="card_text">
              {{ q.question }}
            </div>
        </Card>
    </div>
  </div>
</template>
<style scoped>
  .card_text {
    text-decoration: none;
    outline: none;
    cursor: pointer;
  }
  .grid_wrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    justify-content: center;
    width: 60%;
    margin: 0.5rem 0;
    grid-gap: 0.3rem;
  }
  .header_text {
    grid-column: 1 / 3;
  }
  .ask_button {
   justify-self: start;
   align-self: center;
  }
  .ask_input {
    align-self: center;
  }
  .card_flex {
    display: grid;
    /* flex-direction: column-reverse; */
    justify-content: center;
  }
</style>
<script>
import axios from "axios";
import { ref, onMounted, defineComponent } from "vue";
import { useRouter} from 'vue-router';
import { useAxios } from '../hooks/useAxios';
import { getToken } from "../utils";
import Card from '../components/Card.vue';
import Button from '../components/Button.vue'
import Input from '../components/Input.vue'
export default defineComponent ({
  name: "Home",
  components: {
    Card,
    Button,
    Input,
  },
  setup() {
    const question = ref(null);
    const questions = ref(null);
    const router = useRouter();
    onMounted(async () => {
      try {
        const res = await useAxios("http://localhost:8000/api/question-list");
        questions.value = res?.data?.questions;
      } catch (err) {
        console.log("err", err);
      }
    });

    const getDataFromParam = (id) => {
      router.push({ name: 'detail', params: {id}})
    };
    const onSubmitQuestion = async () => {
      try {
        const res = await useAxios(
          "http://localhost:8000/api/post-question",
          {
            question: question.value,
            user_id: 1,
          }
        );
        questions.value = res?.data?.questions;
        question.value = null;
      } catch (err) {
        console.log(err);
      }
    };

    return {
      question,
      questions,
      getDataFromParam,
      onSubmitQuestion,
    };
  },

});
</script>
