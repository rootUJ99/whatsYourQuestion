<template>
  <div class="hcenter">
    <div class="flex_column">
        <div class="card_list">
                {{data?.question?.question}}
        </div>
        
        <!-- {% if answers%}
        {% for a in answers%} -->
        <div v-if="data?.answers?.length" >
          <div v-for="a in data?.answers" class="card_list" :key="a.id">
              <p>{{a.answer}}</p>
          </div>
        </div>
        <!-- {% endfor %}
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
        const res = await axios.get(`http://localhost:8000/question-answer/${this.$route.params.id}/`);
        console.log(res)
        this.data = res?.data
      } catch (err) {
        console.log('err', err)
      }
  }
}
</script>