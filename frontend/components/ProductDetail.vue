<template>
    <div class="product" v-if="product">
        <div class="product__image">
            <div class="image__box">
                <NuxtImg :src="product.image_url" />
            </div>
        </div>
        <div class="product__info">
            <h1 class="info__title">{{ product.title }}</h1>
            <ul class="info__list">
                <li class="info__item">
                    <h3 class="info__subtitle">Price</h3> 
                    <p class="info__plain">
                        {{ product.price }} $
                    </p>
                </li>
                <li class="info__item">
                    <h3 class="info__subtitle">Description</h3>
                    <p class="info__plain">
                        {{ product.description }}
                    </p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script setup>
const { product } = defineProps(["product"])
</script>

<style scoped>
.product {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    width: 100%;
    gap: 20px;
}

.product__info {
    background-color: rgb(230, 230, 230);
    display: flex;
    flex-direction: column;
    padding: 20px;
    border-radius: 10px;
    max-width: 620px;
    gap: 30px;
}

.product__image {
    max-width: 300px;
    max-height: 300px;
    height: fit-content;
    background-color: rgb(255, 255, 255);
    border-radius: 5px;
    overflow: hidden;
    padding: 10px;
}

.image__box img {
    max-width: 280px;
    max-height: 280px;
}

.info__list {
    display: flex;
    flex-direction: column;
    gap: 20px;
    list-style: none;
}

.info__item {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.info__subtitle {
    font-size: 1.1em;
}
</style>