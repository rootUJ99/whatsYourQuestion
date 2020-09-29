<template>
  <div>
    <div class="hcenter">
      <div class="profile-grid container-width">
        <img src="../assets/profile.webp" class="profile-picture"/>
        <Card class="profile-card">
            <div class="profile-subgrid">
              <h1 class="profile-username">Ujwal Arak</h1>
              <Link @handleClick="handleFollowing"> Following </Link>
              <Link @handleClick="handleFollower"> Follower </Link>
              <Button class="rounded-button">Follow</Button>
            </div>
        </Card>
      </div>
    </div>
    <div class="hcenter">
    <div class="button-container container-width ">
      <Button 
        class="rounded-button"
        :disabled="tabToggle === toggle.question"
        @handleCLick="handleTabChange"
        >
        Questions
      </Button>
      <Button 
        class="rounded-button" 
        :disabled="tabToggle === toggle.answer"
        @handleCLick="handleTabChange"
      >
        Answers
      </Button>
    </div>
    </div>
    <div class="hcenter">
      <Card>
        Holla molla cholla
      </Card>
    </div>
  </div>
  <Modal :toggle="false"/>
</template>

<script>
import { defineComponent, onMounted, ref } from 'vue';
import { useAxios } from '../hooks/useAxios';
import Card from '../components/Card.vue';
import Button from '../components/Button.vue';
import Link from '../components/Link.vue';
import Modal from '../components/Modal.vue';



export default defineComponent({
  name: 'Profile',
  components: {
    Card,
    Link,
    Button,
    Modal,
  },
  setup: ()=> {
    const toggle = {
    question: 'QUESTION',
    answer: 'ANSWER',
    }
    const profileData = ref(null);
    const tabToggle = ref(toggle.question);
    onMounted(async () => {
      try {
        const res = await useAxios('http://localhost:8000/api/profile-info/1');
        console.log(res?.data);
        profileData.value = res?.data;
      } catch (err){
        console.log("err", err);
      }
    })
    const handleFollowing = () => {
      // modal open code
      console.log('yeah you are following');
    }
    const handleFollower = () => {
      // modal open code
      console.log('yeaher you are a follower');
    }
    const handleTabChange = () => {
      if (tabToggle.value === toggle.question) {
        tabToggle.value = toggle.answer;
      } else {
        tabToggle.value = toggle.question;
      }
      console.log(tabToggle.value)
    }
    return {
      handleFollowing,
      handleFollower,
      profileData,
      handleTabChange,
      toggle,
      tabToggle,
    }
  }
})
</script>

<style scoped>
  .profile-picture {
    grid-row: 1/3;
    grid-column: 1/2;
    width: 12rem;
    height: 12rem;
  }
   @media (max-width: 600px){
    .profile-picture {
        width: 8rem;
        height: 8rem;
      }
    .container-width {
        width: 100%;
    }
  }
  .profile-grid {
    display: grid;
    height: 20%;
    grid-template-columns: 0.5fr 1fr 1fr;
    grid-template-rows: 1fr 0.5fr;
    grid-gap: 0.5rem;
  }
  .profile-card {
    width: 100%;
    grid-row: 1/3;
    grid-column: 2/4;
  }
  .profile-subgrid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 0.5fr;
    justify-items: start;
  }
  .profile-username {
    grid-column: 1/4;
  }
  .button-container {
    display: flex;
    margin: 3rem 0 2rem;
    justify-content: space-evenly;
  }
  .container-width {
    width: 80%;
  }
  .rounded-button {
    border-radius: 4rem;
    outline: none;
  }
</style>