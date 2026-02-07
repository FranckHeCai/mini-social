import { defineStore } from "pinia";

export const useUserStore = defineStore('user-store', ()=>{
  const user = ref({
    username: 'Zuko',
    tag: '@zuko_avatar',
    followers: 0,
    following: 0
  })
  const setUser = (newUser: {username: string, tag: string, followers: number, following: number}) => {
    user.value = newUser
  }

  return { user, setUser }
})