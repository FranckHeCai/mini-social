import { defineStore } from "pinia";

export const useDrawerStore = defineStore('drawer-store', ()=>{
  const showPopup = ref(false)
  const togglePopup = () => {
    showPopup.value = !showPopup.value
  }
  const closePopup = () =>{
    showPopup.value = false
  }
  return { showPopup, togglePopup, closePopup }
})