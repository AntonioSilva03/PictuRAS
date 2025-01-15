<template>
    <div class="plan-box" :class="planType">
        <h2>{{ title }}</h2>
        <ul>
            <li v-for="feature in features" :key="feature">{{ feature }}</li>
        </ul>
        <div class="plan-footer">
            <h3>{{ price }}</h3>
            <button @click="onChoosePlan" :class="`${planType}-btn`">
                Prosseguir →
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "PlanCard",
    props: {
        title: { type: String, required: true },
        features: { type: Array, required: true },
        price: { type: String, required: true },
        planType: { type: String, required: true },
        onChoosePlan: { type: Function, required: true },
    },
};
</script>

<style scoped>
.plan-box {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: rgba(0, 0, 0, 0.25) 0px 4px 6px;
    text-align: center;
    width: 300px;
    height: 350px;
    transition: transform 0.3s ease;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.plan-box h2 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.plan-box ul {
    list-style-type: none;
    text-align: start;
    padding: 0;
    width: 80%;
    margin-bottom: 1rem;
    flex-grow: 1;
    width: 90%;
    align-self: center;
}

.plan-footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: auto;
}

.plan-footer h3 {
    margin-bottom: 1rem;
    font-size: 1.2rem;
    font-weight: bold;
}

.plan-box button {
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.free-plan {
    border: 2px solid #007bff;
}

.monthly-plan {
    border: 2px solid #8a2be2;
}

.annual-plan {
    border: 2px solid #d415cb;
}

.free-plan-btn {
    background-color: #007bff;
}

.monthly-plan-btn {
    background-color: #8a2be2;
}

.annual-plan-btn {
    background-color: #d415cb;
}

.plan-box button:hover {
    opacity: 0.9;
}
</style>
