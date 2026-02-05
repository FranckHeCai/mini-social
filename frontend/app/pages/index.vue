<script setup lang="ts">
interface Manga{
  name: string
  author: string
}
import { posts } from '~/data/mock_posts'

// const response = await $fetch('http://localhost:8000/health')
// const message = response.message

const user = ref({
  username: 'INKU',
  tag: '@Inku_fr'
})

const content = ref(`「OFFICIEL」L'ANIME ONE PIECE HEROINES SORTIRA LE 5 JUILLET 2026 ! 🍊<br><br>
          
        L'épisode sur NAMI sera adapté, basé sur le roman qui conte aussi des histoires sur Robin, Perona ou Vivi ! <br><br>

        NOUVEAU VISUEL !`)

</script>
<template>
  <div class="relative max-w-3xl border-x border-white/20">
    <!-- FEED HEADER -->
    <FeedHeader />
    <!-- CREATE POST HEADER -->
    <FeedPostHeader />

    <!-- FEED -->
    <!-- POST -->
    <ul>
      <Post v-for="post in posts" :key="post.user.tag" pp="../assets/feitan.jpg" :user="post.user" :content="post.content" />
    </ul>
  </div>
  

</template>