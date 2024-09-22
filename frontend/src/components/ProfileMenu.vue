<template>
    <div class="profile__box">
        <div class="profile__name" v-if="profile.loaded && profile.isLoggedIn">
            <NuxtLink to="/me">
                <div class="profile__wrapper">
                    {{ profile.username }}
                </div>
            </NuxtLink>
        </div>
        <div class="login" v-else>
            <NuxtLink to="/login">
                <div class="profile__wrapper">
                    Log in
                </div>
            </NuxtLink>
        </div>
    </div>
</template>

<script setup lang="ts">
import { useProfileStore } from '~/stores/profile';
const profile = useProfileStore()
onMounted(() => {
    profile.fetchMe()
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

a {
    color: rgb(200, 200, 200);
}

.profile__wrapper {
    padding: 8px 10px;
}
</style>