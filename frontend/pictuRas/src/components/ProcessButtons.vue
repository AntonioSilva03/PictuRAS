<template>
    <div class="btn-wrapper">
        <button @click="">Preview</button>
        <button @click="">Process</button>
    </div>
</template>
<script>
export default {
    name:"ProcessButtons",
    methods: {
        
    },
    
}
</script>
<style scoped>

.btn-wrapper{

    display: flex;  
    flex-direction: column;
    align-items: center;
    gap:20px;  
    align-self: center;

}

.btn-wrapper button{

}
    
</style>