import { defineStore } from 'pinia';
import axios from 'axios';

const api = import.meta.env.VITE_API_GATEWAY;

export const useProfileStore = defineStore('profileStore', {
    state: () => ({
        profile: {
            name: 'jmf',
            email: 'jmf@example.com',
            status: 'premium',
        },
        loading: false,
        error: null
    }),

    actions: {
        async fetchProfile() {
            this.loading = true;
            this.error = null;
            
            try {
                const response = await axios.get(`${api}/api/profile`,{ withCredentials: true } );
                this.profile = response.data;
            }
            catch (error) {
                this.error = `Failed to fetch profile for user ID: ${this.profile.email}`;
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