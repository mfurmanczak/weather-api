from cal_setup import get_calendar_service

# Take id of event to delete
print("Enter the event ID to delete")
delete_event_id = input()

# Delete the event and error handling
service = get_calendar_service()
try:
    service.events().delete(
        calendarId='primary',
        eventId=delete_event_id,
    ).execute()
except googleapiclient.errors.HttpError:
    print("Failed to delete event")

print("Event deleted")