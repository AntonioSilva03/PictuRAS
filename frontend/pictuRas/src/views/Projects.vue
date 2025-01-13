<template>
    <div class="main-layout">
        <Navbar id="nav"></Navbar>
      
    </div>
</template>


<script>

import Navbar from '../components/Navbar.vue';

export default {
    name: 'Landing',
    components: {
        Navbar,
    },
}

</script>


<style scoped>
    .main-layout {
        display: flex;
        flex-direction: column;
        grid-template-areas:
            "nav nav"
            ". .";
        overflow: auto;
        gap:0px;
        overflow-x: hidden;
    }
</style>