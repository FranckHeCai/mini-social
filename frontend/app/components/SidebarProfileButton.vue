<script setup lang="ts">
const props = defineProps<{
  username: string
  tag: string
}>()
</script>

<template>
  <button class="p-2 sm:px-3 sm:py-2 flex items-center justify-center sm:gap-2 hover:bg-white/10 transition-colors duration-200 rounded-full">
    <ProfilePicture size="11" src="../assets/feitan.jpg" />
    <div class="flex-1 hidden sm:inline-block">
      <h3 class="text-start">{{ props.username }}</h3>
      <p class="text-start text-secondary">{{ props.tag }}</p>
    </div>

    <IconsDots class="size-5 hidden sm:block" />

  </button>
</template>

<style scoped>

</style>