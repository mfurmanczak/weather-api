# import create_event
# import update_event
# import delete_event
# import list_events
import check_available
from datetime import datetime
import weather_gain
import cal_setup

new_city = weather_gain.get_city()


check_available.get_break_times()
# print(check_available.break_times[0][0])
# while(True):
n = 5
while(n != 0):
    current_date_time = datetime.now()
    
    year = str(current_date_time.year)
    month = str(current_date_time.month)
    day = str(current_date_time.day)
    hour = str(current_date_time.hour)
    minute = str(current_date_time.minute)
    second = str(current_date_time.second)
    tzinfo = str(current_date_time.tzinfo)
        
    if int(month) < 10:
        month = "0"+month
    if int(day) < 10:
        day = "0"+day
    if int(hour) < 10:
        hour = "0"+hour
    if int(minute) < 10:
        minute = "0"+minute
    if int(second) < 10:
        second = "0"+second

    
    current_date_time = year+'-'+month+'-'+day+"T"+hour+":"+minute+":"+second+"Z"
    #(current_date_time)
    for pause in range(len(check_available.break_times)):
        # print(check_available.break_times[pause][0])
        # print(current_date_time)
        
        # 2 if statements:
        
            # This one checks break times with the calendar
        if current_date_time == check_available.break_times[pause][0]:
            
            # This one waits for custom time to pass
        # if current_date_time == "2023-01-16T13:28:00Z":
            print(weather_gain.get_weather(new_city))
            n = 0