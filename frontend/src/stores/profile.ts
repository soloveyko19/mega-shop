import { defineStore } from "pinia";
import type { credentials, profile } from "~/utils/types";


export const useProfileStore = defineStore('profile', {
    state: () => ({
            loaded: false,
            isLoggedIn: false,
            email: '',
            name: '',
            id: -1,
    }),
    actions: {
        async fetchMe() {
            this.loaded = true
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            try {
                const res = await $fetch<profile>(baseAPIUrl + '/me', {
                    timeout: 10000,
                    credentials: 'include',
                })
                this.email = res.email
                this.id = res.id
                this.name = res.name
                this.isLoggedIn = true
            } catch (error) {
                this.isLoggedIn = false
                throw error
            }            
        },
        async updateMe(name: string, email: string) {
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            await $fetch<profile>(baseAPIUrl + '/me', {
                method: 'POST',
                timeout: 10000,
                credentials: 'include',
                body: {
                    email,
                    name
                }
            })
        },
        async login(meProfile: credentials) {
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            await $fetch(baseAPIUrl + '/login', {
                body: meProfile,
                timeout: 10000,
                credentials: 'include',
                method: 'POST',
            })
        },
        async logout() {
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            await $fetch(baseAPIUrl + '/logout', {
                method: 'POST',
                timeout: 10000,
                credentials: 'include'
            })                        
        },
        async register(data: credentials) {
            const config = useRuntimeConfig()
            const baseAPIUrl = config.public.apiUrlClient
            await $fetch(baseAPIUrl + '/register', {
                method: "POST",
                timeout: 10000,
                body: data,
                credentials: 'include'
            })
        }

    }
})