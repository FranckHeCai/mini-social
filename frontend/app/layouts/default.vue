<script setup lang="ts">
import { fetch_user_info } from '~/api/fetch_user_info';
import { createPost } from '~/api/posts/createPost';
import { fetchPosts } from '~/api/posts/fetchPosts';
import { useAuthStore } from '~/store/authStore';
import { useDrawerStore } from '~/store/drawerStore';
import { useUserStore } from '~/store/userStore';


const authStore = useAuthStore()
const userStore = useUserStore()
const drawerStore = useDrawerStore()
const { showPostPopup } = storeToRefs(drawerStore)

const postText = ref('')
const selectedFile = ref(null)
const popupRef = useTemplateRef('popupRef')

const textareaRef = ref<HTMLTextAreaElement | null>(null)

const handleCreatePost = async () =>{
    try {
    const formData = new FormData()
    formData.append('content', postText.value)

    if(selectedFile.value){
      formData.append('file', selectedFile.value)
    }
    await createPost(formData)
    postText.value = ''
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

watch(postText, async () => {
  await nextTick()
  autoResize()
})

onMounted(()=>{
  if(authStore.loggedIn && !userStore.user){
    fetch_user_info()
  }
})

</script>

<template>
  <div class="flex justify-end min-h-screen bg-black text-primary">
    <SideBar />

    <!-- Main Content -->
    <main class="max-w-6xl w-full h-screen overflow-y-auto border-x border-white/20">
      <slot></slot>
    </main>
    <ModalBackground v-if="showPostPopup">
      <div ref="popupRef" class="w-full h-dvh sm:h-auto sm:max-w-lg p-5 bg-black rounded-xl">
        <div class="flex justify-between items-center">
          <button class="cursor-pointer" @click="drawerStore.closePostPopup">
            <IconsCross class="hidden sm:block size-5" />
            <IconsLeftArrow class="sm:hidden size-8" />
          </button>
          <button @click="handleCreatePost" :disabled="postText.length===0" class="sm:hidden px-4 py-1 rounded-full bg-stone-50 text-black font-bold disabled:opacity-50 transition-all duration-150">Post</button>
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
            <textarea ref="textareaRef" v-model="postText" class="flex-1 text-lg resize-none sm:text-xl font-light focus:outline-0" type="text" placeholder="What's happening?"></textarea>
          </div>
          <div class="border-b border-white/20">

          </div>
          <div class="flex">
            <div class="flex-1">
            </div>
            <button @click="handleCreatePost" :disabled="postText.length===0" class="hidden sm:block px-4 py-1 rounded-full bg-stone-50 text-black font-bold disabled:opacity-50 transition-all duration-150">Post</button>
          </div>
        </div>
      </div>
    </ModalBackground>
  </div>
</template>

<style scoped>
::-webkit-scrollbar {
  width: 8px;
}

/* Track */
::-webkit-scrollbar-track {
  background: oklch(37.3% 0.034 259.733);
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: oklch(55.1% 0.027 264.364);
  border-radius: 8px;
}

</style>