<template>
    <div class="main-layout">
        <Navbar id="nav"></Navbar>
        <SidebarProjects />
        <ProjectList/>
    </div>
</template>


<script>

import Navbar from '../components/Navbar.vue';
import SidebarProjects from '../components/Sidebar-Projects.vue';
import ProjectList from '../components/ProjectList.vue';

export default {
    name: 'Projects',
    components: {
        Navbar,
        SidebarProjects,
        ProjectList,

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