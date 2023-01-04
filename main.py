from calendar_api.calendar_api import google_calendar_api
m=google_calendar_api()
m.create_event(calendar_id='AIzaSyCSGlDRqLrv8mHlih_431aVIw6SQ4knFf4',
    start='2017,12,5,15,00,00',
    end='2017,12,5,15,15,00'
    description='foo'
)