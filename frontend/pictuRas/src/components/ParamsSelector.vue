<template>
    <form v-if="activeTool" class="wrap" @submit.prevent>
      <ul class="params-list">
        <li
          v-for="param in activeTool.parameters"
          :key="param.name"
        >
            <div v-if="param.type === 'float'" class="slide-wraper">
            <h2>{{ param.name }}</h2>
            <input 
                :value="param.value"
                @input="handleInput(param, $event)"
                @blur="handleBlur(param)"
                type="number" 
                :step="0.01" 
                :min="param.min_value" 
                :max="param.max_value"
            />
            <ToolSlider 
                v-model="param.value" 
                :min="param.min_value" 
                :max="param.max_value" 
                :step="0.01" 
            />
            </div>
            <div v-if="param.type === 'int'" class="slide-wraper">
                <h2>{{ param.name }}</h2>
                <input 
                    :value="param.value"
                    @input="handleInput(param, $event)"
                    @blur="handleBlur(param)"
                    type="number" 
                    :step="1" 
                    :min="param.min_value" 
                    :max="param.max_value"
                    :decimals="0"
                />
                <ToolSlider 
                    v-model="param.value" 
                    :min="param.min_value" 
                    :max="param.max_value" 
                    :step="1" 
                    :decimals="0"
                />
            </div>
            <div v-if="param.type === 'hex'" class="hex-wraper">
                <h2>{{ param.name }}</h2>
                <Sketch v-model="param.value"/>
            </div>
        </li>
      </ul>
      <div class="btn-flex">
        
        <button @click="activeTool.active = true">Apply</button>
        <button @click="activeTool.active = false">Remove</button>
      </div>
      
    </form>
</template>

<script>
import { useEditingToolStore } from '../stores/EditingTool';
import { storeToRefs } from 'pinia';
import ToolSlider from './ToolSlider.vue';
import { Sketch } from '@ckpack/vue-color';


export default {
  name: 'ParamsSelector',
  components: {
    ToolSlider,
    Sketch
  },
  setup() {
    const store = useEditingToolStore();
    const { activeTool } = storeToRefs(store);

    const clampValue = (value, min, max, isInt = false) => {
      let numValue = Number(value);
      
      // Handle NaN case
      if (isNaN(numValue)) {
        return min;
      }
      
      // Clamp value between min and max
      numValue = Math.min(Math.max(numValue, min), max);
      
      // Round if integer
      return isInt ? Math.round(numValue) : numValue;
    };

    const handleInput = (param, event) => {
      const value = event.target.value;
      
      // Allow empty input while typing
      if (value === '') {
        param.value = value;
        return;
      }

      const numValue = Number(value);
      
      // If the value is not a valid number, don't update
      if (isNaN(numValue)) {
        event.target.value = param.value;
        return;
      }

      // Update the value while typing, only enforcing min/max on blur
      param.value = param.type === 'int' ? Math.round(numValue) : numValue;
    };

    const handleBlur = (param) => {
      // Enforce min/max constraints when the input loses focus
      if (param.value === '' || typeof param.value !== 'number') {
        param.value = param.min_value;
      } else {
        param.value = clampValue(param.value, param.min_value_value, param.max_value, param.type === 'int');
      }
    };

    return {
      activeTool,
      handleInput,
      handleBlur
    };
  }
};
</script>

<style scoped>

.wrap{

    display: flex;
    flex-direction: column;
    height: 100%;
    overflow-y: scroll;
    align-items: center;
}

.params-list{

    display: flex;
    flex-direction: column;
    overflow-y: inherit;
    height: 60%;

}

ul {
    list-style: none;
    padding: 0;
  }
  
li {

    display: flex;
    flex-direction: column;
    align-items: center;

  }

.slide-wraper{

    display: flex;
    flex-direction: column;
    align-items: center;

}

.slide-wraper h2{

    font-size: 20px;
    font-weight: 500;

}

.hex-wraper{

    display: flex;
    flex-direction: column;
    align-items: center;

}

.hex-wraper h2{

    font-size: 20px;
    font-weight: 500;

}

.btn-flex{
    display: flex;
    flex-direction: row;
    gap:10px;

  }

</style>