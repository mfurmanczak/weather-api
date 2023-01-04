import metoffer

api_key = '01234567-89ab-cdef-0123-456789abcdef'
M = metoffer.MetOffer(api_key)
x = M.nearest_loc_forecast(54.972656, -1.614074, MetOffer.THREE_HOURLY)