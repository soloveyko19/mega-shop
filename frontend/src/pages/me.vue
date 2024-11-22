<template>
    <Card>
        <h1 class="title">Your profile</h1>
        <div class="profile" v-if="profile.isLoggedIn">
            <div class="profile__item">
                <div class="profile__title">
                    Id
                </div>
                <div class="profile__value">
                    {{ profile.id }}
                </div>
            </div>
            
            <div class="profile__item">
                <div class="profile__title">
                    Email
                </div>
                <div class="profile__value">
                    {{ profile.email }}
                </div>
            </div>
            
            <div class="profile__item">
                <div class="profile__title">
                    Name
                </div>
                <div class="profile__value">
                    {{ profile.name ? profile.name: 'Not set' }}
                </div>
            </div>
            <div class="profile__item">
                <BaseButton :click="editProfile" :color="'primary'">
                    Edit profile
                </BaseButton>
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
        <div class="modal_window" v-if="showModalWindow">
            <ModalWindow :exit="closeModal">
                <UpdateProfileForm :onSuccess="() => {showModalWindow = false}" :defaultEmail="profile.email" :defaultName="profile.name" />
            </ModalWindow>
        </div>
    </Card>
</template>

<script lang="ts" setup>
import type { requestStatus } from '~/utils/types';
import { useProfileStore } from '~/stores/profile';

const logoutStatus = ref<requestStatus>('idle') 
const profile = useProfileStore()
const router = useRouter()
const showModalWindow = ref<boolean>(false)

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

function editProfile() {
    showModalWindow.value = true;
}

function closeModal() {
    showModalWindow.value = false;
}

</script>

<style scoped>
.profile {
    display: flex;
    flex-direction: column;
}

.profile__item {
    display: flex;
    gap: 20px;
    flex-direction: column;
    border-top: 1px solid rgb(150, 150, 150);
    padding: 10px;
}

.profile__title {
    display: flex;
    align-items: center;
    font-size: 1.1em;
}
</style>