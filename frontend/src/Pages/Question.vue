<template>
  <div class="hcenter">
    <div class="flex_column">
        <div class="card_list">
                {{list?.question?.question}}
        </div>
        <div v-if="list?.answers?.length" >
          <div v-for="a in list?.answers" class="card_list" :key="a.id">
              <p>{{a.answer}}</p>
              <div v-if="a.comment.length">
                <div v-for="c in a.comment" :key="c.id">
                  <div class="comment_container">
                    <div class="veritcal_hr"/>
                  {{c.comment}}
                </div>
              </div>
           <textarea class="input_answer" name="comment" v-model="comment"/>
           <button class="answer_button" @click="onSubmitComment(a.id)">Comment</button>
          </div>
        </div>
    <div class="card_list">
        <textarea class="input_answer" name="answer" v-model="answer"/>
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
.veritcal_hr {
}
</style>
<script>
import axios from 'axios';
export default {
  name: 'Question',
  data() {
    return {
      list: null,
      answer: null,
      comment: null,
      }
  },
  async mounted() {
    try {
        const res = await axios.get(`http://localhost:8000/api/question-answer-list/${this.$route.params.id}/`);
        console.log(res.data)
        this.list = res?.data
      } catch (err) {
        console.log('err', err)
      }
  },
  methods: {
    async onSubmit(){
      try {
        const res = await axios.post('http://localhost:8000/api/post-answer', {
          answer: this.answer,
          question_id: this.list.question.id,
          user_id:  this.list.question.user_id,
        });
        this.list = res?.data
        this.answer = null
      } catch(err) {
        console.log('err', err);
      }
      // this.answer=null;
    },
    async onSubmitComment(answer_id) {
      try {
        const res = await axios.post('http://localhost:8000/api/post-comment', {
          comment: this.comment,
          answer_id,
          user_id: this.list.question.user_id,
          question_id: this.list.question.id,
        })
      } catch(err) {
        console.log('err', err);
      }
    }
  }
}
</script>