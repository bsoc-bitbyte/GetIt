// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindTypography from '@tailwindcss/typography'

export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr: true,
  plugins: ["~/plugins/fetch.js"],
  modules: [
    "@nuxtjs/tailwindcss",
    "@pinia/nuxt",
    "@pinia-plugin-persistedstate/nuxt",
  ],
  tailwindcss: {
    config: {
      plugins: [tailwindTypography]
    }
  },
  runtimeConfig: {
    public: {
      API_BASE_URL: process.env.NUXT_API_BASE_URL || "http://localhost:8000",
    },
  },
});

