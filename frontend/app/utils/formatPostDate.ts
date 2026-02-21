export default function(date: Date){
  const timeAgo = useTimeAgo(
    () => new Date(date), {
      messages: {
        justNow: 'now',
        past: '{0}',
        future: 'in {0}',
        invalid: '',
        minute: '{0}m ago',
        minutes: '{0}m ago',
        hour: '{0}h ago',
        hours: '{0}h ago',
        day: '{0}d ago',
        days: '{0}d ago',
        week: '{0}w ago',
        weeks: '{0}w ago',
        month: '{0}mo ago',
        months: '{0}mo ago',
        year: '{0}y ago',
        years: '{0}y ago',

      }
    })
  
  return timeAgo
}