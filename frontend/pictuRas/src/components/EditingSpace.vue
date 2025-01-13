<template>
    <div class="editing-space">
      <div v-if="imageStore.selectedImage" class="image-preview" id="prev">
        <img :src="imageStore.selectedImage" alt="Selected Image" />
      </div>
      <div v-else class="placeholder" id="prev">
        <p>No image selected</p>
      </div>
      <ToolsList id="tools"></ToolsList>
      <ParamsSelector v-if="imageStore.selectedImage" id="params"></ParamsSelector>
      <ProcessButtons id="submit-area"/>
    </div>
  </template>
  
  <script setup>
  import { useImageStore } from '../stores/ImageStore';
  import ParamsSelector from './ParamsSelector.vue';
  import ProcessButtons from './ProcessButtons.vue'
  import ToolsList from './ToolsList.vue';
  
  const imageStore = useImageStore();
  </script>
  
  <style scoped>

  .editing-space {
    background-color: #fff;
    display: grid;
    grid-template-areas:
      "prev tools"
      "params submit-area";
    grid-template-columns: 75% 25%;
    width: 100%;
    margin-top: 10%;
  }

  .image-preview {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .image-preview img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }
  
  .placeholder {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    color: #999;
  }
  #prev{
    grid-area: prev;
  }

  #tools{
    grid-area: tools;
  }

  #params{
    grid-area: params;
  }
  #submit-area{
    grid-area: submit-area;
  }

  </style>
  