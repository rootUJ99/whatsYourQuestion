import {createRouter, createWebHistory} from 'vue-router';
import Home from '../Pages/Home.vue';
import Detail from '../Pages/Detail.vue';
import Auth from '../Pages/Auth.vue';
import {getToken} from '../utils';
const routerHistory = createWebHistory()

const router = createRouter({
  history: routerHistory,
  
  routes: [
    {
      path: '/auth',
      name: 'auth',
      component: Auth,
    },
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: Detail,
      props: true,
    },
  ]
})

// router.beforeEach((to, from, next) => {
//   console.log(getToken());
//   if (getToken()) next({ name: 'auth' })
//   else next()
// })
export default router;