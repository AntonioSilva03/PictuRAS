<template>
  <div class="main-layout">
    <Navbar id="nav"></Navbar>
    <div class="main-part">
      <ImageList id="image-list"></ImageList>
      <EditingSpace id="editing-space"></EditingSpace>
    </div>
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
  background-color: rgb(255, 255, 255);
  height: 100vh;
}

/*
  .main-part {
    display: grid;
      height: 100%;
      width: 100%;
      grid-template-columns: 25% 75%;
      grid-template-areas:
        "image-list editing-space";
      overflow: auto;
      gap:0px;
  }
*/

.main-part {
  flex-grow: 1;
  display: flex;
  height: 100vh;
  overflow: auto;
}

#nav {
    flex-shrink: 0;
}

.main-layout {
    display: flex;
    flex-direction: column;
    height: 100vh;
    max-height: 100vh;
}

.main-part {
    flex-grow: 1;
    overflow-y: auto;
    display: flex;
}

#nav {
    position: sticky;
    top: 0;
}

#image-list {
  grid-area: image-list;
  width: 25%;
}

#editing-space {
  grid-area: editing-space;
  width: 75%;
}
</style>