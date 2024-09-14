<template>
    <div class="categories">
        <ul v-if="categories">
            <li  v-for="category in categories" :key="category" >
                <NuxtLink :to="`/products/category/${category}`">
                    {{ category }}
                </NuxtLink>        
            </li>
        </ul>
        <div class="categories__error" v-else-if="error">
            Error on fetching categories
            <button @click="clear(); refresh()">
                Try again
            </button>
        </div>
        <div class="categories__loading" v-else>
            <LoadingSpinner /> 
        </div>
    </div>
</template>

<script lang="ts" setup>
const config = useRuntimeConfig()

const { data: categories, error, clear, refresh } = useFetch(`${config.public.apiUrl}/products/categories`, {
    timeout: 10000
})
</script>

<style scoped>
</style>