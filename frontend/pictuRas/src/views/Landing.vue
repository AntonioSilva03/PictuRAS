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
  };
  </script>
  
  <style scoped>
  
  
  .main-layout {
      background-color: aqua;
      display: grid;
      height: 100%; /* Works if parent divs allow it */
      width: 100%;
      grid-template-rows: 1fr 1fr;
      grid-template-columns: 1fr 1fr;
      grid-template-areas:
        "nav nav"
        ". .";
      overflow: auto;
  }

  #nav{
    grid-area: nav;
  }
  </style>
  