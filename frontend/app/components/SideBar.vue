<script setup lang="ts">
import { onClickOutside } from '@vueuse/core';
import { useDrawerStore } from '~/store/drawerStore';


const drawerStore = useDrawerStore()
const {showPopup} = storeToRefs(drawerStore)
const popupRef = useTemplateRef('popupRef')

const handleTogglePopup = () => {
  drawerStore.togglePopup()
}

onClickOutside(popupRef, (event) => {
  drawerStore.closePopup()
})

</script>
<template>
      <!-- Sidebar -->
    <aside class="relative max-w-3xs sm:w-full p-3 flex flex-col justify-between">
      <nav class="flex flex-col gap-3 items-center sm:items-start">
        <NuxtLink
          to="/"
          class="flex items-center gap-3 p-2 sm:pr-10"
        >
          <img class="size-7" src="../assets/x_logo.svg" alt="x_logo">
        </NuxtLink>
        <NuxtLink
          to="/"
          v-slot="{isActive}"
        >
          <div 
            class="flex items-center gap-3 p-2 sm:pr-10 hover:bg-white/15 transition-colors duration-100 rounded-full text-xl"
            :class="[
              isActive ? 'font-bold' : 'font-light'
            ]"
          >
            <IconsHome class="size-8" />
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
            <IconsProfile class="size-8" />
            <span class="hidden sm:inline">Profile</span>
          </div>
        </NuxtLink>
        <button class="bg-stone-50 p-3 sm:py-3 sm:px-0 sm:w-full rounded-full text-black">
          <IconsCreate class="size-6 sm:hidden" />
          <p class="text-lg  font-bold hidden sm:inline">Post</p>
        </button>
      </nav>
      <SidebarProfileButton @click="handleTogglePopup" username="Zuko" tag="@zuko_avatar"/>
      <div class="absolute bottom-20 left-5" ref="popupRef" v-if="showPopup">
        <LogoutPopup />
      </div>
    </aside>
</template>


<style scoped>

</style>