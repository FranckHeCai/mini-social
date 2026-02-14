<script setup lang="ts">
interface Manga{
  name: string
  author: string
}
import { API_ROUTES } from '~/api/apiRoutes'
import { fetchPosts } from '~/api/posts/fetchPosts'
import { mock_posts } from '~/data/mock_posts'
import { useAuthStore } from '~/store/authStore'
import { useDrawerStore } from '~/store/drawerStore'
import { usePostStore } from '~/store/postStore'
import { useUserStore } from '~/store/userStore'
import type { apiAuthenticationResponse, apiGenericResponse, Posts } from '~/type'

const authStore = useAuthStore()
const {token} = storeToRefs(authStore)

const postStore = usePostStore()
const {posts} = storeToRefs(postStore)

const loading = ref(false)

const checkHealth = async () => {
  const response: apiGenericResponse = await $fetch(API_ROUTES.base)
  console.log(response.message)
}

const handleLogin = async () => {
  try {
    const response: apiAuthenticationResponse = await $fetch(`${API_ROUTES.login}/login`, {
      method: 'POST',
      headers: {
        'Content-type': 'application/x-www-form-urlencoded'
      },
      body: {
        username: 'zuko@avatar.com',
        password: '1234'
      }
    })
    
    const newToken = response.access_token
    authStore.setToken(newToken)
    
  } catch (error) {
    console.error(error)
  }
}

const getPosts = async () => {
  try {
    if (!token.value){
      console.log('token: ', token.value)
    }
    loading.value = true
    await new Promise((resolve) => setTimeout(resolve, 2000))
    await fetchPosts()

    loading.value =false
  } catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  await handleLogin()
  getPosts()
})

</script>
<template>
  <div class="relative max-w-150 border-r border-white/20 flex flex-col">
    <!-- <button @click="handleLogin" class="bg-stone-50 p-3 sm:py-3 sm:px-0 sm:w-full rounded-full text-black font-bold">LOGIN</button>
    <button @click="getPosts" class="bg-stone-50 p-3 sm:py-3 sm:px-0 sm:w-full rounded-full text-black font-bold">get posts</button> -->
    <!-- FEED HEADER -->
    <FeedHeader page="For you" />
    <!-- CREATE POST HEADER -->
    <FeedPostHeader />

    <!-- FEED -->
    <LoadingSpinner v-if="loading" />
    <ul v-else-if="posts.length > 0">
      <Post v-for="post in posts" :key="post.id" :post />
    </ul>
    <div v-else class="flex flex-1 justify-center items-center">
      <p class="text-secondary text-center">No posts available</p>
    </div>
    <!-- POST -->
    <!-- <ul>
      <Post v-for="post in mock_posts" :key="post.user.tag" pp="../assets/feitan.jpg" :user="post.user" :content="post.content" />
    </ul> -->
  </div>
  

</template>