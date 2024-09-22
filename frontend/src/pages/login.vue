<template>
    <Card>
        <h1 class="title">Login</h1>
        <div class="login_form">
            <div class="login_form__item">
                <input type="text" name="username" class="form__input" placeholder="Username" v-model="formData.username" maxlength="100">
            </div>
            <div class="login_form__item">
                <input type="password" name="password" class="form__input" placeholder="Password" v-model="formData.password" maxlength="100">
            </div>
            <div class="login_form__item" v-if="status == 'error'">
                {{ errorMessage }}
            </div>
            <div class="login_form__item">
                <div class="login__button">
                    <BaseButton :click="login">
                        <div class="loading" v-if="status == 'pending'">
                            <LoadingSpinner />
                        </div>
                        <div class="btn__text" v-else>
                            Log in
                        </div>
                    </BaseButton>
                </div>
            </div>
            <div class="login_form__item">
                <div class="no_account_label">
                    Don't have an account? <NuxtLink to="/register">Register now</NuxtLink>
                </div>
            </div>
        </div>
    </Card>
</template>


<script setup lang="ts">
import type { credentials, requestStatus } from '~/utils/types';
import { validatePassword, validateUsername } from '~/utils/validators';

const status = useState<requestStatus>("status", () => 'idle')
const errorMessage = useState<String>("errorMessage", () => "")
const profile = useProfileStore()
const router = useRouter()

const formData: credentials = { username: "", password: "" }

watchEffect(() => {
    if (profile.loaded && profile.isLoggedIn) {
        router.push('/me')
    }
})


async function login() {
    status.value = 'pending'
    try {
        validateUsername(formData.username)
        validatePassword(formData.password)
    } catch (error) {
        if (error instanceof Error) {
            status.value = 'error'
            errorMessage.value = error.message
        }
        return
    }
    try {
        await profile.login(formData)
        await profile.fetchMe()
        router.push('/me')
        status.value = 'idle'
    } catch (error) {
        status.value = 'error'
        errorMessage.value = error.response._data.detail
    }
    
}
</script>


<style scoped>
.title {
    text-align: center
}

.login_form {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 25px;
    max-width: 300px;
    align-self: center;
    background-color: rgb(220, 220, 220);
    padding: 20px;
    border-radius: 5px;
}

.login_form__item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    width: 100%;
}

.form__input {
    background-color: transparent;
    padding: 5px 10px;
    border: none;
    border-bottom: 1px solid rgb(33, 33, 33);
    font-size: 1em;
    width: 100%;
}

.form__input:focus {
    outline: 1px solid rgb(33, 33, 33);
}

.no_account_label {
    font-size: 0.8em;
}

.no_account_label a {
    transition: 0.2s;

}

.no_account_label a:hover {
    color: rgb(0, 164, 5);
}
</style>