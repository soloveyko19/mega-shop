<template>
    <NuxtLink :to="`/product/${product.id}`">        
        <div class="product">
            <div class="product__image">
                <NuxtImg :src="product.image"  />
            </div>
            <div class="product__info">
                <div class="product__title">
                    {{ product.title }}
                </div>  
                <div class="product__price">
                    <b>{{ product.price }} $</b>
                </div>
            </div>
        </div>
    </NuxtLink>
</template>

<script setup>
const { product } = defineProps(["product"])
</script>

<style scoped>
.product {
    min-height: 100%;
    min-width: 100%;
    border-radius: 10px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.product__image {
    padding: 10px;
    background-color: rgb(255, 255, 255);
    display: flex;
    height: 300px;
    align-items: center;
    justify-content: center;
}

.product__image img {
    max-width: 100%;
    max-height: 280px;
    height: fit-content;
}

.product__info {
    padding: 10px;
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.product__title {
    text-align: center;
}

.product__price {
    text-align: center
}
</style>