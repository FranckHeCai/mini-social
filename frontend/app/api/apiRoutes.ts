const config = useRuntimeConfig()

export const API_ROUTES = {
  base: config.public.CLIENT,
  health: `${config.public.CLIENT}/health`,
  auth: `${config.public.CLIENT}/auth`,
  login: `${config.public.CLIENT}/auth/jwt`,
  posts: `${config.public.CLIENT}/posts`,
  users: `${config.public.CLIENT}/users`
}