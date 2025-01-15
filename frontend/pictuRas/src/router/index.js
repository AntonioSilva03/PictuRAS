import { createRouter, createWebHistory } from 'vue-router';
import NotFound from '../views/NotFound.vue';
import Landing from '../views/Landing.vue';
import Login from '../views/Login.vue';
import Project from '../views/Project.vue';
import Register from '../views/Register.vue'
import Profile from '../views/Profile.vue';
import Projects from '../views/Projects.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'landing',
      component: Landing,
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
      name: 'projectNoId',
      component: Project,
      props: false, // No projectId is passed as a prop
    },
    {
      path: '/project/:projectUrlId',
      name: 'projectWithId',
      component: Project,
      props: true, // Enables passing projectId as a prop
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/:pathMatch(.*)*', // Catch-all route for 404
      name: 'NotFound',
      component: NotFound,
    },
    {
      path:'/projects',
      name: 'projects',
      component: Projects,
    },
  ]
});

export default router;
