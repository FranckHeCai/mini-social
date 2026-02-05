import { defineStore } from "pinia";

export const useAuthStore = defineStore('auth-store', ()=>{
  const token = useCookie('auth-token', { default: () => null })
  const loggedIn = computed(() => !!token.value)
  const setToken = (newToken: string | null) => {
    token.value = newToken
  }
  const clearToken = () => {
    token.value = null
  }
  return { token, loggedIn, setToken, clearToken }
})