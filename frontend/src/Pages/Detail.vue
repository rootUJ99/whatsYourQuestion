<template>
  <div class="hcenter">
    <div class="flex_column">
      <div class="card_list">
        {{ list?.question?.question }}
      </div>
      <div v-if="list?.answers?.length">
        <div v-for="(a,index) in list?.answers" class="card_list" :key="a.id">
          <p>{{ a.answer }}</p>
          <div v-if="a.comment.length">
            <div v-for="c in a.comment" :key="c.id">
              <div class="comment_container">
                <div class="veritcal_hr" />
                {{ c.comment }}
              </div>
            </div>
          </div>
          <textarea class="input_answer" name="comment" v-model="comment[index]" />
          <button class="answer_button" @click="onSubmitComment(a.id, index)">
            Comment
          </button>
        </div>
      </div>
      <div class="card_list">
        <textarea class="input_answer" name="answer" v-model="answer" />
        <button class="answer_button" @click="onSubmit">Answer</button>
      </div>
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
import {ref, onMounted} from 'vue';
export default {
  name: "Question",
  // data() {
  //   return {
  //     list: null,
  //     answer: null,
  //     comment: [],
  //   };
  // },
  
  // async mounted() {
  //   try {
  //     const res = await axios.get(
  //       `http://localhost:8000/api/question-answer-list/${this.$route.params.id}/`
  //     );
  //     console.log(res.data);
  //     this.list = res?.data;
  //   } catch (err) {
  //     console.log("err", err);
  //   }
  // },
  // methods: {
  //   async onSubmit() {
  //     try {
  //       const res = await axios.post("http://localhost:8000/api/post-answer", {
  //         answer: this.answer,
  //         question_id: this.list.question.id,
  //         user_id: this.list.question.user_id,
  //       });
  //       this.list = res?.data;
  //       this.answer = null;
  //     } catch (err) {
  //       console.log("err", err);
  //     }
  //     // this.answer=null;
  //   },
  //   async onSubmitComment(answer_id, index) {
  //     try {
  //       const res = await axios.post("http://localhost:8000/api/post-comment", {
  //         comment: this.comment[index],
  //         answer_id,
  //         user_id: this.list.question.user_id,
  //         question_id: this.list.question.id,
  //       });
  //       this.list = res?.data;
  //       delete this.comment[index]
  //     } catch (err) {
  //       console.log("err", err);
  //     }
  //   },
  // },

  setup(props, ctx){
    const list = ref(null);
    const answer = ref(null);
    const comment = ref([]);

    onMounted(async ()=>{
      try {
        console.log(ctx.attrs.get, 'router');
        // const new Url
        const res = await axios.get(
        `http://localhost:8000/api/question-answer-list/${1}/`
        // const res = await axios.get(
        // `http://localhost:8000/api/question-answer-list/${ctx.root.$route.params.id}/`
      );
        console.log(res.data);
        list.value = res?.data;
      } catch (err) {
        console.log("err", err);
      }
    });

    const onSubmit = async () => {
      try {
        console.log(ctx, 'router');
        const res = await axios.post("http://localhost:8000/api/post-answer", {
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
        const res = await axios.post("http://localhost:8000/api/post-comment", {
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
};
</script>
