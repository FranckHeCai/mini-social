export default function (username: string){
  const split = username.split(' ')
  const newUsername = split.join('_')
  return newUsername
}