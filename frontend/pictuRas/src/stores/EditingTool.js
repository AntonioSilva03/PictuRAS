import { defineStore } from 'pinia'

export const useEditingToolStore = defineStore('editingTool', {
  state: () => ({
    tools: [{name:"Brightness",active:false,position:0,parameter:[(0.5,'Numeric','')]},{name:"Watermark",parameter:[]}],
    activeTool: null
  }),
  // procedimento, posição , ativa?, parametros[]:
  // (nome, valor, tipo, tipo de interface, range)
  // degrees, -90, numerico, slide, [-360,360]


  actions: {
    addTool(name) {
      this.tools.push({
        name,
        active, // diz se é para ser aplicada, gateway resolve
        position,
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