<script setup lang="ts">
import { API_ROUTES } from '~/api/apiRoutes'
import { fetchPosts } from '~/api/posts/fetchPosts'
import { usePostStore } from '~/store/postStore'

import type { apiGenericResponse } from '~/type'

const postStore = usePostStore()
const {posts} = storeToRefs(postStore)

const loading = ref(false)

const checkHealth = async () => {
  const response: apiGenericResponse = await $fetch(API_ROUTES.base)
  console.log(response.message)
}

const getPosts = async () => {
  try {
    loading.value = true
    await fetchPosts()

    loading.value =false
  } catch (error) {
    console.error(error)
  }
}

onMounted(async () => {
  getPosts()

})

</script>
<template>
  <div class="relative max-w-150 border-r border-white/20 flex flex-col">
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