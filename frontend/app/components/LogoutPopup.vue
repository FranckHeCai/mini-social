<script setup lang="ts">
import { useUserStore } from '~/store/userStore';

const userStore = useUserStore()
const {user} = userStore
</script>

<template>
  <!-- <div class="absolute bottom-10 left-10 max-w-2xs p-4 rounded-xl shadow shadow-stone-50/50 bg-black font-medium">
    <p>Log out {{ user.username }}</p>
  </div> -->
  <div class="absolute bottom-20 left-5"> 
    <div class="w-50 border border-stone-400/50 rounded-xl bg-black py-3 font-medium relative z-20">
      <button class="w-full px-5 py-2 hover:bg-white/10 transition-all duration-200">Log out {{ user.username }}</button>
    </div>
    <div class="absolute inset-1 rounded-xl blur-md bg-stone-50/40 z-10"></div>
  </div>
</template>


<style scoped>

</style>