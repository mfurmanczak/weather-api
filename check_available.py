import datetime
import weather_gain
import list_events
from cal_setup import get_calendar_service

break_times = []

def get_break_times():
    end = ''
    for event in list_events.events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        if start != end and end != '':
            break_times.append([end, start])
        end = event['end'].get('dateTime', event['end'].get('date'))
    return break_times

# get_busy_times()
# print(break_times)
# print(busy_times)
            
# generate_total_times()
# print(total_times)
# print(get_busy_times())
   