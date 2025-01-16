import { defineStore } from 'pinia';
import axios from 'axios';

export const useProfileStore = defineStore('profileStore', {
    state: () => ({
        profile: {
            id: '1',
            fullName: 'João Miguel Lobo Fernandes',
            username: 'jmf',
            email: 'jmf@example.com',
            password: '*******', // Isto deve ser o hash da senha real
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
                // Simular um pedido de API para buscar o perfil
                console.log(`Fetching profile for user ID: ${userId}`);
                // Exemplo de dados recebidos:
                this.profile = { 
                    id: '1',
                    fullName: 'João Miguel Lobo Fernandes',
                    username: 'jmf',
                    email: 'jmf@example.com',
                    password: '*******', 
                    status: 'premium',
                };
            }
            catch (error) {
                this.error = `Failed to fetch profile for user ID: ${userId}`;
                console.error(error);
            }
            finally {
                this.loading = false;
            }
        },

        async updateProfile(updatedProfile) {
            this.loading = true;
            this.error = null;

            try {
                // Aqui você faria uma chamada real para atualizar o perfil no backend
                // Exemplo de requisição com axios
                const response = await axios.put(`/api/users/${this.profile.id}`, updatedProfile);

                // Atualizar os dados locais
                this.profile = response.data;
                console.log('Profile updated:', this.profile);

            } catch (error) {
                this.error = 'Failed to update profile.';
                console.error(error);
            } finally {
                this.loading = false;
            }
        },

        async updatePassword(currentPassword, newPassword) {
            this.loading = true;
            this.error = null;

            try {
                // Verificação da senha atual e atualização da senha
                if (currentPassword !== this.profile.password_hash) {
                    this.error = 'Incorrect current password.';
                    return;
                }

                // Aqui você pode adicionar a lógica de hashing da nova senha antes de armazená-la
                const newPasswordHash = newPassword; // Simule o hashing aqui (ex: bcrypt)

                // Atualizando o perfil com a nova senha
                this.profile.password_hash = newPasswordHash;

                console.log('Password updated successfully!');
            } catch (error) {
                this.error = 'Failed to update password.';
                console.error(error);
            } finally {
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
