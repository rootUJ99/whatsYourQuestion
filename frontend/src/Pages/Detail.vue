<template>
  <div class="hcenter">
    <div class="flex_column">
      <Card class="card_list">
        <template v-slot:header>
          <CardProfile
            :handleClick="() => pushToProfile(list?.question?.user_id)"
            :name="list?.question?.username"
          />
        </template>
        {{ list?.question?.question }}
      </Card>
      <div v-if="list?.answers?.length">
        <Card v-for="(a, index) in list?.answers" class="card_list" :key="a.id">
          <template v-slot:header>
            <CardProfile
              :handleClick="() => pushToProfile(a?.user_id)"
              :name="a?.username"
            />
          </template>
          <div>
            <p>{{ a.answer }}</p>
            <div v-if="a.comment.length">
              <div v-for="c in a.comment" :key="c.id">
                <div class="comment-container">
                  <div class="veritcal_hr" />
                  <CardProfile
                    :handleClick="() => pushToProfile(c?.user_id)"
                    :name="c?.username"
                  />
                  {{ c.comment }}
                </div>
              </div>
            </div>
            <Input
              type="textarea"
              class="input_answer"
              name="comment"
              :value="comment[index]"
              @input="(e) => (comment[index] = e.target.value)"
            />
            <Button @handleClick="onSubmitComment(a.id, index)">
              Comment
            </Button>
          </div>
        </Card>
      </div>
      <Card class="card_list">
        <Input
          type="textarea"
          class="input_answer"
          name="answer"
          :value="answer"
          @input="(e) => (answer = e.target.value)"
        />
        <Button @handleClick="onSubmit">Answer</Button>
      </Card>
    </div>
  </div>
</template>
<style scoped>
.comment-container {
  padding: 0.7rem;
  margin: 0.5rem;
  border-left: 0.1rem solid gray;
}
</style>

<script>
import axios from "axios";
import { ref, reactive, onMounted, watchEffect, defineComponent } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAxios } from "../hooks/useAxios";
import { getUserData } from "../utils";
import Card from "../components/Card.vue";
import Button from "../components/Button.vue";
import Input from "../components/Input.vue";
import CardProfile from "../components/CardProfile.vue";
export default defineComponent({
  name: "Question",
  props: ["id"],
  components: {
    Card,
    Button,
    Input,
    CardProfile,
  },
  setup(props, ctx) {
    const router = useRouter();
    const list = ref(null);
    const answer = ref(null);
    const comment = ref([]);
    const userData = reactive(getUserData());

    const pushToProfile = (user_id) => {
      router.push({
        name: "profile",
        params: { id: user_id },
      });
    };

    const getDetails = async () => {
      try {
        const res = await useAxios(
          `http://localhost:8000/api/question-answer-list/${props.id}/`
        );
        console.log(res.data);
        list.value = res?.data;
      } catch (err) {
        console.log("err", err);
      }
    };
    // onMounted(getDetails);
    watchEffect(getDetails);
    const onSubmit = async () => {
      try {
        console.log(ctx, "router");
        const res = await useAxios("http://localhost:8000/api/post-answer", {
          answer: answer.value,
          question_id: list.value.question.id,
          user_id: userData.user_id,
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
        const res = await useAxios("http://localhost:8000/api/post-comment", {
          comment: comment.value[index],
          answer_id,
          user_id: userData.user_id,
          question_id: list.value.question.id,
        });
        list.value = res?.data;
        delete comment.value[index];
      } catch (err) {
        console.log("err", err);
      }
    };

    return {
      pushToProfile,
      list,
      answer,
      comment,
      onSubmit,
      onSubmitComment,
    };
  },
});
</script>
