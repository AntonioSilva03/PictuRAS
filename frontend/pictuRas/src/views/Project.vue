<template>
    <div class="main-layout">
        <Navbar id="nav"></Navbar>
        <ImageList id="image-list"></ImageList>
        <EditingSpace id="editing-space"></EditingSpace>
    </div>
</template>
  
<script>
import { useProjectStore } from '../stores/projectStore';
import { useRouter } from 'vue-router';
import Navbar from '../components/Navbar.vue';
import ImageList from '../components/ImageList.vue';
import EditingSpace from '../components/EditingSpace.vue';
import axios from 'axios';

const api = import.meta.env.VITE_API_GATEWAY;

export default {
  name: 'Project',
  components: {
    Navbar,
    ImageList,
    EditingSpace
  },
  setup() {
    const projectStore = useProjectStore();
    const router = useRouter();

    // Check for selected project and user status
    const checkProjectAndUserStatus = async () => {

      if (!projectStore.selectedProject) {

        const userStatus = await getUserStatus(); // Example: Replace with real API or authentication logic

        if (userStatus === 'loggedIn') {

          router.push('/projects'); // Redirect to projects page
        } else if (userStatus === 'anonymous') {
          
          // generate session project
          alert('You are currently Anonymous. Reduced features ');
          projectStore.generateSessionProject();
          console.log(projectStore.selectProject.name)
        }
      }
    };

    // Call the check function when the component mounts
    checkProjectAndUserStatus();
  }
};


const getUserStatus = async () => {
  try {
    const response = await axios.get(api+'/api/user/status', { withCredentials: true });
    return response.data.status;
  } catch (error) {
    console.error('Error fetching user status:', error);
  }
};


</script>
  
  <style scoped>
  
  
  .main-layout {
      background-color: rgb(255, 255, 255);
      display: grid;
      height: 100%;
      width: 100%;
      grid-template-columns: 25% 75%;
      grid-template-areas:
        "nav nav"
        "image-list editing-space";
      overflow: auto;
      gap:0px;
  }

  #nav{
    grid-area: nav;
  }

  #image-list{
    grid-area: image-list;
  }
  #editing-space{
    grid-area: editing-space;
  }
  </style>
  