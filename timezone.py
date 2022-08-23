# importing module
import datetime
import calendar
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def get_timezone(city_name):
    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    lad = city_name
    # getting Latitude and Longitud
    location = geolocator.geocode(lad)
    # pass the Latitude and Longitud
    # into a timezone_at
    # and it return timezone
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    result = str(result)
    globalDate = datetime.datetime.now(pytz.timezone(result))
    return "The time now in " + city_name + " is: " + globalDate.strftime('%H:%M %p, %A, %B %d, %Y')