<template>
    <div class="category"
        @mouseenter="showCategoryList = true"
        @mouseleave="showCategoryList = false"
        @click="showCategoryList ? showCategoryList = false : showCategoryList = true"
    >
        <div class="category__main">
            <div class="category__title">
                <div class="title__text" v-if="!title">
                    Category
                </div>
                <div class="title__text" v-else>
                    {{ title }}
                </div>
            </div> 
            <div class="icon">
                <img :src="color ? color == 'white' ? downArrowWhiteImage : downArrowBlackImage : downArrowWhiteImage">
            </div>
        </div>
        <ul class="category__list" v-if="showCategoryList && categoryStore.fetched">
            <li v-for="category in categoryStore.data" :key="category.id" class="category__item">
                <button @click="click && click(category)" class="blank_button">
                    <div class="item__wrapper">
                        {{ category.name }}
                    </div>
                </button>
            </li>
        </ul>
        <div class="categories__error" v-else-if="false">
            Error on fetching categories
        </div>
        <div class="categories__loading" v-else-if="showCategoryList">
            <LoadingSpinner />
        </div>
    </div>
</template>

<script setup lang="ts">
interface props {
    click?: Function,
    title?: string,
    color?: 'white' | 'black'
}

import downArrowWhiteImage from '@/assets/img/arrow-down-white.svg'
import downArrowBlackImage from '@/assets/img/arrow-down-black.svg'

const { click, title } = defineProps<props>()

const showCategoryList = ref<boolean>(false)
const categoryStore = useCategoryStore()

watchEffect(() => {
    if (import.meta.client && !categoryStore.fetched) {
        categoryStore.fetchCategories()
    }
})

</script>

<style scoped>

.title__text {
    text-transform: capitalize;
}

.category {
    padding: 8px 10px;
    position: relative;
}

.category:hover .category__main .icon img {
    transform: rotateZ(180deg);
}

.category__main {
    display: flex;
    gap: 5px
}

.category__title {
    cursor: default;
}

.icon {
    display: flex;
    align-items: center;
}

.icon img {
    width: 16px;
    height: 16px;
    transition: 0.2s;
}

@keyframes appearing {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}

.category__list {
    list-style: none;
    padding: 0;
    margin: 0;
    position: absolute;
    top: 100%;
    display: flex;
    flex-direction: column;
    left: 0;
    width: 100%;
    animation: appearing 0.2s ease-in;
    border: 1px solid rgb(25, 25, 25);
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    overflow: hidden;
}

.category__item {
    background-color: rgb(230, 230, 230);
    transition: 0.2s;
    color: rgb(30, 30, 30);
}


.category__item:hover {
    background-color: rgb(210, 210, 210);
}

.item__wrapper {
    padding: 8px 10px;
    text-transform: capitalize;
}

.categories__error, .categories__loading {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    padding: 8px 10px;
    background-color: rgb(210, 210, 210);
    display: flex;
    justify-content: center;
    color: rgb(33, 33, 33);
}

.blank_button {
    border: none;
    background-color: transparent;
    font-size: 1em;
    cursor: pointer;
    width: 100%;
}

</style>
