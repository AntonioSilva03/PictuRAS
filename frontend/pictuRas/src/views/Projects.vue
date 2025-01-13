<template>
    <div class="main-layout">
        <SidebarProjects />
        <div class="content-layout">
            <Navbar id="nav"></Navbar>
            <ProjectList/>
        </div>
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

    .content-layout {
    grid-row: 1 / 2; 
    grid-column: 2 / 3; 
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    overflow-x: hidden;
}

</style>