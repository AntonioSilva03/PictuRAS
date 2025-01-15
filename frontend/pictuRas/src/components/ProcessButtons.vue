<template>
    <div class="btn-wrapper">
      <button @click="">Preview</button>
      <button @click="">Process</button>
      <button @click="saveProject()">Save</button>
    </div>
  </template>
  
  <script>
  import { useProjectStore } from '../stores/projectStore';
  import { useEditingToolStore } from '../stores/EditingTool';
  import { storeToRefs } from 'pinia';
  
  export default {
    name: "ProcessButtons",
    setup() {
      const projectStore = useProjectStore();
      const toolsStore = useEditingToolStore();
      const { tools } = storeToRefs(toolsStore);
  
      const saveProject = async () => {
        console.log("here?")
        await projectStore.saveProject(tools.value);
        alert("Project Saved!");

      };
  
      return {
        saveProject,
      };
    },
  };
  </script>
  
  <style scoped>
  .btn-wrapper {
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    gap: 30px;
    padding-top: 20px;
  }
  
  .btn-wrapper button {
    padding: 10px 40px;
    border-radius: 20px;
    background: #000000;
    color: #ffffff;
    border: none;
    cursor: pointer;
    overflow: hidden;
    border: 1px solid #000000;
    transition: 0.25s;
    width: fit-content;
    align-self: center;
  }
  
  .btn-wrapper button:hover {
    background-color: #ffffff;
    box-shadow: 0 0 6px #000000;
    color: #000000;
  }
  </style>
  