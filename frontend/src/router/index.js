import {createRouter, createWebHistory} from 'vue-router';
import Home from '../Pages/Home.vue';
import Detail from '../Pages/Detail.vue';
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
      path: '/detail/:id',
      name: 'detail',
      component: Detail,
      props: (route) => {console.log(route.params.id)}

    },
  ]
})


export default router;