<template>
  <div class="hcenter">
    <div class="flex_column">
        <div class="card_list">
                {{list?.question?.question}}
        </div>
        <div v-if="list?.answers?.length" >
          <div v-for="a in list?.answers" class="card_list" :key="a.id">
              <p>{{a.answer}}</p>
          </div>
        </div>
    <div class="card_list">
        <textarea class="input_answer" name="answer" v-model="answer"/>
        <button class="answer_button" @click="onSubmit">Answer</button>
    </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
export default {
  name: 'Question',
  data() {
    return {
      list: null,
      answer: null,
      }
  },
  async mounted() {
    try {
        const res = await axios.get(`http://localhost:8000/question-answer/${this.$route.params.id}/`);
        console.log(res.data)
        this.list = res?.data
      } catch (err) {
        console.log('err', err)
      }
  },
  methods: {
    async onSubmit(){
      console.log(this.list.question.id)
      try {
        const res = await axios.post('http://localhost:8000/answer-post', {
          answer: this.answer,
          question_id: this.list.question.id,
          user_id:  this.list.question.user_id,
        });
        this.list = res?.data
      } catch(err) {
        console.log('err', err);
      }
      // this.answer=null;
    }
  }
}
</script>