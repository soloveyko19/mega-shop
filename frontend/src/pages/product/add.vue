<template>
    <Card>
        <div class="page">
            <h1 class="title">Add new product</h1>
            <div class="product__form">
                <div class="form__item product__title">
                    <input type="text" class="form__input" placeholder="Title" v-model="product.title">
                </div>
                <div class="form__item product__price">
                    <input type="text" class="form__input" placeholder="Price" @input="priceValidate" v-model="product.price">
                </div>
                <div class="form__item product__description">
                    <textarea class="form__textarea" placeholder="Description" v-model="product.description" ></textarea>
                </div>
                <div class="form__item product__image">
                    <input type="url" class="form__input" placeholder="https://your.image/url" v-model="product.image_url">
                </div>
                <div class="form__item product__category">
                    <CategoryList :title="selectedCategory ? selectedCategory.name : ''" :click="(category: category) => { selectCategory(category) }" :color="'black'" />
                </div>
                <div class="form__item error" v-if="submitStatus == 'error'">
                    {{ submitError }}
                </div>
                <div class="form__item">
                    <BaseButton :click="submitForm">
                        <div class="submit_button__wrapper">
                            <div class="wrapper__loading" v-if="submitStatus == 'pending'">
                                <LoadingSpinner />
                            </div>
                            <div class="wrapper__idle" v-else>
                                Submit
                            </div>
                        </div>
                    </BaseButton>
                </div>
            </div>
        </div>
    </Card>
</template>


<script setup lang="ts">
import type { category, requestStatus, product } from '~/utils/types';
import { validateProduct } from '~/utils/validators'

const product = reactive<product>({title: "", description: "", price: 0, category_id: 0, image_url: ''})
const config = useRuntimeConfig()
const submitStatus = useState<requestStatus>('submitRequestStatus', () => 'idle')
const submitError = useState<string>('submitRequestError', () => '')
const router = useRouter()
const profile = useProfileStore()
const selectedCategory = ref<category | null>(null)

const baseAPIUrl = config.public.apiUrlClient
let prevPriceValue = ''


function selectCategory(category: category) {
    selectedCategory.value = category
    product.category_id = category.id
}

function priceValidate (event: Event) {   
    const regex = /^\d*\.?\d{0,2}$/
    if (!regex.test((event.target as HTMLInputElement).value)) {
        product.price = Number(prevPriceValue)
    }
    prevPriceValue = product.price.toString()
}


function submitForm() {
    try {
        validateProduct(product)
    } catch (error) {
        if (error instanceof Error) {
            submitStatus.value = 'error'
            submitError.value = error.message
        }
        return
    }
    $fetch('/products', {
        baseURL: baseAPIUrl,
        method: "POST",
        credentials: "include",
        timeout: 10000,
        body: product,
        onRequest() {
            submitStatus.value = 'pending'
        },
        onRequestError({ error }) {
            submitStatus.value = 'error'
            submitError.value = error.message
        },
        onResponse({response}) {
            const created_product = response._data
            submitStatus.value = 'idle'
            router.push(`/product/${created_product.id}`)
        },
        onResponseError({response}) {
            submitStatus.value = 'error',
            submitError.value = response._data.detail
        }
    })
}

watchEffect(() => {
    if (profile.loaded && !profile.isLoggedIn) {
        router.push('/login')
    }
})
</script>


<style scoped>
.page {
    display: flex;
    flex-direction: column;
    gap: 30px;
    align-items: center;
}

.product__form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 20px;
    background-color: rgb(220, 220, 220);
    border-radius: 5px;
    max-width: 500px;
    width: 100%;
}

.form__input,
.form__textarea {
    background-color: rgb(240, 240, 240);
    border: 1px solid rgb(33, 33, 33);
    border-radius: 5px;
    transition: .2s;
    font-size: 1em;
    padding: 5px 10px;
    outline: none;
    width: 100%;
}

.form__textarea {
    resize: none;
    min-height: 100px;
}

.form__input:focus,
.form__textarea:focus {
    border: 1px solid rgb(72, 255, 100);
}

.product__category {
    background-color: rgb(240, 240, 240);
    border: 1px solid rgb(33, 33, 33);
    border-radius: 5px;
    width: 100%;
}

.error {
    color: rgb(200, 33, 33);
}
</style>
