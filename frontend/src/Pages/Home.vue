<template>
  <div>
    <div class="hcenter">
      <div class="card">
        <p>Be curious ask Questions</p>
        <input
          name="input_question"
          class="input_question"
          v-model="question"
        />
        <button type="submit" class="ask_button" @click="onSubmitQuestion">
          Ask
        </button>
      </div>
    </div>
    <div class="hcenter">
      <ul class="remove_bullet">
        <Card class="card_list" v-for="q in questions" :key="q.id" v-bind:body="q.question"/>
          <!-- {{ q.username }}
          <li>
            <div class="card_text" @click="getDataFromParam(q.id)" tabindex="0" role="button" aria-pressed="false">
              {{ q.question }}
            </div>
          </li>
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
export default defineComponent ({
  name: "Home",
  components: {
    Card,
  },
  setup() {
    const question = ref(null);
    const questions = ref(null);
    const router = useRouter();
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
