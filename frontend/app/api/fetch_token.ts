import type { apiAuthenticationResponse } from './../type';
import { API_ROUTES } from './apiRoutes';
export const fetch_token = async (credentials:{username: string, password: string}) => {
  const response: apiAuthenticationResponse = await $fetch(`${API_ROUTES.login}/login`, {
    method: 'POST',
    headers: {
      'Content-type': 'application/x-www-form-urlencoded'
    },
    body: {
      username: credentials.username,
      password: credentials.password
    }
  })

  return response.access_token
}