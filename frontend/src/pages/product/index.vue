<template>
    <div class="content">
        <Card>
            <h1 class="title">Products</h1>
            <div class="products" v-if="status == 'success'">
                <ProductList :products="products"/>
            </div>
            <div class="products__loading" v-else-if="status == 'pending' | 'idle'">
                <LoadingSpinner />
            </div>
            <div class="products__error" v-else-if="status == 'error'">
                <div class="error__text">
                    Error on fetching products
                </div>
                <BaseButton :click="() => {clear(); refresh()}">
                    Try again
                </BaseButton>
            </div>
        </Card>
    </div>
</template>


<script setup>
const config = useRuntimeConfig()
const baseApiUrl = import.meta.server ? config.apiUrlServer: config.public.apiUrlClient
const { data: products, status, refresh, clear } = useFetch(`${baseApiUrl}/products`, {
    timeout: 10000,
})
</script>


<style scoped>
.products__loading {
    display: flex;
    justify-content: center;
}

.products__error {
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: center;
}
</style>