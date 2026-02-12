import { defineStore } from "pinia";

export const useAuthStore = defineStore('auth-store', ()=>{
  const token = useCookie('auth-token', { default: () => '' })
  const loggedIn = computed(() => !!token.value)
  const setToken = (newToken: string) => {
    token.value = newToken
  }
  const clearToken = () => {
    token.value = ''
  }
  return { token, loggedIn, setToken, clearToken }
})