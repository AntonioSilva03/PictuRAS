import { defineStore } from 'pinia';
import axios from 'axios';

export const useProfileStore = defineStore('profileStore', {
    state: () => ({
        profile: {
            id: '1',
            username: 'jmf',
            email: 'jmf@example.com',
            status: 'premium',
        },
        loading: false,
        error: null
    }),

    actions: {
        async fetchProfile(userId) {
            this.loading = true;
            this.error = null;
            
            try {
                // const response = await axios.get(`/api/users/${userId}`);
                // this.profile = response.data;
                console.log(`Fetching profile for user ID: ${userId}`);
            }
            catch (error) {
                this.error = `Failed to fetch profile for user ID: ${userId}`;
                console.error(error);
            }
            finally {
                this.loading = false;
            }
            
        }
    },

    getters: {
        displayName: (state) => {
            return state.profile.fullName || state.profile.username || 'Anonymous User';
        }
    }
});