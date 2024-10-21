// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  compatibilityDate: '2024-04-03',
  devtools: { enabled: true },
  modules: ['@nuxt/image', '@pinia/nuxt'],
  css: [
    './assets/css/global.css'
  ],
  runtimeConfig: {
    apiUrlServer: (process.env.TESTING == "true") ? process.env.NUXT_API_URL_CLIENT : 'http://backend:5000/api',
    public: {
      apiUrlClient: process.env.NUXT_API_URL_CLIENT
    }
  },
  nitro: {
    preset: "node-server",
  },
  ssr: true,
  devServer: {
    https: {
      cert: "../../ssl/cert.pem",
      key: "../../ssl/key.pem"
    }
  }
})

if (process.env.TESTING == "true") {
  process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0'
}