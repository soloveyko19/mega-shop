<template>
    <div class="category"
        @mouseenter="showCategoryList = true"
        @mouseleave="showCategoryList = false"
        @click="showCategoryList ? showCategoryList = false : showCategoryList = true"
    >
        <div class="category__main">
            <div class="category__title">
                Category
            </div> 
            <div class="icon">
                <img :src="downArrowImage">
            </div>
        </div>
        <ul class="category__list" v-if="showCategoryList && categories">
            <li v-for="category in categories" :key="category.id" class="category__item">
                <NuxtLink :to="`/product/category/${category.id}`">
                    <div class="item__wrapper">
                        {{ category.name }}
                    </div>
                </NuxtLink>
            </li>
        </ul>
        <div class="categories__error" v-else-if="showCategoryList && error">
            Error on fetching categories
        </div>
        <div class="categories__loading" v-else-if="showCategoryList">
            <LoadingSpinner />
        </div>
    </div>
</template>

<script setup lang="ts">
import downArrowImage from '@/assets/img/arrow-down.svg'

const config = useRuntimeConfig()
let showCategoryList = useState<boolean>("showCategoryList", () => false)

const { data: categories, error } = useFetch(`${config.public.apiUrlClient}/category`,
    {
        timeout: 10000,
        server: false,
    }
)
</script>

<style scoped>
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

</style>
