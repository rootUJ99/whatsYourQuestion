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
            <a href="#" class="anchor_decoration">
              {{ q.question }}
            </a>
          </li>
        </div>
      </ul>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import { ref, reactive, onMounted, defineComponent } from "vue";
export default defineComponent ({
  name: "Home",
  // setup() {
  //   const question = ref(null);
  //   const questions = ref(null)
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
  //     // this.$router.push({ name: 'detail', params: {id}})
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
      qestion: null,
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
