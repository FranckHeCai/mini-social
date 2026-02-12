<script setup lang="ts">
import type { User } from '~/type';

const props = defineProps<{
  pp: string
  user: User
  content: string
  files?: File
  posted?: Date
}>()

const username = ref('INKU')
const tag = ref<`@${string}`>('@Inku_fr')
const posted = ref('5h')
</script>

<template>
  <div class="p-4 flex gap-2 border-b border-white/20">
    <div>
      <div class="size-11 rounded-full overflow-hidden">
          <img class="h-full w-full" src="../assets/feitan.jpg" alt="profile-picture">
      </div>
    </div>
    <div class="">
      <div class="flex flex-wrap gap-1 items-center">
        <h3 class="font-medium">{{ props.user.username }}</h3>
        <div class="size-5">
          <img class="h-full w-full" src="../assets/x_verified_badge.svg" alt="">
        </div>
        <p class="text-secondary">
          <span v-if="$props.user.tag">{{ props.user.tag }}</span>
          <span v-else>@{{ props.user.username }}</span>
          · {{ posted }}</p>
      </div>
      <p>
        {{ props.content }}
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
  </div>
</template>


<style scoped>

</style>