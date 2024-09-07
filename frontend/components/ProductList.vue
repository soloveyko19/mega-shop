<template>
    <ul class="product__list">
        <li v-for="product in products" :key="product.id" class="product__item">
            <ProductItem :product="product" />
        </li>
    </ul>
</template>

<script setup>
const { products } = defineProps(["products"])
</script>


<style scoped>
.product__list {
    --gap: 20px;
    --offsets: 2;
}

@media (max-width: 700px) {
    .product__list {
        --offsets: 1;
    }
}

@media (max-width: 400px) {
    .product__list {
        --offsets: 0
    }
}

.product__list {
    list-style: none;
    display: flex;
    flex-wrap: wrap;
    gap: var(--gap);
}

.product__item {
    width: calc((100% - (var(--gap) * var(--offsets))) / (var(--offsets) + 1));
    background-color: rgb(230, 230, 230);
    border-radius: 5px;
    transition: 0.2s;
}


</style>

