<script lang="ts" setup>
const pages = [
  {
    page: 'Home',
    path: '/'
  },
  {
    page: 'Profile',
    path: '/profile'
  }
]
</script>
<template>
  <header>
    <ul>
      <li v-for="route in pages" :key="route.path">
        <NuxtLink to='/'>{{ route.page }}</NuxtLink>
      </li>
    </ul>
  </header>
</template>