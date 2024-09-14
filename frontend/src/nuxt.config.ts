// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxt/image'],
  css: [
    './assets/css/global.css'
  ],
  runtimeConfig: {
    apiUrlServer: 'http://backend:5000/api',
    public: {
      apiUrlClient: process.env.NUXT_PUBLIC_API_URL_CLIENT
    }
  },
  nitro: {
    preset: "node-server",
  },
  ssr: true,
})