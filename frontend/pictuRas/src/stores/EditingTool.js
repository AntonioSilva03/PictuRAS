import { defineStore } from 'pinia'
import axios from 'axios'

export const useEditingToolStore = defineStore('editingTool', {
  state: () => ({
    tools: [],
    activeTool: null
  }),

  actions: {
    async fetchTools() {
      try {

        const response = await axios.get(`${import.meta.env.VITE_API_GATEWAY}/api/tools`)
        const fetchedTools = response.data.map((tool, index) => ({
          ...tool,
          active: false, // Add "active" field
          position: index // Add "position" field
        }))
        this.tools = fetchedTools
      } catch (error) {
        console.error('Failed to fetch tools:', error)
      }
    },

    addTool(name) {
      this.tools.push({
        position: this.tools.length,
        name,
        input_type,
        output_type,
        active: false, // Set active to false by default
        parameters: []
      })
    },

    removeTool(name) {
      this.tools = this.tools.filter(tool => tool.name !== name)
      if (this.activeTool?.name === name) {
        this.activeTool = null
      }
    },

    setActiveTool(name) {
      this.activeTool = this.tools.find(tool => tool.name === name) || null
    },

    addParameter(toolName, parameter) {
      const tool = this.tools.find(t => t.name === toolName)
      if (tool) {
        tool.parameters.push(parameter)
      }
    },

    updateParameterValue(toolName, paramName, value) {
      const tool = this.tools.find(t => t.name === toolName)
      const param = tool?.parameters.find(p => p.name === paramName)
      if (param) {
        param.value = value
      }
    },
    mergeTools(activeTools){
      for (let i = 0;i < activeTools.length; i++){
        for(let j = 0; j < this.tools.length; j++){
          if (this.tools[j].name === activeTools[i].name){
            if (activeTools[i].parameters != null && activeTools[i].parameters.length > 0) {
              this.tools[j].parameters = JSON.parse(JSON.stringify(activeTools[i].parameters));
          }
            
            this.tools[j].position = i;
            this.tools[j].active=true;


            let b = this.tools[j];
            this.tools[j] = this.tools[i];
            this.tools[i] = b;
          }

        }

      }
    }
  },

  getters: {
    getTool: (state) => {
      return (name) => state.tools.find(tool => tool.name === name)
    },

    getParameterValue: (state) => {
      return (toolName, paramName) => {
        const tool = state.tools.find(t => t.name === toolName)
        return tool?.parameters.find(p => p.name === paramName)?.value
      }
    }
  }
})
