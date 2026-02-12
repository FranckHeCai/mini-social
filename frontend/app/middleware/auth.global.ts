// import { fetch_user_info } from "~/api/fetch_user_info"
import { useAuthStore } from "~/store/authStore"
import { useUserStore } from "~/store/userStore"

export default defineNuxtRouteMiddleware((to, from) => {
  //AUTHENTICATION MIDDLEWARE

  const authStore = useAuthStore()
  // authStore.clearToken()

  const userStore = useUserStore()
  const { user } = storeToRefs(userStore)

  if(!authStore.loggedIn && to.path !=='/login' && to.path !=='/register'){
    return navigateTo('/login')
  }

  if (authStore.loggedIn && to.path === '/login') {
    return navigateTo('/')
  }

  // if(authStore.loggedIn && !user.value){
  //   fetch_user_info()
  // }
})