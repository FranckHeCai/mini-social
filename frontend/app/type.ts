export type ID = `${string}-${string}-${string}-${string}-${string}`

export interface User {
  id: ID
  email: string
  username: string
  created_at: Date
  tag?: string
  followers?: number
  following?: number
  is_superuser?: boolean
  is_verified?: boolean
}
export interface Post {
  id: ID
  title: string
  content: string
  user: User
  created_at: Date
  file?: File
}

export type Posts = Post[]

export type apiGenericResponse = {
  message: string
}

export type apiAuthenticationResponse = {
  access_token: string
  token_type: string
}

