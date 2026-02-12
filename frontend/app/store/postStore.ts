import { defineStore } from "pinia";
import type { Posts } from "~/type";

export const usePostStore = defineStore('post-store', ()=>{
  const posts = ref<Posts>([])
  const setPosts = (newPosts: Posts) => {
    posts.value = newPosts
  }

  return { posts, setPosts }
})