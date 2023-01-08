## Script to delete events from google calendar
from cal_setup import get_calendar_service

# Delete the event
service = get_calendar_service()
try:
    service.events().delete(
        calendarId='primary',
        eventId='uogu4p2n84uscs35plnvf69t4g',
    ).execute()
except googleapiclient.errors.HttpError:
    print("Failed to delete event")

print("Event deleted")