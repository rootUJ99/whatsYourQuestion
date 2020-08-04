import {createRouter, createWebHistory} from 'vue-router';
import Home from '../Pages/Home.vue';
import Question from '../Pages/Question.vue';
const routerHistory = createWebHistory()

const router = createRouter({
  history: routerHistory,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/question',
      name: 'question',
      component: Question,
    },
  ]
})


export default router;