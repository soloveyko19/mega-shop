<template>
    <div class="page">
        <Card>
            <h1 class="title">{{ category }}</h1>
            <div class="products" v-if="products">
                <ProductList :products="products" />
            </div>
            <div class="product__error" v-else-if="error">
                Error
                <Button @click="clear(); refresh()">Try again</Button>
            </div>
            <div class="products__loading" v-else>
                <LoadingSpinner />
            </div>
        </Card> 
    </div>
</template>

<script setup>
const { category } = useRoute().params
const url = `https://fakestoreapi.com/products/category/` + category
const { data: products, error, refresh, clear } = useFetch(url, {
    timeout: 10000
})
</script>

<style scoped>
.page {
    display: flex;
    flex-direction: column;
    gap: 30px;
}

.title {
    text-transform: capitalize;
}

.products__loading {
    display: flex;
    justify-content: center;
}
</style>