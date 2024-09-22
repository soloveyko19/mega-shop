<template>
    <button class="btn" :class="'btn_' + (color ? color: 'primary')" @click="click && click()">
        <slot />
    </button>
</template>


<script setup lang="ts">
interface props {
    click: Function
    color?: 'primary' | 'red'
}

const { click, color } = defineProps<props>()
</script>


<style scoped>
.btn {
    padding: 10px 15px;
    border-radius: 10px;
    font-size: 1em;
    width: fit-content;
    border: none;
    cursor: pointer;
    transition: 0.2s;
}

.btn_primary {
    color: black;
    background-color: rgb(230, 230, 230);
    border: 1px solid black;
}

.btn_red {
    color: rgb(33, 33, 33);
    background-color: rgb(255, 220, 220);
    border: 1px solid red;
}

.btn_primary:hover {
    background-color: rgb(210, 210, 210);
}

.btn_red:hover {
    background-color: rgb(255, 200, 200);
}
</style>