import { defineStore } from "pinia";
import type { User } from "~/type";

export const useUserStore = defineStore('user-store', ()=>{
  const loading = ref(false)
  const user = ref<User | null>(null)
  const setUser = (newUser: User) => {
    user.value = newUser
  }

  const clearUser = () =>{
    user.value = null
  }

  return { user, setUser, clearUser, loading }
})