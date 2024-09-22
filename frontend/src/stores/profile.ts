import { defineStore } from "pinia";
import type { credentials, profile } from "~/utils/types";


export const useProfileStore = defineStore('profile', {
    state: () => ({
            loaded: false,
            isLoggedIn: false,
            username: '',
            id: -1,
    }),
    actions: {
        async fetchMe() {
            this.loaded = true
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            try {
                const res = await $fetch<profile>('/me', {
                    timeout: 10000,
                    credentials: 'include',
                    baseURL: baseAPIUrl,
                })
                this.username = res.username
                this.id = res.id
                this.isLoggedIn = true
            } catch (error) {
                this.isLoggedIn = false
                throw error
            }            
        },
        async login(meProfile: credentials) {
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            await $fetch('/login', {
                body: meProfile,
                timeout: 10000,
                credentials: 'include',
                baseURL: baseAPIUrl,
                method: 'POST',
            })
        },
        async logout() {
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            await $fetch('/logout', {
                method: 'POST',
                timeout: 10000,
                credentials: 'include',
                baseURL: baseAPIUrl
            })                        
        },
        async register(data: credentials) {
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            await $fetch('/register', {
                baseURL: baseAPIUrl,
                method: "POST",
                timeout: 10000,
                body: data,
                credentials: 'include'
            })
        }

    }
})