<template> 
    <LoadingSpinner />
    <div class="error" v-if="error">{{ error }}</div>
</template>

<script setup lang="ts">
const route = useRoute()
const config = useRuntimeConfig()

const error = route.query.error
const code = route.query.code

if (import.meta.client && code) {
    const response = await $fetch<{ result: string }>(
        config.public.apiUrlClient + `/login/google?code=${code}`,
        {
            timeout: 10000,
            credentials: 'include',
        }
    )
    if (response.result == 'success') {
        navigateTo('/me')
    }
}


</script>