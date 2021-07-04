import {createRouter, createWebHistory} from 'vue-router';
import Home from '../Pages/Home.vue';
import Detail from '../Pages/Detail.vue';
import Auth from '../Pages/Auth.vue';
import Profile from '../Pages/Profile.vue';
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
      path: '/profile/:id',
      name: 'profile',
      component: Profile,
      props: true,
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

router.beforeEach((to, from, next) => {
  console.log(getToken(), to.name);
  if (to.name !== 'auth' && !getToken()) next({ name: 'auth' })
  else next()
});

export default router;