import { createRouter, createWebHistory } from 'vue-router';
import NotFound from '../views/NotFound.vue';
import Landing from '../views/Landing.vue';
import Login from '../views/Login.vue';
import Project from '../views/Project.vue';
import Register from '../views/Register.vue';
import Profile from '../views/Profile.vue';
import Payment from '../views/Payment.vue';
import PaymentResult from '../views/PaymentResult.vue';
import Plan from '../views/Plan.vue';
import EditProfile from '../views/EditProfile.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing,
      props: true
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/register',
      name: 'Register',
      component: Register,
     },
    {
      path: '/project',
      name: 'project',
      component: Project,
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/editprofile',
      name: 'editprofile',
      component: EditProfile,
    },
    {
      path: '/plan',
      name: 'plan',
      component: Plan,
    },
    {
      path: '/payment',
      name: 'payment',
      component: Payment,
    },
    {
      path: '/payment/result',
      name: 'payment-result',
      component: PaymentResult, 
    },
    {
        path: '/plan',
        name: 'plan',
        component: Plan,
       },
    {
      path: '/:pathMatch(.*)*', // Catch-all route for 404
      name: 'NotFound',
      component: NotFound
    }
  ]
});

export default router;
