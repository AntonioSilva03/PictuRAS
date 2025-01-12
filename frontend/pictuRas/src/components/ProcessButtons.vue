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
    position: relative;
}

.btn-wrapper button:nth-child(1) {
    top: 10%;
}

.btn-wrapper button:nth-child(2) {
    top: 30%;
}

.btn-wrapper button {
    padding: 10px 30px;
    border-radius: 20px;
    background: #000000;
    color: #ffffff;
    border: none;
    cursor: pointer;
    overflow: hidden;
    border: 1px solid #000000;
    transition: 0.25s;
    width: fit-content;
    position: absolute;
    align-self: center;
}

.btn-wrapper button:hover {
    background-color: #ffffff;
    box-shadow: 0 0 6px #000000;
    color: #000000;
}

</style>