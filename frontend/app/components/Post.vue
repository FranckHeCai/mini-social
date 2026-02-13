<script setup lang="ts">
import { API_ROUTES } from '~/api/apiRoutes';
import { fetch_with_token } from '~/api/fetch_with_token';
import { fetchPosts } from '~/api/posts/fetchPosts';
import { usePostStore } from '~/store/postStore';
import { useUserStore } from '~/store/userStore';
import type { apiGenericResponse, ID, Post, User } from '~/type';

const props = defineProps<{
  pp?: string
  user?: User
  content?: string
  files?: File
  posted?: Date
  post: Post
}>()

const username = ref('INKU')
const tag = ref<`@${string}`>('@Inku_fr')
const posted = ref('5h')

const showPostPopup = ref(false)
const popupRef = useTemplateRef('popupRef')

const userStore = useUserStore()
const { user } = storeToRefs(userStore)
const postStore = usePostStore()

const handleDeletePost = async () =>{
  try {
    const response: apiGenericResponse = await fetch_with_token(`${API_ROUTES.posts}/${props.post.id}`, {
      method: 'DELETE'
    })

    const removedPost = postStore.posts.filter((post: Post) => post.id !== props.post.id)
    postStore.setPosts(removedPost)
    console.log(response.message)
  } catch (error) {
    console.error(error)
  }
}

onClickOutside(popupRef, ()=>{
  showPostPopup.value = false
})
</script>

<template>
  <div class="relative p-3 flex gap-2 border-b border-white/20">
    <div>
      <div class="size-11 rounded-full overflow-hidden">
          <img class="h-full w-full" src="../assets/feitan.jpg" alt="profile-picture">
      </div>
    </div>
    <div class="">
      <div class="flex justify-between items-center">
        <div class="flex flex-wrap gap-1 items-center">
          <h3 class="font-medium">{{ props.post.user.username }}</h3>
          <div class="size-5">
            <img class="h-full w-full" src="../assets/x_verified_badge.svg" alt="">
          </div>
          <p class="text-secondary">
            <span v-if="props.post.user.tag">{{ props.post.user.tag }}</span>
            <span v-else>@{{ props.post.user.username }}</span>
            · {{ posted }}
          </p>
        </div>
        <button v-if="props.post.user.id === user?.id" @click="()=>{showPostPopup = true}" class="size-7 text-secondary rounded-full p-1 hover:bg-blue-500/30 hover:text-blue-400 transition-all duration-200 cursor-pointer">
          <IconsDots />
        </button>
      </div>
      <p>
        {{ props.post.content }}
      </p>
      <div class="mt-3">
        <div class="rounded-lg overflow-hidden sm:max-w-2/3">
          <img src="../assets/mock_img.jfif" alt="">
        </div>
      </div>
      <div class="mt-3 text-secondary flex justify-between">
        <button class="flex items-center gap-1 hover:text-blue-400 hover:bg-blue-500/10 rounded-full transition-all duration-200">
          <div class="size-5">
            <IconsComment />
          </div>
          8
        </button>
        <button class="flex items-center gap-1 hover:text-emerald-500 hover:bg-emerald-500/10 rounded-full transition-all duration-200">
          <div class="size-5">
            <IconsRepost />
          </div>
          8
        </button>
        <button class="flex items-center gap-1 hover:text-rose-500 hover:bg-rose-500/10 rounded-full transition-all duration-200">
          <div class="size-5">
            <IconsHeartOutline />
          </div>
          8
        </button>


      </div>
    </div>
    <div class="absolute top-3 right-3" ref="popupRef" v-if="showPostPopup">
      <PostPopup @deletePost="handleDeletePost" />
    </div>
  </div>
</template>


<style scoped>

</style>