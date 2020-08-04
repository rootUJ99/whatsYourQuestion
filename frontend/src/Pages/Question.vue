<template>
  <div class="hcenter">
    <div class="flex_column">
        <!-- <div class="card_list">
                {{question}}
        </div> -->
        
        <!-- {% if answers%}
        {% for a in answers%}
        <div class="card_list">
            <p>{{a}}</p>
        </div>
        {% endfor %}
        {% endif %} -->
    <div class="card_list">
        <form>
            <textarea class="input_answer"/>
            <button type="submit" class="answer_button">Answer</button>
        </form>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Question',
  data: function() {
    return {data: null}
  },
  async mounted() {
    try {
        const res = await axios.get('http://localhost:8000/question-answer/1/');
        console.log(res)
        this.questions = res?.data?.questions;
      } catch (err) {
        console.log('err', err)
      }
  }
}
</script>