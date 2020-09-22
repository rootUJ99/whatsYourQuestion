<template>
  <div>
    <div class="hcenter">
      <Card>
        <div>
          <p>Be curious ask Questions</p>
          <Input
            name="input_question"
            class="input_question"
            v-model="question"
          />
          <Button @handleClick="onSubmitQuestion">
            Ask
          </Button>
        </div>
      </Card>
    </div>
    <div class="hcenter">
      <ul class="remove_bullet">
        <Card class="card_list" v-for="q in questions" :key="q.id">
          <div @click="getDataFromParam(q.id)" tabindex="0" role="button" aria-pressed="false">
              {{ q.question }}
            </div>
        </Card>
          <!-- {{ q.username }}
        </Card> -->
      </ul>
    </div>
  </div>
</template>
<style scoped>
  .card_text {
    text-decoration: none;
    color: gray;
    outline: none;
    cursor: pointer;
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
    // console.log('this is changing fuck yeah', question);
    onMounted(async () => {
      try {
        const res = await useAxios("http://localhost:8000/api/question-list");
        questions.value = res?.data?.questions;
        console.log(questions);
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
