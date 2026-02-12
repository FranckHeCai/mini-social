<script setup lang="ts">
import { fetch_token } from '~/api/fetch_token'
import { fetch_user_info } from '~/api/fetch_user_info'
import Logo from '~/components/Icons/Logo.vue'
import { useAuthStore } from '~/store/authStore'
import { useUserStore } from '~/store/userStore'

const authStore = useAuthStore()
const {token} = storeToRefs(authStore)

const userStore = useUserStore()

definePageMeta({
  layout: 'auth'
})
const form = reactive({
  username: '',
  password: ''
})

const loading = ref(false)
const showPassword = ref(false)
const alertError = reactive({
  show: false,
  message: ''
})

const handleLogin = async () => {
  loading.value = true
  try {
    // LOGIN API CALL
    const response: string = await fetch_token({username: form.username, password: form.password})
    
    const newToken = response
    authStore.setToken(newToken)

    await fetch_user_info()
    // On success, redirect
    navigateTo('/')
  } catch (error) {
    console.error('Login failed:', error)

    alertError.message = "failed to fetch"
    alertError.show = true

    setTimeout(()=>{
      alertError.show = false
      alertError.message = ''
    }, 2000)
  } finally {
    loading.value = false
  }
}

const handleShowPassword = () => {
  showPassword.value = !showPassword.value
} 

</script>

<template>
  <div class="relative min-h-screen grid sm:grid-cols-2 items-center gap-10 py-3 px-4 sm:px-6 lg:px-8 bg-black text-primary">
    <div class="hidden sm:block mx-auto max-w-sm w-full">
      <Logo />
    </div>
    <div class="absolute sm:hidden top-3 right-1/2 translate-x-1/2 size-10">
      <Logo />
    </div>
    <div class="mx-auto max-w-md w-full flex flex-col gap-8">
      <div>
        <h2 class="text-2xl sm:text-3xl font-bold">
          Sign in to X
        </h2>
      </div>
      <form class="flex flex-col gap-8" @submit.prevent="handleLogin">
        <input type="hidden" name="remember" value="true" />
        <div class="flex flex-col gap-3">
          <div>
            <label for="email" class="sr-only">Email address</label>
            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="appearance-none relative block w-full px-2 py-3 border border-gray-500 placeholder-gray-500 text-lg text-secondary rounded-sm focus:outline-none  focus:border-blue-400 focus:border-2" 
              placeholder="Email address"
              v-model="form.username"
            />
          </div>
          <div class="relative">
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              name="password"
              :type="showPassword ? 'text' : 'password'"
              autocomplete="current-password"
              required
              class="appearance-none relative block w-full px-2 py-3 border border-gray-500 placeholder-gray-500 text-lg text-secondary rounded-sm focus:outline-none  focus:border-blue-400 focus:border-2"
              placeholder="Password"
              v-model="form.password"
            />
            <button
            @click="handleShowPassword"
            type="button"
            class="absolute top-4 right-3 size-6 flex justify-center text-gray-500"
            :disabled="loading"
            >
              <IconsEye v-if="!showPassword" />
              <IconsEyeOff v-else />
            </button>
          </div>
        </div>

        <div class="flex flex-col gap-6">
          <button
            type="submit"
            class="bg-stone-50 p-2 sm:w-full rounded-full font-medium text-black cursor-pointer hover:opacity-85 transition-all duration-200"
            :disabled="loading"
          >
            <span v-if="loading" class="">
              <svg class="animate-spin h-5 w-5 text-black" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </span>
            <span v-else>Sign in</span>
          </button>

          <button 
            type="button"
            class="p-2 sm:w-full rounded-full font-medium text-stone-50 border cursor-pointer hover:bg-white/15 transition-all duration-200"
          >
            Forgot password?
          </button>
        </div>
      </form>
      <p class="text-secondary">
          Don't have an account? 
          <NuxtLink to="/register" class="text-blue-400 hover:underline">
            Sign up
          </NuxtLink>
      </p>
      <div v-if="alertError.show" class="animate-alert mt-4 py-2 px-4 inline-block font-medium bg-rose-600 text-stone-50 rounded-md">
        <p>ERROR</p>
      </div>
    </div>
  </div>
</template>