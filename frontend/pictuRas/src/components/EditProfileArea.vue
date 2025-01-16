<template>
    <div class="profile-area">
        <div v-if="profileStore.loading" class="text-center">
            Loading...
        </div>

        <div v-else-if="profileStore.error" class="text-red-500">
            {{ profileStore.error }}
        </div>

        <div v-else class="profile-Container">
            <div class="left-side">
                <img src="/logo-no-text.png" alt="Logo" class="logo1" />
                <h1>Edit Profile</h1>
                <form @submit.prevent="saveChanges">
                    <label for="fullName">Full Name:</label>
                    <input
                        type="text"
                        id="fullName"
                        v-model="editableProfile.fullName"
                        class="form-input"
                    />

                    <label for="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        v-model="editableProfile.username"
                        class="form-input"
                    />

                    <label for="email">Email:</label>
                    <input
                        type="email"
                        id="email"
                        v-model="editableProfile.email"
                        class="form-input"
                    />

                    <label for="password">Current Password:</label>
                    <input
                        type="text"
                        id="password"
                        :value="editableProfile.password"
                        class="form-input"
                        readonly
                    />

                    <!-- Overlay to change password -->
                    <div v-if="isPasswordEditOverlayVisible" class="overlay">
                        <div class="overlay-content">
                            <h2>Edit Password</h2>
                            <label for="newPassword">Current Password:</label>
                            <input
                                type="password"
                                id="newPassword"
                                v-model="editableProfile.currentPassword"
                                class="form-input"
                            />

                            <label for="newPassword">New Password:</label>
                            <input
                                type="password"
                                id="newPassword"
                                v-model="editableProfile.newPassword"
                                class="form-input"
                            />

                            <label for="confirmPassword">Confirm New Password:</label>
                            <input
                                type="password"
                                id="confirmPassword"
                                v-model="editableProfile.confirmPassword"
                                class="form-input"
                            />

                            <div class="profile-buttons">
                                <button type="button" @click="savePasswordChanges">
                                    Save Password
                                </button>
                                <button type="button" @click="togglePasswordEditOverlay">
                                    Cancel
                                </button>
                            </div>
                        </div>
                    </div>

                    <div class="profile-buttons">
                        <button type="button" @click="togglePasswordEditOverlay">
                            Edit Password
                        </button>
                        <button type="submit">
                            Save Changes
                        </button>
                        <RouterLink to="/profile">
                            <button type="button">
                                Cancel
                            </button>
                        </RouterLink>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useProfileStore } from '../stores/ProfileStore';
import { useRouter } from 'vue-router';

const profileStore = useProfileStore();
const router = useRouter();

const editableProfile = ref({
    fullName: '',
    username: '',
    email: '',
    newPassword: '',
    confirmPassword: ''
});

const currentPassword = ref('');
const showPassword = ref(false);
const isPasswordEditOverlayVisible = ref(false);

onMounted(() => {
    profileStore.fetchProfile(1); // Passar o ID do usuário
    editableProfile.value = { ...profileStore.profile };
});

const togglePasswordVisibility = () => {
    showPassword.value = !showPassword.value;
};

const togglePasswordEditOverlay = () => {
    isPasswordEditOverlayVisible.value = !isPasswordEditOverlayVisible.value;
};

const savePasswordChanges = async () => {
    if (editableProfile.value.newPassword !== editableProfile.value.confirmPassword) {
        alert('Passwords do not match.');
        return;
    }

    // Atualizar a senha
    await profileStore.updatePassword(currentPassword.value, editableProfile.value.newPassword);
    alert('Password updated successfully!');
    togglePasswordEditOverlay(); // Fechar a overlay
};

const maskedPassword = computed(() => {
    return '*'.repeat(currentPassword.value.length);
});

const saveChanges = async () => {
    try {
        // Verificar a senha atual antes de fazer qualquer alteração no perfil
        if (currentPassword.value !== '') {
            // Se a senha atual foi preenchida, atualize a senha também
            if (editableProfile.value.newPassword !== editableProfile.value.confirmPassword) {
                alert('New passwords do not match.');
                return;
            }

            await profileStore.updatePassword(currentPassword.value, editableProfile.value.newPassword);
        }

        // Atualizar o resto do perfil
        await profileStore.updateProfile(editableProfile.value);
        alert('Profile updated successfully!');
        router.push('/profile');
    } catch (error) {
        console.error('Failed to update profile:', error);
        alert('Failed to update profile.');
    }
};
</script>

<style scoped>
.profile-area {
    width: 100%;
    display: flex;
    justify-content: center;
}

.profile-Container {
    background-color: #f7f7f7;
    width: 60%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 40px;
    margin-top: 10vh;
    border-radius: 40px;
    box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, 
                 rgba(0, 0, 0, 0.12) 0px -12px 30px, 
                 rgba(0, 0, 0, 0.12) 0px 4px 6px, 
                 rgba(0, 0, 0, 0.17) 0px 12px 13px, 
                 rgba(0, 0, 0, 0.09) 0px -3px 5px;
}

.left-side {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 100%;
}

.logo1 {
    width: 100px;
    height: 100px;
    margin-bottom: 16px;
}

.left-side h1 {
    font-size: 26px;
    margin-bottom: 20px;
}

.form-input {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-size: 16px;
}

.profile-buttons {
    display: flex;
    justify-content: space-between;
    width: 100%;
}

.profile-buttons button {
    padding: 10px 30px;
    border-radius: 20px;
    background: #000000;
    color: #ffffff;
    border: none;
    cursor: pointer;
    transition: 0.25s;
}

.profile-buttons button:nth-child(2) {
    background: #000000;
    color: #ffffff;
}

.profile-buttons button:hover {
    background-color: #000000;
    box-shadow: 0 0 6px #000000;
}

.profile-buttons button>a {
    position: relative;
    z-index: 1;
    text-decoration: none;
    color: #ffffff;
    font-size: 15px;
}

.profile-buttons button:hover>a {
    color: #000000;
}

/* Overlay */
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}

.overlay-content {
    background-color: white;
    padding: 40px;
    border-radius: 10px;
    width: 400px;
    box-shadow: rgba(0, 0, 0, 0.25) 0px 4px 6px;
}

.overlay h2 {
    font-size: 20px;
    margin-bottom: 20px;
}
</style>
