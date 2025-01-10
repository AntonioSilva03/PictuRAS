import { defineStore } from 'pinia'

export const useEditingToolStore = defineStore('editingTool', {
  state: () => ({
    tools: [
      {position:0,name:"Brightness",active:false,parameters:[{
        name:'Brightness',
        value:0.5,
        type:'float',
        min_value:0,
        max_value:1
      }]},
      {position:1,name:"Saturation",active:false,parameters:[{
        name:'Saturation',
        value:0.5,
        type:'float',
        min_value:0,
        max_value:1
      }]},
      {position:2,name:"Border",active:false,parameters:[
        {
          name:'border_width',
          value:0,
          type:'int',
          min_value:0,
          max_value:2000
      },
      {
        name:'border_height',
        value:0,
        type:'int',
        min_value:0,
        max_value:2000
    },
    {
      name:'border_color',
      value:"#000000",
      type:'hex',
    },
    
    ]}
],
    activeTool: null
  }),
  // procedimento, posição , ativa?, parametros[]:
  // (nome, valor, tipo, tipo de interface, range)
  // degrees, -90, numerico, slide, [-360,360]


  actions: {
    addTool(name) {
      this.tools.push({
        position,
        name,
        active, // diz se é para ser aplicada, gateway resolve
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