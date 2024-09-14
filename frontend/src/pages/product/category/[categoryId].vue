<template>
    <div class="page">
        <Card>
            <h1 class="title" v-if="category">{{ category.name }}</h1>
            <div class="products" v-if="products">
                <ProductList :products="products" />
            </div>
            <div class="product__error" v-else-if="error">
                Error
                <button @click="clear(); refresh()">Try again</button>
            </div>
            <div class="products__loading" v-else>
                <LoadingSpinner />
            </div>
        </Card> 
    </div>
</template>

<script setup>
const config = useRuntimeConfig()
const { categoryId } = useRoute().params
const baseApiUrl = import.meta.server ? config.apiUrlServer: config.public.apiUrlClient

const { data: category } = useFetch(`${baseApiUrl}/category/${categoryId}`)

const { data: products, error, refresh, clear } = useFetch(`${baseApiUrl}/products/category/${categoryId}`, {
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