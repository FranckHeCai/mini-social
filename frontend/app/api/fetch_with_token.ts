import { useAuthStore } from "~/store/authStore"
import { storeToRefs } from "pinia"

interface FetchWithTokenOptions {
  method?: "GET" | "POST" | "PUT" | "DELETE" | "PATCH" | "OPTIONS" | "HEAD"
  headers?: Record<string, string>
  body?: any
}

export const fetch_with_token = async <T = any>(
  url: string,
  options: FetchWithTokenOptions = {}
): Promise<T> => {
  const authStore = useAuthStore()
  const { token } = storeToRefs(authStore)

  const headers = {
    ...(token.value ? { 'Authorization': `Bearer ${token.value}` } : {}),
    ...(options.headers || {})
  }

  try {
    const response: T = await $fetch(url, {
      ...options,
      headers
    })
    return response
  } catch (error) {
    console.error('API fetch error:', error)
    throw error
  }
}
