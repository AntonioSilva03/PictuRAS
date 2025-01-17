<template>
  <div class="btn-wrapper">
    <button @click="preview">Preview</button>
    <button @click="process">Process</button>
    <button @click="saveProject">Save</button>
  </div>
</template>

<script>
import { useProjectStore } from '../stores/ProjectStore';
import { useEditingToolStore } from '../stores/EditingTool';
import { storeToRefs } from 'pinia';
import { useImageStore } from '../stores/ImageStore';

const ws = import.meta.env.VITE_WS_GATEWAY;

export default {
  name: "ProcessButtons",
  setup() {
    const projectStore = useProjectStore();
    const toolsStore = useEditingToolStore();
    const imageStore = useImageStore();
    const { tools } = storeToRefs(toolsStore);

    const ws = import.meta.env.VITE_WS_GATEWAY;
    let websocket = null; // WebSocket instance

    const saveProject = async () => {
      await projectStore.saveProject(tools.value);
      alert("Project Saved!");
    };

    const process = () => {
      // Establish WebSocket connection
      // trocar com o ws
      if(projectStore.selectedProject.tools.length ===0){
        alert("Select at least one tool before processing!")
        return
      }
      websocket = new WebSocket(ws); // Replace with your WebSocket server URL

      websocket.onopen = () => {
        console.log("WebSocket connection established");
        
        // Send a JSON message to the server
        const payload = {
          type: "process",
          project: projectStore.getId()
        };
        websocket.send(JSON.stringify(payload));
        console.log("Message sent:", payload);
        imageStore.enterProcessMode();
      };

      websocket.onmessage = (event) => {
        // Parse the JSON message received from the server
        const message = JSON.parse(event.data);
        console.log("Message from server:", message);

        // Handle the message based on the `action` or content
        if (message.type === "progress" && message.progress < 1.0) {
          imageStore.updateList(message.images)
          console.log(`Update: ${message.progress}`);
        } else if (message.type === "progress" && message.progress === 1.0) {
          alert(`Processing complete!`);
          imageStore.fetchImages(message.project)
          websocket.close(); // Close the WebSocket connection
        }else if (message.type === "error") {
          alert(`Processing error: ${message.progress}`);
          websocket.error(); // Close the WebSocket connection
        }
      };

      websocket.onerror = (error) => {
        console.error("WebSocket error:", error);
        imageStore.leaveProvessMode(true)
      };

      websocket.onclose = () => {
        console.log("WebSocket connection closed");
        imageStore.leaveProvessMode(false)
      };
    };

    const preview = () => {
      // Establish WebSocket connection
      // trocar com o ws
      websocket = new WebSocket(ws); // Replace with your WebSocket server URL

      websocket.onopen = () => {
        console.log("WebSocket connection established");
        
        // Send a JSON message to the server
        const payload = {
          type: "preview",
          project: projectStore.getId(),
          image: imageStore.getSelectedImageId()
        };
        websocket.send(JSON.stringify(payload));
        console.log("Message sent:", payload);
        imageStore.enterPreviewMode();
      };

      websocket.onmessage = (event) => {
        // Parse the JSON message received from the server
        const message = JSON.parse(event.data);
        console.log("Message from server:", message);

        // Handle the message based on the `action` or content
        if (message.type === "progress" && message.progress < 1.0) {
         //  imageStore.updateList(message.images)
          console.log(`Update: ${message.progress}`);
        } else if (message.type === "progress" && message.progress === 1.0) {
          imageStore.updateSelectedImage(message.images);
          alert(`Preview complete!`);
          websocket.close(); // Close the WebSocket connection
        }else if (message.type === "error") {
          alert(`Preview error: ${message.progress}`);
          websocket.error(); // Close the WebSocket connection
        }
      };

      websocket.onerror = (error) => {
        console.error("WebSocket error:", error);
        imageStore.leavePreviewMode(true)
      };

      websocket.onclose = () => {
        console.log("WebSocket connection closed");
        imageStore.leavePreviewMode(false)
      };
    };

    return {
      saveProject,
      process,
      preview,
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
