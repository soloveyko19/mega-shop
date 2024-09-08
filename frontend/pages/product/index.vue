<template>
    <div class="content">
        <Card>
            <h1 class="title">Products</h1>
            <div class="products" v-if="products">
                <ProductList :products="products"/>
            </div>
            <div class="products__loading" v-else-if="!products && !error">
                <LoadingSpinner />
            </div>
            <div class="products__error" v-else>
                <div class="error__text">
                    Error on fetching products
                </div>
                <button class="error__btn" @click="clear(); refresh()">Try again</button>
            </div>
        </Card>
    </div>
</template>


<script setup>
const config = useRuntimeConfig()

const { data: products, error, refresh, clear } = useFetch(`${config.public.apiUrl}/products`, {
    timeout: 10000
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

.error__btn {
    color: black;
    padding: 10px 15px;
    background-color: rgb(230, 230, 230);
    border-radius: 10px;
    font-size: 1em;
    width: fit-content;
    border: none;
    border: 1px solid black;
    cursor: pointer;
    transition: 0.2s;
}

.error__btn:hover {
    background-color: rgb(210, 210, 210);
}
</style>