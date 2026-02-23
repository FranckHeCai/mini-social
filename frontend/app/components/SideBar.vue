<script setup lang="ts">
import { onClickOutside } from '@vueuse/core';
import { createPost } from '~/api/posts/createPost';
import { fetchPosts } from '~/api/posts/fetchPosts';
import { useDrawerStore } from '~/store/drawerStore';
import { useUserStore } from '~/store/userStore';


const drawerStore = useDrawerStore()
const {showPopup, showPostPopup} = storeToRefs(drawerStore)
const popupRef = useTemplateRef('popupRef')

const userStore = useUserStore()
const { user } = storeToRefs(userStore)

const postText = ref('')
const selectedFile = ref<File|undefined>(undefined)
const imagePreview = computed(()=>{
  if(selectedFile.value?.type.startsWith('image')){
    return URL.createObjectURL(selectedFile.value)
  }
})

const textareaRef = ref<HTMLTextAreaElement | null>(null)

const handleCreatePostButton = () =>{
  drawerStore.togglePostPopup()
}

const handleTogglePopup = () => {
  drawerStore.togglePopup()
}

onClickOutside(popupRef, (event) => {
  drawerStore.closePopup()
})


const handleCreatePost = async () =>{
    try {
    const formData = new FormData()
    formData.append('content', postText.value)

    if(selectedFile.value){
      formData.append('file', selectedFile.value)
    }
    await createPost(formData)
    postText.value = ''
    selectedFile.value = undefined
    drawerStore.closePostPopup()
    fetchPosts()

  } catch (error) {
    console.error(error)
  }
}

onClickOutside(popupRef, ()=>{
  drawerStore.closePostPopup()
})


const autoResize = () => {
  const el = textareaRef.value
  if (!el) return

  el.style.height = 'auto'          // reset
  el.style.height = el.scrollHeight + 'px' // grow
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

watch(postText, async () => {
  await nextTick()
  autoResize()
})

</script>
<template>
      <!-- Sidebar -->
    <aside class="relative max-w-3xs sm:w-full p-3 flex flex-col justify-between">
      <nav class="flex flex-col gap-3 items-center sm:items-start">
        <NuxtLink
          to="/home"
          class="flex items-center gap-3 p-2 sm:pr-10"
        >
          <img class="size-7" src="../assets/x_logo.svg" alt="x_logo">
        </NuxtLink>
        <NuxtLink
          to="/home"
          v-slot="{isActive}"
        >
          <div 
            class="flex items-center gap-3 p-2 sm:pr-10 hover:bg-white/15 transition-colors duration-100 rounded-full text-xl"
            :class="[
              isActive ? 'font-bold' : 'font-light'
            ]"
          >
            <IconsHome v-if="isActive" class="size-8" />
            <IconsHomeOutline v-else class="size-8" />
            <span class="hidden sm:inline">Home</span>
          </div>
        </NuxtLink>
        <NuxtLink
          to="/profile"
          v-slot="{isActive}"
        >
          <div
            class="flex items-center gap-3 p-2 sm:pr-10 hover:bg-white/15 transition-colors duration-100 rounded-full text-xl"
            :class="[
              isActive ? 'font-bold' : 'font-light'
            ]"
          >
            <IconsProfile v-if="isActive" class="size-8" />
            <IconsProfileOutline v-else class="size-8" />
            <span class="hidden sm:inline">Profile</span>
          </div>
        </NuxtLink>

        <!-- CREATE POST BUTTON -->
        <button @click="handleCreatePostButton" class="bg-stone-50 p-3 sm:py-3 sm:px-0 sm:w-full rounded-full text-black cursor-pointer hover:opacity-80 transition-all duration-200">
          <IconsCreate class="size-6 sm:hidden" />
          <p class="text-lg  font-bold hidden sm:inline">Post</p>
        </button>
      </nav>
      
      <SidebarProfileButton v-if="user" @click="handleTogglePopup" :username="user.username"/>
      <div class="absolute bottom-20 left-5" ref="popupRef" v-if="showPopup">
        <LogoutPopup />
      </div>
      
    </aside>
    <ModalBackground v-if="showPostPopup">
      <div ref="popupRef" class="w-full h-dvh sm:h-auto sm:max-w-lg p-5 bg-black rounded-xl">
        <div class="flex justify-between items-center">
          <button class="cursor-pointer" @click="drawerStore.closePostPopup">
            <IconsCross class="hidden sm:block size-5" />
            <IconsLeftArrow class="sm:hidden size-8" />
          </button>
        </div>
        <div class="mt-5 flex flex-col gap-3">
          <div class="flex gap-3 min-h-40">
            <!-- PROFILE PICTURE -->
            <div>
              <div class="size-11 rounded-full overflow-hidden">
                <img class="h-full w-full" src="../assets/feitan.jpg" alt="profile-picture">
              </div>
            </div>

            <!-- INPUT TEXT -->
            <div class="flex-1 flex-col">
              <textarea ref="textareaRef" v-model="postText" class="w-full flex-1 text-lg resize-none sm:text-xl font-light focus:outline-0" type="text" placeholder="What's happening?">
              </textarea>
              <div v-if="imagePreview && selectedFile" class="relative">
                <img class="rounded-2xl" :src="imagePreview" :alt="selectedFile.name">
                <button @click="removeFile" class="absolute top-1 right-1 size-7.5 p-1.5 bg-black/70 rounded-full cursor-pointer backdrop-blur-md">
                  <IconsCross />
                </button>
              </div>
            </div>
          </div>
          <div class="border-b border-white/20">

          </div>
          <div class="flex">
            <div class="flex-1">
              <label for="file" >
                <IconsMedia class="size-9 p-2 text-blue-400 hover:bg-blue-400/20 transition-all duration-200 rounded-full" />
              </label>
              <input @change="handleFileSelect" hidden id="file" type="file">
            </div>
            <button @click="handleCreatePost" :disabled="postText.length===0" class="hidden sm:block px-4 py-1 rounded-full bg-stone-50 text-black font-bold cursor-pointer disabled:opacity-50 transition-all duration-150">Post</button>
          </div>
        </div>
      </div>
    </ModalBackground>
</template>


<style scoped>

</style>