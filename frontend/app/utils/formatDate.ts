export default function (date: Date){
  const newDate = new Date(date)
  const months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
  ]
  const currentMonth = months[newDate.getUTCMonth()]
  const currentYear = newDate.getUTCFullYear()
  return `${currentMonth} ${currentYear}`
}