<script setup lang="ts">
import { API_ROUTES } from '~/api/apiRoutes';
import { fetch_with_token } from '~/api/fetch_with_token';
import { useDrawerStore } from '~/store/drawerStore';
import { useUserStore } from '~/store/userStore';

const userStore = useUserStore()
const {user} = storeToRefs(userStore)

const drawerStore = useDrawerStore()

const loading = ref(false)

const emit = defineEmits<{
  deletePost: []
}>()

const handleDeletePost = () =>{
  emit('deletePost')
}
</script>

<template>
  <BasePopup>
    <button @click="handleDeletePost" class="w-50 flex items-center gap-3 p-3 hover:bg-white/5 cursor-pointer transition-all duration-200">
      <div class="size-5">
        <IconsDelete />
      </div>
      <p>Delete post</p>
    </button>
  </BasePopup>
</template>


<style scoped>

</style>