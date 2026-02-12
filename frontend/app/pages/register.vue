<script setup lang="ts">
import { API_ROUTES } from '~/api/apiRoutes'
import { fetch_token } from '~/api/fetch_token'
import { fetch_with_token } from '~/api/fetch_with_token'
import Logo from '~/components/Icons/Logo.vue'
import { useAuthStore } from '~/store/authStore'
import { useUserStore } from '~/store/userStore'
import type { User } from '~/type'

const authStore = useAuthStore()
const {token, loggedIn} = authStore

const userStore = useUserStore()

definePageMeta({
  layout: 'auth'
})
const form = reactive({
  username: '',
  email: '',
  password: '',
  is_active: true,
  is_superuser: false,
  is_verified: true
})

const loading = ref(false)
const showPassword = ref(false)
const alertError = reactive({
  show: false,
  message: ''
})


const handleRegister = async () => {
  loading.value = true
  try {
    // SIGN UP API CALL
    console.log('Sign up attempt:', form)

    const user: User = await $fetch(`${API_ROUTES.auth}/register`, {
      method: 'POST',
      body: {
        ...(form)
      }
    })
    // On success, redirect to home page
    userStore.setUser(user)

    const response: string = await fetch_token({username: user.email, password: form.password})

    const newToken = response
    authStore.setToken(newToken)

    clearForm()
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

const clearForm = () => {
  form.username = ''
  form.email = ''
  form.password = ''
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
    <div class="mx-auto max-w-lg w-full flex flex-col gap-8">
      <div class="flex flex-col gap-20">
        <h1 class="text-5xl lg:text-6xl font-bold">Happening now</h1>
        <h2 class="text-2xl sm:text-3xl font-bold">
          Join today.
        </h2>
      </div>
      <form class="flex flex-col gap-8" @submit.prevent="handleRegister">
        <input type="hidden" name="remember" value="true" />
        <div class="flex flex-col gap-3">
          <div>
            <label for="email" class="sr-only">Username</label>
            <input
              id="username"
              name="username"
              type="text"
              autocomplete="username"
              required
              class="appearance-none relative block w-full px-2 py-3 border border-gray-500 placeholder-gray-500 text-lg text-secondary rounded-sm focus:outline-none  focus:border-blue-400 focus:border-2" 
              placeholder="Username"
              v-model="form.username"
            />
          </div>
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
              v-model="form.email"
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
            <span v-else>Create account</span>
          </button>
        </div>
      </form>
      <div class="flex flex-col gap-5">
        <p class="font-medium text-lg">
            Already have an account?
        </p>
        <NuxtLink to="/login" class="p-2 flex justify-center sm:w-full rounded-full font-medium text-stone-50 border border-gray-500 cursor-pointer hover:bg-white/15 transition-all duration-200">
          Sign in
        </NuxtLink> 

      </div>
      <div v-if="alertError.show" class="animate-alert mt-4 py-2 px-4 inline-block font-medium bg-rose-600 text-stone-50 rounded-md">
        <p>ERROR</p>
      </div>
    </div>
  </div>
</template>
