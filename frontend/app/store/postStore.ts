import { defineStore } from "pinia";
import type { Posts } from "~/type";

export const usePostStore = defineStore('post-store', ()=>{
  const posts = ref<Posts>([])
  const selectedFile = ref<File|undefined>(undefined)
  const imagePreview = computed(()=>{
    if(selectedFile.value?.type.startsWith('image')){
      return URL.createObjectURL(selectedFile.value)
    }
  })
  
  const setPosts = (newPosts: Posts) => {
    posts.value = newPosts
  }

  const setSelectedFile = (file: File | undefined) => {
    selectedFile.value = file
  }

  const removeFile = () =>{
    selectedFile.value = undefined
  }
  return { posts, setPosts, selectedFile, imagePreview, setSelectedFile, removeFile }
})