<script setup lang="ts">
import { API_ROUTES } from '~/api/apiRoutes';
import { fetch_with_token } from '~/api/fetch_with_token';
import { createPost } from '~/api/posts/createPost';
import { fetchPosts } from '~/api/posts/fetchPosts';
import type { apiGenericResponse } from '~/type';

const feedType = ref<'fy' | 'following'>('fy')
const postText = ref('')
const selectedFile = ref(null)


const handleCreatePost = async () => {
  try {
    const formData = new FormData()
    formData.append('content', postText.value)

    if(selectedFile.value){
      formData.append('file', selectedFile.value)
    }
    await createPost(formData)
    postText.value = ''
    fetchPosts()
    
  } catch (error) {
    console.error(error)
  }
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
      <input v-model="postText" class="flex-1 text-lg sm:text-xl font-light focus:outline-0" type="text" placeholder="What's happening?">
    </div>
    <div class="flex">
      <div class="flex-1">
      </div>
      <button @click="handleCreatePost" :disabled="postText.length===0" class="px-4 py-1 rounded-full bg-stone-50 text-black font-bold disabled:opacity-50 transition-all duration-150">Post</button>
    </div>
  </div>
</template>

<style scoped>

</style>