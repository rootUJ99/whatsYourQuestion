<template>
  <div class="hcenter">
    <Card>
      <div class="grid-wrapper">
        <p class="header-text">Be curious ask Questions</p>
        <Input
          name="input_question"
          placeholder="What is speed of light??"
          class="ask-input"
          :value="question"
          @input="(e) => (question = e.target.value)"
        />
        <Button class="ask-button" @handleClick="onSubmitQuestion">
          Ask
        </Button>
      </div>
    </Card>
  </div>
  <div class="card-flex">
    <Card class="card_list" v-for="q in questions" :key="q.id">
      <template v-slot:header>
        <CardProfile
          :handleClick="() => pushToProfile(q.user_id)"
          :name="q.username"
        />
      </template>
      <div
        @click="getDataFromParam(q.id)"
        tabindex="0"
        role="button"
        aria-pressed="false"
        class="card-text"
      >
        {{ q.question }}
      </div>
    </Card>
  </div>
</template>

<style scoped>
.card-text {
  text-decoration: none;
  outline: none;
  cursor: pointer;
}
.grid-wrapper {
  display: grid;
  grid-template-columns: 1fr 0.3fr;
  grid-template-rows: 1fr 1fr;
  justify-content: center;
  width: 100%;
  /* margin: 0.5rem 0; */
  grid-gap: 0.3rem;
}
.header-text {
  grid-column: 1 / 3;
}
.ask-button {
  justify-self: start;
  align-self: center;
}
.ask-input {
  align-self: center;
}
.card-flex {
  display: grid;
  justify-content: center;
  margin-top: 0.5rem;
}
</style>

<script>
import axios from "axios";
import { ref, onMounted, defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useAxios } from "../hooks/useAxios";
import { getToken } from "../utils";
import Card from "../components/Card.vue";
import Button from "../components/Button.vue";
import Input from "../components/Input.vue";
import CardProfile from "../components/CardProfile.vue";
export default defineComponent({
  name: "Home",
  components: {
    Card,
    Button,
    Input,
    CardProfile,
  },
  setup() {
    const question = ref(null);
    const questions = ref(null);
    const router = useRouter();
    onMounted(async () => {
      try {
        const res = await useAxios("http://localhost:8000/api/question-list");
        questions.value = res?.data?.questions;
      } catch (err) {
        console.log("err", err);
      }
    });

    const getDataFromParam = (id) => {
      router.push({ name: "detail", params: { id } });
    };

    const pushToProfile = (user_id) => {
      router.push({
        name: "profile",
        params: { id: user_id },
      });
    };
    const onSubmitQuestion = async () => {
      try {
        const res = await useAxios("http://localhost:8000/api/post-question", {
          question: question.value,
          user_id: 1,
        });
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
      pushToProfile,
    };
  },
});
</script>
