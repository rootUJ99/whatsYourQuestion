<template>
  <div>
    <div class="hcenter">
      <div class="container-width profile-grid">
        <img src="../assets/profile.webp" class="profile-picture" />
        <Card class="profile-card">
          <div class="profile-subgrid">
            <h1 class="profile-username">{{ profileData?.user?.username }}</h1>
            <Link @handleClick="handleFollowing"> Following {{profileData?.following?.length }} </Link>
            <Link @handleClick="handleFollower"> Follower {{profileData?.follower?.length }} </Link>
            <Button
              v-if="getUserData()?.user_id != profileData?.user?.id"
              class="rounded-button"
              @handleClick="handlefollowNew"
              >
              {{checkIfFollowing() ? 'Unfollow' : 'Follow' }}
              </Button
            >
          </div>
        </Card>
      </div>
    </div>
    <div class="hcenter">
      <div class="button-container container-width">
        <Button
          class="rounded-button"
          :disabled="tabToggle === toggle.question"
          @handleClick="handleTabChange"
        >
          Questions
        </Button>
        <Button
          class="rounded-button"
          :disabled="tabToggle === toggle.answer"
          @handleClick="handleTabChange"
        >
          Answers
        </Button>
      </div>
    </div>
    <div v-if="tabToggle === toggle.question" class="card-flex">
      <Card class="catd-item" v-for="q in profileData?.questions" :key="q.id">
        {{ q.question }}
      </Card>
    </div>
    <div v-if="tabToggle === toggle.answer" class="card-flex">
      <Card class="catd-item" v-for="a in profileData?.answers" :key="a.id">
        {{ a.answer }}
      </Card>
    </div>
  </div>
  <Modal :toggle="modalToggle" @onClose="modalClose"/>
</template>

<script>
import { defineComponent, onMounted, ref } from "vue";
import { useAxios } from "../hooks/useAxios";
import Card from "../components/Card.vue";
import Button from "../components/Button.vue";
import Link from "../components/Link.vue";
import Modal from "../components/Modal.vue";
import { getUserData } from "../utils";
export default defineComponent({
  name: "Profile",
  components: {
    Card,
    Link,
    Button,
    Modal,
  },
  props: ["id"],
  setup: ({ id }) => {
    const toggle = {
      question: "QUESTION",
      answer: "ANSWER",
    };
    const profileData = ref(null);
    const modalToggle = ref(false);
    const tabToggle = ref(toggle.question);
    onMounted(async () => {
      try {
        const res = await useAxios(
          `http://localhost:8000/api/profile-info/${id}/`
        );
        console.log(res?.data);
        profileData.value = res?.data;
      } catch (err) {
        console.log("err", err);
      }
    });

    const checkIfFollowing = () => {
      return !!profileData.value?.follower?.find(it => it.profile_following_id === Number(id));
    }

    const handlefollowNew = async () => {
      try {
        const res = await useAxios(`http://localhost:8000/api/follow-unfollow`, {
          user_id: id,
          flag: checkIfFollowing() ? 'UNFOLLOW': 'FOLLOW',
        })
        profileData.value = res?.data;
      } catch (err) {
        console.log("err", err);
      }
    } 
    
    const handleFollowing = () => {
      // modal open code
      modalToggle.value = true;
      console.log("yeah you are following");
    };

    const handleFollower = () => {
      // modal open code
      modalToggle.value = true;
      console.log("yeaher you are a follower");
    };

    const modalClose = () => {
      modalToggle.value = false;
    }

    const handleTabChange = () => {
      console.log(tabToggle.value);
      if (tabToggle.value === toggle.question) {
        tabToggle.value = toggle.answer;
      } else {
        tabToggle.value = toggle.question;
      }
    };
    return {
      handleFollowing,
      handleFollower,
      profileData,
      modalToggle,
      handleTabChange,
      toggle,
      tabToggle,
      getUserData,
      handlefollowNew,
      checkIfFollowing,
      modalClose,
    };
  },
});
</script>

<style scoped>
.profile-grid {
  display: grid;
  height: 20%;
  grid-template-columns: 0.5fr 1fr 1fr;
  grid-template-rows: 1fr 0.5fr;
  grid-gap: 0.5rem;
}

.profile-picture {
  grid-row: 1/3;
  grid-column: 1/2;
  width: 12rem;
  height: 12rem;
}

.profile-card {
  width: 100%;
  grid-row: 1/3;
  grid-column: 2/4;
}

@media (max-width: 600px) {
  .profile-grid {
    width: 100%;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
  }
  .container-width {
    width: 100%;
  }

  .profile-picture {
    grid-row: 1/2;
    grid-column: 1/3;
    justify-self: center;
  }

  .profile-card {
    grid-row: 2/3;
    grid-column: 1/3;
  }
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
  width: 60%;
}
.rounded-button {
  border-radius: 4rem;
  outline: none;
}
.card-flex {
  display: grid;
  width: 100%;
  grid-gap: 0.5rem;
  justify-content: center;
}
.catd-item {
  justify-self: center;
  width: 100%;
}
</style>