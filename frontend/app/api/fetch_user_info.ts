import { useUserStore } from '~/store/userStore';
import type { User } from './../type';
import { API_ROUTES } from './apiRoutes';
import { fetch_with_token } from './fetch_with_token';
export const fetch_user_info = async () =>{
  const userStore = useUserStore()

  try {
    userStore.loading = true
    const userInfo: User = await fetch_with_token(`${API_ROUTES.users}/me`, {
        method: 'GET'
      })  
  
    userStore.setUser(userInfo)
    userStore.loading = false
    
  } catch (error) {
    console.error(error)
  }
}