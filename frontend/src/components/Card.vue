<template>
    <div class="card">
        <slot />
    </div>
</template>


<style scoped>
.card {
    display: flex;
    flex-direction: column;
    gap: 20px;
}
</style>