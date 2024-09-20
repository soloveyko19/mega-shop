<template>
    <button class="btn" @click="click && click()">
        <slot />
    </button>
</template>


<script setup lang="ts">
const { click } = defineProps({
    click: {
        type: Function,
    }
})
</script>


<style scoped>
.btn {
    color: black;
    padding: 10px 15px;
    background-color: rgb(230, 230, 230);
    border-radius: 10px;
    font-size: 1em;
    width: fit-content;
    border: none;
    border: 1px solid black;
    cursor: pointer;
    transition: 0.2s;
}

.btn:hover {
    background-color: rgb(210, 210, 210);
}
</style>