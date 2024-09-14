<template>
    <div class="loading-spinner">
      <div class="spinner" />
    </div>
  </template>

<style scoped>
@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    100% {
        transform: rotate(360deg);
    }
}

.loading-spinner {
    display: flex;
    width: fit-content;
    height: fit-content;
    justify-content: center;
    align-items: center;
}

.spinner {
    width: 30px;
    height: 30px;
    border: 5px solid rgba(0, 0, 0, 0.2);
    border-top-color: #000000;
    border-radius: 50%;
    animation: spin 2s infinite linear;
}
</style>