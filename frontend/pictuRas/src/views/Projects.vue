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
import axios from 'axios'
import { useRouter } from 'vue-router';
import { useProjectStore } from '../stores/ProjectStore.js';
import { onMounted, computed } from 'vue';

const api = import.meta.env.VITE_API_GATEWAY;

export default {
    name: 'Projects',
    components: {
        Navbar,
        SidebarProjects,
        ProjectList,
    },
    setup() {
        const router = useRouter();  // Move the router here
        const projectStore = useProjectStore();
        
        // Fetch user status and check for anonymity
        const getUserStatus = async () => {
            try {
                const response = await axios.get(api + '/api/user/status', { withCredentials: true });
                return response.data.status;
            } catch (error) {
                console.error('Error fetching user status:', error);
            }
        };

        // Quick check for anonymous users
        const quickCheck = async () => {
            const userStatus = await getUserStatus();
            if (userStatus === 'anonymous') {
                router.push('/project/undefined');  // Navigate to /project using router
            }
        };

        // Fetch projects on component mount
        onMounted(async () => {
            await quickCheck();
            await projectStore.fetchProjects();
        });

        // Access projects from the store as a computed property
        const projects = computed(() => projectStore.projects);

        return {
            projects,
        };
    },
};
</script>

<style scoped>
.main-layout {
    display: flex;
    flex-direction: column;
    overflow: auto;
    gap: 0px;
    overflow-x: hidden;
}

.content-layout {
    width: 100%;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    overflow-x: hidden;
}
</style>
