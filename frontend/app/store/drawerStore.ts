import { defineStore } from "pinia";

export const useDrawerStore = defineStore('drawer-store', ()=>{
  const showPopup = ref(false)
  const showPostPopup = ref(false)

  const togglePopup = () => {
    showPopup.value = !showPopup.value
  }
  const closePopup = () =>{
    showPopup.value = false
  }

  const togglePostPopup = () => {
    showPostPopup.value = !showPostPopup.value
  }
  const closePostPopup = () =>{
    showPostPopup.value = false
  }
  return { showPopup, togglePopup, closePopup, showPostPopup, togglePostPopup, closePostPopup }
})