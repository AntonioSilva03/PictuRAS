<template>
    <div class="tools-list">
      <h1>Tools</h1>
      <draggable
      v-model="tools"
      tag="ul"
      :active="true"
      @change="updateList"
      >
      <template #item="{ element: tool }">
        
        <li
          :class="{ active: tool.active === true }"
          @click="selectTool(tool.name)"
        >{{ tool.name }}
        </li>

      </template>
      </draggable>
    </div>
  </template>
  
  <script>
  import { useEditingToolStore } from '../stores/EditingTool'
  import { storeToRefs } from 'pinia'
  import draggable from 'vuedraggable';
  
  export default {
    name: 'ToolsList',
    components:{
      draggable
    },
    methods: {
      updateList() {
        this.tools.forEach((item, index) => (item.position = index))
      },
    },
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
    font-weight: bold;
  }
  </style>