import { defineStore } from "pinia";
import type { Posts, User } from "~/type";

export const useUserStore = defineStore('user-store', ()=>{
  const loading = ref(false)
  const user = ref<User | null>(null)
  const userPosts = ref<Posts>([])

  const setUser = (newUser: User) => {
    user.value = newUser
  }
  const clearUser = () =>{
    user.value = null
  }
  const setUserPosts = (posts: Posts) =>{
    userPosts.value = posts
  }

  return { user, setUser, clearUser, userPosts, setUserPosts, loading }
})