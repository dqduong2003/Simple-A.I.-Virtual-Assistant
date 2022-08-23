# weather
import requests, json

def weather(city_name):
    api_key = "d03e7aefdb3bd0e357713d2e1cc605f0"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = int(y["temp"] - 273.15)
        current_humidity = y["humidity"]
        z = x["weather"]
        description = z[0]["description"]
        robot = "The city right now has " + str(description) + ", the temperature is " + str(current_temperature) + " degree Celcius, " + "and the humidty is " + str(current_humidity) + "%"
    else:
        robot = "Can't find the city name"
    return robot


# timezone
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


# open website
import webbrowser
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def open_website(web):
    if web == "Google":
        webbrowser.open("https://www.google.com")
    else:
        for url in search(web, tld="com", num=1, stop=1):
            webbrowser.open(url)


# search google
def google_search(query):
    url = "https://google.com/?q=" + "+".join(query)
    webbrowser.open(url)

def draw_hello():
    print("||    ||    =====  ||     ||       =====")
    print("||    ||  ||       ||     ||     ||     ||")
    print("||====||  ||=====  ||     ||     ||     ||")
    print("||    ||  ||       ||     ||     ||     ||")
    print("||    ||    =====  ||==== ||====   =====\n")


# wikipedia
import wikipedia
from bs4 import BeautifulSoup
import warnings
warnings.catch_warnings()
warnings.simplefilter("ignore")

def wiki(query):
    # soup = BeautifulSoup(html,features="lxml")
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "No result found, please try again"


# thank you
import random

def thank(name):
    response = ["You're welcome!", "It's my pleasure!", "Glad to help you, "+name, "Not a problem!"]
    return random.choice(response)


# goodbye
def bye(name):
    res = ["Goodbye, "+name, "Have a nice day, "+name, "Glad to help you!", "See you soon"]
    return res[random.randint(0, len(res)-1)]


# jokes
def joke():
    jokes = ["What do you call a factory that makes okay products?\nA satisfactory", "Why don't eggs tell jokes? They'd crack each other up.", "What do you call someone with no body and no nose? Nobody knows.",
             "Why can't a nose be 12 inches long?\nBecause then it would be a foot.", "I have a joke about chemistry, but I don't think it will get a reaction", "My dad told me a joke about boxing. I guess I missed the punch line.",
             "How did Harry Potter get down the hill?\nWalking. JK! Rowling.", "Why can't you hear a psychiatrist using the bathroom? Because the 'P' is silent."]
    return random.choice(jokes)