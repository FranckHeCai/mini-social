<script setup lang="ts">
import { API_ROUTES } from '~/api/apiRoutes';
import { fetch_with_token } from '~/api/fetch_with_token';
import { createPost } from '~/api/posts/createPost';
import { fetchPosts } from '~/api/posts/fetchPosts';
import { usePostStore } from '~/store/postStore';
import type { apiGenericResponse } from '~/type';

const feedType = ref<'fy' | 'following'>('fy')
const postText = ref('')

const selectedFile = ref<File|undefined>(undefined)
const imagePreview = computed(()=>{
  if(selectedFile.value?.type.startsWith('image')){
    return URL.createObjectURL(selectedFile.value)
  }
})


const handleCreatePost = async () => {
  try {
    const formData = new FormData()
    formData.append('content', postText.value)

    if(selectedFile.value){
      formData.append('file', selectedFile.value)
    }
    await createPost(formData)
    postText.value = ''
    selectedFile.value = undefined
    fetchPosts()
    
  } catch (error) {
    console.error(error)
  }
}

const handleFileSelect = (e: Event) => {
  const input = e.target as HTMLInputElement
  if (!input.files) return
  // const filesAsArray = Array.from(input?.files || [])
  selectedFile.value = input.files[0]
  console.log('INPUT: ', input.files)
  console.log('SELECTED FILE: ', selectedFile.value)
}

const removeFile = () =>{
  selectedFile.value = undefined
}
</script>

<template>
  <div class="p-4 flex flex-col gap-3 border-b border-white/20">
    <div class="flex gap-3">
      <div>
        <div class="size-11 rounded-full overflow-hidden">
          <img class="h-full w-full" src="../assets/feitan.jpg" alt="profile-picture">
        </div>
      </div>
      <div class="flex flex-col gap-5">
        <input v-model="postText" class="w-full text-lg sm:text-xl font-light focus:outline-0" type="text" placeholder="What's happening?">
        <div v-if="imagePreview && selectedFile" class="relative">
          <img class="rounded-2xl" :src="imagePreview" :alt="selectedFile.name">
          <button @click="removeFile" class="absolute top-1 right-1 size-7.5 p-1.5 bg-black/70 rounded-full cursor-pointer backdrop-blur-md">
            <IconsCross />
          </button>
        </div>
      </div>
    </div>
    <div class="flex">
      <div class="flex-1">
        <label for="file" >
          <IconsMedia class="size-9 p-2 text-blue-400 hover:bg-blue-400/20 transition-all duration-200 rounded-full" />
        </label>
        <input @change="handleFileSelect" hidden id="file" type="file">
      </div>
      <button @click="handleCreatePost" :disabled="postText.length===0 && !selectedFile" class="px-4 py-1 rounded-full bg-stone-50 text-black font-bold disabled:opacity-50 transition-all duration-150">Post</button>
    </div>
  </div>
</template>

<style scoped>

</style>