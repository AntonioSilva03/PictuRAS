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
                <h1>Username: {{ profileStore.profile.username }}</h1>
                <p>Email: {{ profileStore.profile.email }}</p>
                <p>Satus: <b>{{ profileStore.profile.status }}</b></p>
                <button><RouterLink to="/plans">Change plan</RouterLink></button>
            </div>
            <div class="right-side">
                <button><RouterLink to="/projects">My projects</RouterLink></button>
                <div v-if="profileStore.profile.projects && profileStore.profile.projects.length > 0" class="projects-list">
                    <ul>
                        <li v-for="(project, index) in profileStore.profile.projects.slice(0, 4)" :key="index">
                            {{ project.name }}
                        </li>
                    </ul>
                </div>
            </div>
        </div>

    </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useProfileStore } from '../stores/ProfileStore';
import { RouterLink } from 'vue-router';

const profileStore = useProfileStore();


onMounted(async () => {
    await profileStore.fetchProfile();
});
</script>

<style scoped>

.profile-area {
    width: 100%;
    display: flex;
    justify-content: center;
}

.profile-Container {
    background-color: #c5c5c5;
    width: 60%;
    height: auto;
    display: flex;
    justify-content: space-around;
    margin-top: 10vh;
    padding: 70px;
    border-radius: 40px;
    cursor: default;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.2);
}

.left-side {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.left-side b{
    font-weight: normal;
    color: #ffd500;
}

.left-side button {
    background-color: #ffd500;
    color: #000000;
    border: none;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
}

.left-side button a {
    text-decoration: none;
    color: #000000;
}

.right-side button {
    background-color: #000000;
    color: #000000;
    border: none;
    border-radius: 10px;
    padding: 10px;
    cursor: pointer;
}

.right-side button a {
    text-decoration: none;
    color: #ffffff;
}


</style>