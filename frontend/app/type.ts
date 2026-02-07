export interface User {
  username: string
  tag: string
}
export interface Post {
  pp: string
  user: User
  content: string
  file?: File
}

