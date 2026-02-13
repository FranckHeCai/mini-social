<script setup lang="ts">
import { API_ROUTES } from '~/api/apiRoutes';
import { Logout } from '~/api/auth/logout';
import { fetch_with_token } from '~/api/fetch_with_token';
import { useAuthStore } from '~/store/authStore';
import { useDrawerStore } from '~/store/drawerStore';
import { useUserStore } from '~/store/userStore';

const userStore = useUserStore()
const {user} = storeToRefs(userStore)

const drawerStore = useDrawerStore()

const formatUsername = (username: string) =>{
  const split = username.split(' ')
  const newUsername = split.join('_')
  return newUsername
}

const handleLogout = () =>{
  drawerStore.closePopup()
  Logout()
}
</script>

<template>
  <BasePopup extraClass="py-3 w-50">
      <button @click="handleLogout" class="w-full px-5 py-2 text-start hover:bg-white/10 transition-all duration-200">Log out <span class="text-sm">@{{ user?.username ? formatUsername(user.username) : '' }}</span></button>
  </BasePopup>
</template>


<style scoped>

</style>