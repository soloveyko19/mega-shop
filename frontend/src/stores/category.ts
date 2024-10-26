import { defineStore } from "pinia";
import { type categoryList } from "~/utils/types";


export const useCategoryStore = defineStore('categoryStore', {
    state: () => ({
        data: Array(),
        fetched: false
    }),
    actions: {
        async fetchCategories() {
            this.fetched = true
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            try {
                const res = await $fetch<categoryList>(baseAPIUrl + '/category', {
                    timeout: 10000,
                })
                this.data = res
            } catch (error) {
                this.data = []
                throw error
            }
        }
    }
})