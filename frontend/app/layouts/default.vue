<template>
  <div class="flex justify-end min-h-screen bg-black text-stone-50">
    <SideBar />

    <!-- Main Content -->
    <main class="max-w-7xl w-full h-screen overflow-y-auto">
      <slot></slot>
    </main>
  </div>
</template>

<script setup lang="ts">


</script>

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