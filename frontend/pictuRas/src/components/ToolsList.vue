<template>
    <div class="tools-list">
      <h1>Tools</h1>
      <ul>
        <li
          v-for="tool in tools"
          :key="tool.name"
          :class="{ active: activeTool?.name === tool.name }"
          @click="selectTool(tool.name)"
        >
          {{ tool.name }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import { useEditingToolStore } from '../stores/editingTool'
  import { storeToRefs } from 'pinia'
  
  export default {
    name: 'ToolsList',
    setup() {
      const store = useEditingToolStore()
      const { tools, activeTool } = storeToRefs(store)
      
      const selectTool = (name) => {
        store.setActiveTool(name)
      }
  
      return {
        tools,
        activeTool,
        selectTool
      }
    }
  }
  </script>
  
  <style scoped>
  .tools-list {
    padding: 1rem;
    background-color: #e0e0e0;
    width: 80%;
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  
  li {
    padding: 0.5rem 1rem;
    cursor: pointer;
    margin: 0.25rem 0;
    border-radius: 4px;
  }
  
  li:hover {
    background-color: #f0f0f0;
  }
  
  li.active {
    background-color: #e0e0e0;
    font-weight: bold;
  }
  </style>