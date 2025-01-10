<template>
    <form v-if="activeTool" class="wrap" @submit.prevent>
      <ul>
        <li
          v-for="param in activeTool.parameters"
          :key="param.name"
        >
            <div v-if="param.type === 'float'">
            {{ param.name }}
            <input 
                :value="param.value"
                @input="handleInput(param, $event)"
                @blur="handleBlur(param)"
                type="number" 
                :step="0.01" 
                :min="param.min" 
                :max="param.max"
            />
            <ToolSlider 
                v-model="param.value" 
                :min="param.min" 
                :max="param.max" 
                :step="0.01" 
            />
            </div>
            <div v-if="param.type === 'int'">
                {{ param.name }}
                <input 
                    :value="param.value"
                    @input="handleInput(param, $event)"
                    @blur="handleBlur(param)"
                    type="number" 
                    :step="1" 
                    :min="param.min" 
                    :max="param.max"
                    :decimals="0"
                />
                <ToolSlider 
                    v-model="param.value" 
                    :min="param.min" 
                    :max="param.max" 
                    :step="1" 
                    :decimals="0"
                />
            </div>
        </li>
      </ul>
    </form>
</template>

<script>
import { useEditingToolStore } from '../stores/editingTool';
import { storeToRefs } from 'pinia';
import ToolSlider from './ToolSlider.vue';

export default {
  name: 'ParamsSelector',
  components: {
    ToolSlider
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
        param.value = param.min;
      } else {
        param.value = clampValue(param.value, param.min, param.max, param.type === 'int');
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