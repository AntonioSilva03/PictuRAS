<template>
    <div class="main-layout">
        <Navbar id="nav"></Navbar>
        <ImageList id="image-list"></ImageList>
        <EditingSpace id="editing-space"></EditingSpace>
    </div>
</template>
  
<script>

    import Navbar from '../components/Navbar.vue';
    import ImageList from '../components/ImageList.vue';
    import EditingSpace from '../components/EditingSpace.vue';

    // Example: Hardcode or get project ID dynamically
    const projectId = 1; // Assume this comes from route params or user selection

    export default {
    name: 'Project',
    components: {
        Navbar,
        ImageList,
        EditingSpace
    },
    };

</script>
  
  <style scoped>
  
  
  .main-layout {
      background-color: aqua;
      display: grid;
      height: 100%;
      width: 100%;
      grid-template-rows: 8% 92%;
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
  