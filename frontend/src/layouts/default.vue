<template>
    <div class="layout">
        <BaseHeader/>
        <div class="container">
            <slot />
        </div>
    </div>
</template>

<script setup lang="ts">
</script>

<style>
.layout {
    min-height: 100vh;
    min-width: 100%;
    background: rgb(200, 200, 200);
    color: rgb(33, 33, 33);
}

a {
    text-decoration: none;
    color: rgb(33, 33, 33);
}

.container {
    max-width: 1000px;
    margin: 0 auto;
    padding: 20px;
}
</style>