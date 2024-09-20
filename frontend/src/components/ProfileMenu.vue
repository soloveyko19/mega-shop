<template>
    <div class="profile__box">
        <div class="login" v-if="!me">
            <NuxtLink to="/login">
                <div class="profile__wrapper">
                    Log in
                </div>
            </NuxtLink>
        </div>
        <div class="profile__name" v-else>
            <div class="profile__wrapper">
                {{ me.username }}
            </div>
        </div>
    </div>
</template>

<script setup>
const config = useRuntimeConfig()
const { data: me } = useFetch(`${config.public.apiUrlClient}/me`, {
    timeout: 10000,
    server: false,
    credentials: "include"
})
</script>

<style scoped>
.profile__box {
    border-radius: 5px;
    transition: 0.2s;
    cursor: default;
}

.profile__box:hover {
    background-color: #fff2;
}

.login a {
    color: rgb(200, 200, 200);
}

.profile__wrapper {
    padding: 8px 10px;
}
</style>