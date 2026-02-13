<script setup lang="ts">
import { fetch_user_info } from '~/api/fetch_user_info';
import { useAuthStore } from '~/store/authStore';
import { useUserStore } from '~/store/userStore';


const authStore = useAuthStore()
const userStore = useUserStore()

const postText = ref('')
const showPopup = ref(true)
const popupRef = useTemplateRef('popupRef')

const handleCreatePost = async () =>{

}

const closePopup = () =>{
  showPopup.value = false
}

onClickOutside(popupRef, ()=>{
  closePopup()
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
    <ModalBackground v-if="showPopup">
      <div ref="popupRef" class="w-full max-w-md p-4 bg-black rounded-xl">
        <button @click="closePopup">
          <IconsCross class="size-5" />
        </button>
        <div class="mt-5 flex flex-col gap-3">
          <div class="flex gap-3 h-40">
            <!-- PROFILE PICTURE -->
            <div>
              <div class="size-11 rounded-full overflow-hidden">
                <img class="h-full w-full" src="../assets/feitan.jpg" alt="profile-picture">
              </div>
            </div>

            <!-- INPUT TEXT -->
            <textarea v-model="postText" class="flex-1 text-lg resize-none sm:text-xl font-light focus:outline-0" type="text" placeholder="What's happening?"></textarea>
          </div>
          <div class="border-b border-white/20">

          </div>
          <div class="flex">
            <div class="flex-1">
            </div>
            <button @click="handleCreatePost" :disabled="postText.length===0" class="px-4 py-1 rounded-full bg-stone-50 text-black font-bold disabled:opacity-50 transition-all duration-150">Post</button>
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