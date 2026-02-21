<script setup lang="ts">
import { useUserStore } from '~/store/userStore';
import { fetch_user_info } from '~/api/fetch_user_info';
import { fetchUserPosts } from '~/api/posts/fetchUserPosts';

const userStore = useUserStore()
const {user, loading, userPosts} = storeToRefs(userStore)


const returnHome = () =>{
  navigateTo('/')
}

onMounted(async () =>{
  if (!user.value){
    fetch_user_info()
  } else {
    fetchUserPosts()
  }
})
</script>

<template>
  <div class="max-w-150 border-x border-white/20">
    <LoadingSpinner v-if="loading" />
    <div v-else>
      <!-- Profile Section -->
      <div v-if="user">
        <!-- PROFILE HEADER -->
        <div class="flex justify-between px-3 py-1">
          <div class="flex gap-7 items-center">
            <button @click="returnHome" class="size-9 p-1 hover:bg-white/10 rounded-full transition-all duration-200">
              <IconsLeftArrow />
            </button>
            <div>
              <h2 class="text-lg font-bold">{{ user?.username }}</h2>
              <p class="-mt-1 text-sm text-secondary">{{ userPosts.length }} posts</p>
            </div>
          </div>
        </div>
        <!-- PROFILE BANNER -->
        <div class="background h-100 bg-white/20">
          <img class="object-cover" src="../assets/profile_background.jfif" alt="profile_background">
        </div>

        <!-- PROFILE INFO -->
        <div class="relative flex flex-col">
          <div class="pl-5">
            <div class="-mt-13 size-25 outline-3 sm:-mt-18 sm:size-33 sm:outline-4 outline-black rounded-full overflow-hidden">
              <img class="h-full w-full" src="../assets/feitan.jpg" alt="profile-picture">
            </div>
          </div>
          <div class="p-4 flex flex-col gap-3">
            <!-- USERNAME AND TAG -->
            <div>
              <h3 class="text-xl font-bold">{{ user.username }}</h3>
              <p class="text-secondary">{{ user.username ? `@${formatUsername(user.username)}` : '____'}}</p>
            </div>
            <!-- JOINED DATE -->
            <div class="text-secondary flex gap-2 items-center">
              <IconsCalendar class="size-5" />
              <p>
                Joined {{ formatDate(user.created_at) }}
              </p>
            </div>
            <!-- FOLLOWER AND FOLLOWING -->
            <div class="flex gap-5">
              <p class="text-secondary"><span class="text-primary font-medium">{{ user.following ? user.following : '0'}}</span> Following</p>
              <p class="text-secondary"><span class="text-primary font-medium">{{ user.followers ? user.followers : '0'}}</span> Followers</p>
            </div>
          </div>
          <button class="absolute top-3 right-4 border border-neutral-500 py-1 px-3 text-sm sm:text-base rounded-full font-medium hover:bg-white/10 transition-all duration-200 cursor-pointer">Edit profile</button>
        </div>
      </div>
      <!-- Post Section -->
       <FeedHeader page="Posts" />
       <ul>
        <Post v-for="post in userPosts" :key="post.id" :post />
      </ul>
    </div>
  </div>
</template>

<style scoped>
.background {
  max-height: 200px;
  width: 600px;
}
</style>