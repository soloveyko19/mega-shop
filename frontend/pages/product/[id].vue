<template>
    <div class="product_page">
        <div class="product" v-if="product">
            <ProductDetail :product="product" />
        </div>
        <div class="product__error" v-else-if="error">
            Error
            <button @click="clear(); refresh()">Try again</button>
        </div>
        <div class="product__loading" v-else>
            <LoadingSpinner/>
        </div>
    </div>
</template>

<script setup>
const { id } = useRoute().params
const uri = 'https://fakestoreapi.com/products/' + id
const { data: product, error, clear, refresh } = useFetch(uri)
</script>

<style scoped>
.product_page {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.back {
    background-color: rgb(25, 25, 25);
    width: fit-content;
    border: 1px solid #000;
    border-radius: 10px;
    transition: 0.2s;
}

.back:hover {
    border: solid 1px rgb(0, 200, 7);
}

.back__wrapper {
    width: 100%;
    height: 100%;
    padding: 10px;
}

.product__loading {
    display: flex;
    justify-content: center;
}
</style>

