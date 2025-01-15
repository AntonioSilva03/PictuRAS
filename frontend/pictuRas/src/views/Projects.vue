<template>
    <div class="main-layout">
        <SidebarProjects />
        <div class="content-layout">
            <Navbar id="nav"></Navbar>
            <ProjectList :projects="projects" />
        </div>
    </div>
</template>


<script>

import Navbar from '../components/Navbar.vue';
import SidebarProjects from '../components/Sidebar-Projects.vue';
import ProjectList from '../components/ProjectList.vue';
import { useProjectStore } from '../stores/ProjectStore.js';
import { onMounted, computed } from 'vue';

export default {
    name: 'Projects',
    components: {
        Navbar,
        SidebarProjects,
        ProjectList,
    },
    setup() {
        const projectStore = useProjectStore();

        // Fetch projects on component mount
        onMounted(() => {
            projectStore.fetchProjects();
        });

         // Use a computed property to access projects from the store
        const projects = computed(() => projectStore.projects);
        console.log(projects)

        return {
            projects,
        };
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