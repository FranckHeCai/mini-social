import { useAuthStore } from "~/store/authStore"
import { API_ROUTES } from "../apiRoutes"
import { fetch_with_token } from "../fetch_with_token"
import { useUserStore } from "~/store/userStore"

export const Logout = async () =>{
  const authStore = useAuthStore()
  const userStore = useUserStore()
  try {
    await fetch_with_token(`${API_ROUTES.login}/logout`, {
      method: 'POST'
    })
    authStore.clearToken()
    userStore.clearUser()

    console.log('token: ', authStore.token)
    console.log('user: ', userStore.user)
    navigateTo('/login')
  } catch (error) {
    console.error(error)
  }
}