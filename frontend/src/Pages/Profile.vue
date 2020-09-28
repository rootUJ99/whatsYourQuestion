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
      <Button class="rounded-button">
        Questions
      </Button>
      <Button class="rounded-button">
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
import {defineComponent, onMounted} from 'vue';
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
    onMounted(()=> {
      console.log('holla molla boy');
    })
    const handleFollowing = () => {
      // modal open code
      console.log('yeah you are following');
    }
    const handleFollower = () => {
      // modal open code
      console.log('yeaher you are a follower');
    }
    return {
      handleFollowing,
      handleFollower,
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