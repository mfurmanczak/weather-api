from datetime import datetime, timedelta
from cal_setup import get_calendar_service

# Take the inputs from the user
service = get_calendar_service()

# Take id of event to delete
print("Enter the event ID to update")
update_event_id = input()

print("What is the new name for the event?")
new_name = input()

print("What is the description for the event?")
description = input()

print("When is the event? (YYYY-MM-DD)")
date = input()

print("What is the start time for the event? (HH:MM)")
start = input()
start = start.split(":")
print(start)
print("How long is the event?")
duration = input()
duration = int(duration)

# Process the inputs and format them for the API
d = datetime.strptime(date, "%Y-%m-%d")

full_start_date = datetime(d.year, d.month, d.day, (int)(start[0]), (int)(start[1]), 0, 0)
full_end_date = full_start_date + timedelta(hours=duration)

full_start_date = full_start_date.isoformat()
full_end_date = full_end_date.isoformat()

event_result = service.events().update(
    calendarId='primary',
    eventId=update_event_id,
    body={
        "summary": new_name,
        "description": description,
        "start": {"dateTime": full_start_date, "timeZone": 'Europe/London'},
        "end": {"dateTime": full_end_date, "timeZone": 'Europe/London'},
    },
).execute()

print("updated event")
print("id: ", event_result['id'])
print("summary: ", event_result['summary'])
print("starts at: ", event_result['start']['dateTime'])
print("ends at: ", event_result['end']['dateTime'])