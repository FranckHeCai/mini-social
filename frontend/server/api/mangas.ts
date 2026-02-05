import manga_data from './manga_data.json'
export default defineEventHandler(async ()=>{
  return new Promise<any>((resolve) => {
    setTimeout(()=> {
      resolve(manga_data)
    }, 2000)
  })
})