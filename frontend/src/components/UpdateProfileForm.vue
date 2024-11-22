<template>
    <Card>
        <h3 class="title">Update Profile</h3>
        <form class="profile__form" v-on:submit.prevent>
            <div class="form__item">
                <input type="email" placeholder="Email" class="form__input email" v-model="updateFields.email">
            </div>
            <div class="form__item">
                <input type="text" placeholder="Name" class="form__input name" v-model="updateFields.name">
            </div>
            <div class="form__item" v-if="errorMessage">
                <div class="error">
                    {{ errorMessage }}
                </div>
            </div>
            <div class="form__item">
                <BaseButton :click="submit">
                    Update profile
                </BaseButton>
            </div>
        </form>
    </Card>
</template>

<script setup lang="ts">
interface Props {
    onSuccess: () => void,
    defaultName: string,
    defaultEmail: string
}
const { onSuccess, defaultName, defaultEmail } = defineProps<Props>()

import { useProfileStore } from '~/stores/profile';
const profile = useProfileStore()
const updateFields = { name: defaultName, email: defaultEmail}
const errorMessage = ref('')

async function submit() {
    try {
        await profile.updateMe(
            updateFields.name,
            updateFields.email
        )
        await profile.fetchMe()
        onSuccess()
    } catch (error) {
        errorMessage.value = error.detail
    }
}
</script>

<style scoped>
.profile__form {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.form__item {
    display: flex;
    flex-direction: column;
}


.form__input {
    background-color: transparent;
    border: none;
    border-bottom: 1px solid rgb(33, 33, 33);
    font-size: 1em;
    padding: 5px 10px;
}

.form__input:focus {
    outline: 1px solid rgb(33, 33, 33);
}
</style>