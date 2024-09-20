<template>
    <header class="header">
        <nav class="header__nav">
            <div class="nav__brand_name">
                <NuxtLink to="/">
                    <div class="brand_name__wrapper">
                        Mega
                    </div>
                </NuxtLink>
            </div>
            <ul class="nav__list">
                <li class="nav__item">
                    <NuxtLink to="/">
                        <div class="item__wrapper">
                            Home
                        </div>
                    </NuxtLink>
                </li>
                <li class="nav__item">
                    <NuxtLink to="/product">
                        <div class="item__wrapper">
                            Products
                        </div>
                    </NuxtLink>
                </li>
                <li class="nav__item">
                    <CategoryList />
                </li>
            </ul>
            <div class="nav__profile">
                <ProfileMenu />
            </div>
        </nav>
    </header>
</template>

<script setup lang="ts">
</script>

<style scoped>
.header {
    width: 100%;
    background-color: rgb(26, 26, 26);
    color: rgb(200, 200, 200);
    padding: 20px 30px;
    display: flex;
    justify-content: space-between;
}

a {
    color: rgb(200, 200, 200);
}

.header__nav {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    column-gap: 50px;
    row-gap: 10px;
    width: 100%;
}

.nav__brand_name {
    font-size: 3em;
    text-decoration: none;
}

.nav__list {
    list-style: none;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    padding: 0;
    margin: 0;
    column-gap: 20px;
    row-gap: 10px;
}

.nav__item {
    transition: 0.2s;
    border-radius: 5px;
}

.nav__item .router-link-exact-active {
    color: rgb(0, 200, 7);
}

.nav__item:hover {
    background-color: #fff2;
}

.item__wrapper {
    padding: 8px 10px;
}

.header__theme {
    display: flex;
    align-items: center;
}

.nav__profile {
    margin-left: auto;
}

</style>