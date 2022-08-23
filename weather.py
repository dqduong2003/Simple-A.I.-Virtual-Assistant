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
