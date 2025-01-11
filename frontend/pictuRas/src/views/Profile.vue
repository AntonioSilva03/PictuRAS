<template>
    <div class="main-layout">
        <Navbar id="nav"></Navbar>
        <ProfileArea id="profileArea"></ProfileArea>
    </div>
</template>

<script>

import Navbar from '../components/Navbar.vue';
import ProfileArea from '../components/ProfileArea.vue';

export default {
    name: 'Profile',
    components: {
        Navbar,
        ProfileArea
    },
};

</script>

<style scoped>
.main-layout {
    background-color: rgb(255, 255, 255);
}

</style>