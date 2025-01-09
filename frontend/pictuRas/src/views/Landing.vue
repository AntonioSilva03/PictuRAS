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
        Navbar
    },
    };

</script>
  
  <style scoped>
  
  
  .main-layout {
      background-color: aqua;
      display: grid;
      height: 100%;
      width: 100%;
      grid-template-rows: 6% 94%;
      grid-template-columns: 25% 75%;
      grid-template-areas:
        "nav nav"
        ". .";
      overflow: auto;
      gap:0px;
  }

  #nav{
    grid-area: nav;
  }
  </style>
  