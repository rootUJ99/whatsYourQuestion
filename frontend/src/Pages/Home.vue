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
        <div class="card_list" v-for="q in questions" :key="q.id">
          {{ q.username }}
          <li>
            <div class="card_text" @click="getDataFromParam(q.id)" tabindex="0" role="button" aria-pressed="false">
              {{ q.question }}
            </div>
          </li>
        </div>
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
export default defineComponent ({
  name: "Home",
  // setup() {
  //   const question = ref(null);
  //   const questions = ref(null);
  //   const route = useRouter();
  //   onMounted(async () => {
  //     try {
  //       const res = await axios.get("http://localhost:8000/api/question-list");
  //       questions.value = res?.data?.questions;
  //       console.log(questions);
  //     } catch (err) {
  //       console.log("err", err);
  //     }
  //   });

  //   const getDataFromParam = (id) => {
  //     router.push({ name: 'detail', params: {id}})
  //   };
  //   const onSubmitQuestion = async () => {
  //     try {
  //       const res = await axios.post(
  //         "http://localhost:8000/api/post-question",
  //         {
  //           question: question.value,
  //           user_id: 1,
  //         }
  //       );
  //       // console.log(res?.data);
  //       questions.value = res?.data?.questions;
  //       question.value = null;
  //     } catch (err) {
  //       console.log(err);
  //     }
  //   };

  //   return {
  //     getDataFromParam,
  //     onSubmitQuestion,
  //   };
  // },
  data: function(){
    return {
      questions: null,
      question: null,
    }
  },
  async mounted() {
    try {
      const res = await axios.get('http://localhost:8000/api/question-list');
      console.log(res)
      this.questions = res?.data?.questions;
    } catch (err) {
      console.log('err', err)
    }
  },
  methods: {
      getDataFromParam(id) {
          this.$router.push({ name: 'detail', params: {id}})
      },
      async onSubmitQuestion() {
          try {
            const res = await axios.post('http://localhost:8000/api/post-question', {
              question: this.question,
              user_id: 1,
            });
            // console.log(res?.data);
            this.questions = res?.data?.questions;
            this.question = null
          } catch (err){
            console.log(err);
          }
      }
  }
});
</script>
