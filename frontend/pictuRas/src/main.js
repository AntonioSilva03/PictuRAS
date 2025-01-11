import { createApp } from 'vue';
import { createPinia } from 'pinia';
import App from './App.vue';
import router from './router';

import VueColor from '@ckpack/vue-color';

const pinia = createPinia();

const app = createApp(App);
app.use(pinia);
app.use(router);
app.use(VueColor);
app.mount('#app');
