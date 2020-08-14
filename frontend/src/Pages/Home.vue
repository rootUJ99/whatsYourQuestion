<template>
  <div>

    <div class="hcenter">
        <div class="card">
            <p>
                Be curious ask Questions
            </p>
                <input name="input_question" class="input_question" v-model="question"/>
                <button type="submit" class="ask_button" @click="onSubmitQuestion">Ask</button>
        </div>
    </div>
    <div class="hcenter">
        <ul class="remove_bullet">
            <div class="card_list" v-for="q in questions" :key="q.id" @click="getDataFromParam(q.id)">
                {{q.username}}
                <li>
                    <a href="#" class="anchor_decoration">
                        {{q.question}}
                    </a>
                </li>
            </div>
        </ul>
    </div>
</div>
</template>
<script>

import axios from 'axios';
export default {
    name: 'Home',
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
            this.$router.push({ name: 'question', params: {id}})
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
}
</script>