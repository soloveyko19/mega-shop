<template>
    <Card>
        <h1 class="title">Your profile</h1>
        <div class="profile" v-if="profile.isLoggedIn">
            <div class="profile__item">
                <div class="profile__title">
                    <b>Email</b>
                </div>
                <div class="profile__value">
                    {{ profile.email }}
                </div>
            </div>
            <div class="profile__item">
                <div class="profile__title">
                    <b>Id</b>
                </div>
                <div class="profile__value">
                    {{ profile.id }}
                </div>
            </div>
            <div class="profile__item">
                <div class="profile__title">
                    <b>Name</b>
                </div>
                <div class="profile__value">
                    {{ profile.name ? profile.name: 'Not set' }}
                </div>
            </div>
            <div class="profile__item">
                <BaseButton :click="logout" :color="'red'">
                    <div class="logout_wrapper">
                        <div class="logout__idle" v-if="logoutStatus == 'idle'">
                            Logout
                        </div>
                        <div class="logout__pending" v-else-if="logoutStatus == 'pending'">
                            <LoadingSpinner />
                        </div>
                        <div class="logout__error" v-else-if="logoutStatus == 'error'">
                            Error
                        </div>
                    </div>
                </BaseButton>
            </div>
        </div>
        <div class="profile__loading" v-else>
            <LoadingSpinner />
        </div>
    </Card>
</template>

<script lang="ts" setup>
import type { requestStatus } from '~/utils/types';
import { useProfileStore } from '~/stores/profile';

const logoutStatus = useState<requestStatus>('logoutRequestStatus', () => 'idle') 
const profile = useProfileStore()
const router = useRouter()

watchEffect(() => {
    if (profile.loaded && !profile.isLoggedIn) {
        router.push("/login")
    }
})

async function logout() {
    logoutStatus.value = 'pending'
    try {
        await profile.logout()    
        await profile.fetchMe()
    } catch (error) {
        logoutStatus.value = 'error'
    }
    navigateTo('/login')
    logoutStatus.value = 'idle'
}

</script>

<style scoped>
.profile {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.profile__item {
    display: flex;
    gap: 20px;
}

.profile__title {
    display: flex;
    align-items: center;
}

.profile__title {
    display: flex;
    align-items: center;
}
</style>