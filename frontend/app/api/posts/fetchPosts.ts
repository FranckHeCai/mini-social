import type { Posts } from './../../type';
import { useAuthStore } from "~/store/authStore"
import { usePostStore } from "~/store/postStore"
import { API_ROUTES } from "../apiRoutes"
import { fetch_with_token } from '../fetch_with_token';


export const fetchPosts = async () => {
  const authStore = useAuthStore()
  const {token} = storeToRefs(authStore)
  
  const postStore = usePostStore()
  try {
    if (!token.value){
      console.log('token: ', token.value)
    }
    // const response: Posts = await $fetch(`${API_ROUTES.posts}`, {
    //   method: 'GET',
    //   headers: {
    //     'Authorization' : `Bearer ${token.value}`
    //   }
    // })

    const response = await fetch_with_token(`${API_ROUTES.posts}`, {
      method: 'GET'
    })
    postStore.setPosts(response)
  } catch (error) {
    console.error(error)
  }
}