// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite"
export default defineNuxtConfig({
  app: {
    head:{
      title: 'mini-social',
      meta:[
        {
          name: 'Description',
          content: 'Nuxt project for a mini-social media'
        }
      ]
      
    }
  },
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  alias: {
    assets: '/<rootDir>/assets'
  },
  css:['./main.css'],
  modules:['@pinia/nuxt'],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  ssr: false
})
