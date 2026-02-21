<script setup lang="ts">
import { fetch_user_info } from '~/api/fetch_user_info';
import { createPost } from '~/api/posts/createPost';
import { fetchPosts } from '~/api/posts/fetchPosts';
import { useAuthStore } from '~/store/authStore';
import { useDrawerStore } from '~/store/drawerStore';
import { useUserStore } from '~/store/userStore';


const authStore = useAuthStore()
const userStore = useUserStore()

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