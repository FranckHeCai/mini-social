import { useAuthStore } from "~/store/authStore"
import { fetch_token } from "../fetch_token"


export const Login = async (credentials: {username: string, password: string}) =>{
  const authStore = useAuthStore()
  try {
    const response: string = await fetch_token({...credentials})
    const newToken = response
    authStore.setToken(newToken)

  } catch (error) {
    console.error(error)
  }
}