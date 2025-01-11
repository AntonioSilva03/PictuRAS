import { defineStore } from 'pinia';
import axios from 'axios';

export const useSessionStore = defineStore('session', {
  state: () => ({
    user: null, // Stores user information if logged in
    isAnonymous: true, // Tracks whether the user is anonymous
    sessionData: {}, // Optional: Store temporary data like cart items
  }),
  getters: {
    isLoggedIn: (state) => !state.isAnonymous && state.user !== null, 
  },
  actions: {
    async fetchSession() {
      try {
        const response = await axios.get('/api/session', { withCredentials: true });
        const { user, sessionData } = response.data;

        this.user = user || null;
        this.isAnonymous = !user;
        this.sessionData = sessionData || {};
      } catch (error) {
        console.error('Failed to fetch session:', error);
        this.user = null;
        this.isAnonymous = true;
        this.sessionData = {};
      }
    },
    async login(credentials) {
      try {
        const response = await axios.post('/api/login', credentials, { withCredentials: true });
        this.user = response.data.user;
        this.isAnonymous = false;
      } catch (error) {
        console.error('Login failed:', error);
        throw error;
      }
    },
    async logout() {
      try {
        await axios.post('/api/logout', {}, { withCredentials: true });
        this.user = null;
        this.isAnonymous = true;
        this.sessionData = {};
      } catch (error) {
        console.error('Logout failed:', error);
        throw error;
      }
    },
    setSessionData(data) {
      this.sessionData = { ...this.sessionData, ...data };
    },
  },
});
