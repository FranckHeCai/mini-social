import { API_ROUTES } from "../apiRoutes"
import { fetch_with_token } from '../fetch_with_token';
import { useUserStore } from '~/store/userStore';


export const fetchUserPosts = async () => {
  const userStore = useUserStore()
  const { user, loading } = storeToRefs(userStore)
  try {
    loading.value = true
    if(!user.value) return
    const response = await fetch_with_token(`${API_ROUTES.posts}/user/${user.value.id}`, {
      method: 'GET'
    })
    userStore.setUserPosts(response)
    loading.value = false
  } catch (error) {
    console.error(error)
  }
}