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
    width: 100%;
    height: 100%;
    gap: 30px;
    padding-top: 20px;
}

.btn-wrapper button:nth-child(1) {
}

.btn-wrapper button:nth-child(2) {
    top: 100px;
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