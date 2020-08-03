<template>
  <div>

    <div class="hcenter">
        <div class="card">
            <p>
                Be curious ask Questions
            </p>
            <form action="/" method="post">
                <input name="input_question" class="input_question"/>
                <button type="submit" class="ask_button">Ask</button>
            </form>
        </div>
    </div>
    <div class="hcenter">
        <ul class="remove_bullet">
            <div class="card_list" v-for="q in questions" :key="q.id">
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
    name: 'Hello',
    data: function(){
      return {questions: null,}
    },
    async mounted() {
      try {
        const res = await axios.get('http://localhost:8000/question');
        console.log(res)
        this.questions = res?.data?.questions;
      } catch (err) {
        console.log('err', err)
      }
    }
}
</script>