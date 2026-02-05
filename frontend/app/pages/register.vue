<template>
  <div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full">
      <div class="mt-6 flex flex-col gap-3">
        <h2 class="text-center text-2xl lg:text-3xl font-extrabold text-gray-900">
          Sign up to Mini Social
        </h2>
        <p class="text-sm text-center text-gray-600">
          Or
          <NuxtLink to="/login" class="font-medium text-blue-600 hover:text-blue-600 hover:cursor-pointer">
            sign in to existing account
          </NuxtLink>
        </p>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleRegister">
        <input type="hidden" name="remember" value="true" />
        <div class="shadow-sm -space-y-px">
          <div>
            <label for="email" class="sr-only">Email address</label>
            <input
              id="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm"
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
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
              placeholder="Password"
              v-model="form.password"
            />
            <button
            @click="handleShowPassword"
            type="button"
            class="absolute top-2 right-3 size-6 flex justify-center text-gray-500"
            :disabled="loading"
            >
              <IconsEye v-if="!showPassword" />
              <IconsEyeOff v-else />
            </button>
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:bg-blue-800"
            :disabled="loading"
          >
            <span v-if="loading" class="">
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </span>
            <span v-else>Create account</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useAuthStore } from '~/store/authStore'

const authStore = useAuthStore()
const {token, loggedIn} = authStore

console.log(`CURRENT TOKEN: ${token} - ${loggedIn}`)

definePageMeta({
  layout: 'auth'
})
const form = reactive({
  email: '',
  password: ''
})

const loading = ref(false)
const showPassword = ref(false)

const handleRegister = async () => {
  loading.value = true
  try {
    // TODO: Implement login logic, e.g., call API
    console.log('Login attempt:', form)
    // Simulate API call
    await new Promise(resolve => setTimeout(resolve, 1000))
    // On success, redirect or show message
    alert('Login successful!')
  } catch (error) {
    console.error('Login failed:', error)
    alert('Login failed!')
  } finally {
    loading.value = false
  }
}

const handleShowPassword = () => {
  showPassword.value = !showPassword.value
} 
</script>