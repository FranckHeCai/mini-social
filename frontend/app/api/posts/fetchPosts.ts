import { usePostStore } from "~/store/postStore"
import { API_ROUTES } from "../apiRoutes"
import { fetch_with_token } from '../fetch_with_token';


export const fetchPosts = async () => {
  const postStore = usePostStore()
  try {
    const response = await fetch_with_token(`${API_ROUTES.posts}`, {
      method: 'GET'
    })
    postStore.setPosts(response)
  } catch (error) {
    console.error(error)
  }
}