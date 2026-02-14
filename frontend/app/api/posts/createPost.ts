import type { apiGenericResponse } from "~/type"
import { fetch_with_token } from "../fetch_with_token"
import { API_ROUTES } from "../apiRoutes"

export const createPost = async (data: FormData) =>{
  try {

    const response: apiGenericResponse = await fetch_with_token(`${API_ROUTES.posts}`, {
      method: 'POST',
      body: data
    })

    console.log(response.message)
  } catch (error) {
    console.error(error)
  }
}