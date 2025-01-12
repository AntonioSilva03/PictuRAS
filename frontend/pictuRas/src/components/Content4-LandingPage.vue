<template>
    <div class="content4-layout">
      <div class="content4-init">
        <p class="p4-1">Plans</p>
        <h3 class="h4-1">Start using PictuRAS</h3>
        <p class="p4-2">Choose the perfect plan to unlock your creative potential.</p>
      </div>
      <div class="content4-plans"></div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Content4',
  };
  </script>

<style>
/* Content 4 */

.content4-layout {
    background-color: rgba(255, 255, 255, 0.534);
    display: flex;
    min-height: 80vh;
    flex-direction: column;
}

.content4-init {
  text-align: center; 
  width: 100%;
  padding: 2rem 1rem; 
  height: 20vh;
  font-family: Arial, Helvetica, sans-serif; 
}

.p4-1 {
  font-size: 0.8rem; 
  font-weight: bold; 
  letter-spacing: 1px;
  color: #555;
  text-transform: uppercase; 
}

.h4-1 {
  font-size: 1.4rem; 
  font-weight: bold; 
  color: #333; 
}

.p4-2 {
  font-size: 1rem; 
  line-height: 1.5; 
  max-width: 600px; 
  margin: 0 auto; 
}

.content4-plans{
    height: 70vh;
    width: 100%;
    background: linear-gradient(
        to top, 
        #0057b3da, 
        #70c5f9 40%,  
        #ffffff 100%  
    );
}


</style>
  