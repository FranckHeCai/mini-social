export default defineNuxtRouteMiddleware((to, from) => {

  window.scrollTo({
    top: 0,
    behavior: "smooth"
  })
  
})