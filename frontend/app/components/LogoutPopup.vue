<script setup lang="ts">
import { API_ROUTES } from '~/api/apiRoutes';
import { Logout } from '~/api/auth/logout';
import { fetch_with_token } from '~/api/fetch_with_token';
import { useAuthStore } from '~/store/authStore';
import { useUserStore } from '~/store/userStore';

const userStore = useUserStore()
const {user} = storeToRefs(userStore)

const formatUsername = (username: string) =>{
  const split = username.split(' ')
  const newUsername = split.join('_')
  return newUsername
}

const handleLogout = () =>{
  Logout()
}
</script>

<template>
  <!-- <div class="absolute bottom-10 left-10 max-w-2xs p-4 rounded-xl shadow shadow-stone-50/50 bg-black font-medium">
    <p>Log out {{ user.username }}</p>
  </div> -->
  <div class=""> 
    <div class=" border border-stone-400/50 rounded-xl bg-black py-3 font-medium relative z-20">
      <button @click="handleLogout" class="w-full px-5 py-2 hover:bg-white/10 transition-all duration-200">Log out <span class="text-sm text-secondary">@{{ user?.username ? formatUsername(user.username) : '' }}</span></button>
    </div>
    <div class="absolute inset-1 rounded-xl blur-md bg-stone-50/40 z-10"></div>
  </div>
</template>


<style scoped>

</style>