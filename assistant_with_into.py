import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime
from algorithms import weather, get_timezone, open_website, google_search, draw_hello, wiki, thank, bye, joke
from time import sleep
from termcolor import colored
import os
os.system('color')

def speak(you, robot):
    if name == "":
        print(colored("You: " + you, "green"))
    else:
        print(colored(name + ": " + you, "green"))
    print("Assistant: " + robot)
    robot_mouth.say(robot)
    robot_mouth.runAndWait()

draw_hello()
robot_mouth = pyttsx3.init()
print("Hi, I'm your assistant")
robot_mouth.say("Hi, I'm your assistant")
robot_mouth.runAndWait()
sleep(1)

print("What should I call you? ")
robot_mouth.say("What should I call you? ")
robot_mouth.runAndWait()
name = ""

while True:
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot = ""
    with speech_recognition.Microphone() as mic:
        robot_ear.adjust_for_ambient_noise(mic)
        print(colored("Listening...\n", "blue"))
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    if you == "":
        robot = "I can't hear you, try again"
        speak(you, robot)
    else:
        name = you
        speak(you, "Hello " + you)
        sleep(0.5)
        print("Please ask me some questions")
        robot_mouth.say("Please ask me some questions")
        robot_mouth.runAndWait()
        break

while True:
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot = ""
    with speech_recognition.Microphone() as mic:
        print(colored("Listening...\n", "blue"))
        audio = robot_ear.listen(mic)
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    if you == "":
        robot = "I can't hear you, try again"
        speak(you, robot)
    elif "hello" in you:
        robot = "Hello " + name
        speak(you, robot)
    elif "today" and "date" in you:
        today = date.today()
        robot = "Today's date is " + today.strftime("%B %d, %Y")
        speak(you, robot)
    elif "weather" in you:
        # words = you.split()
        i = you.index("in")
        city = you[(i + 2):len(you)].strip()
        if city == "in":
            speak(you, "Please choose a city")
        else:
            speak(you, weather(city))
    elif "time" in you:
        i = you.index("in")
        city = you[(i + 2):len(you)].strip()
        if city == "in":
            speak(you, "Please choose a city")
        else:
            speak(you, get_timezone(city))
    elif "stupid" in you:
        speak(you, "No, you are the most stupid person in the world. Haha")
    elif "open" in you:
        words = you.split()
        web = words[-1]
        robot = "Opening " + web + " ..."
        speak(you, robot)
        open_website(web)
        sleep(2)
    elif "search" in you or "Search" in you:
        words = you.split()
        words.pop(0)
        robot = "Searching " + " ".join(words) + " ..."
        speak(you, robot)
        google_search(words)
        sleep(5)
    elif "tell" in you and "about" in you:
        words = you.split()
        ab = words.index("about")
        output = []
        i = ab + 1
        while i < len(words):
            output.append(words[i])
            i += 1
        query = " ".join(output)
        speak(you, "Searching info about "+query+"...")
        robot = wiki(query)
        print("Assistant: " + robot)
        robot_mouth.say(robot)
        robot_mouth.runAndWait()
    elif "joke" in you or "funny" in you:
        robot = joke()
        speak(you, robot)
    elif "thank" in you:
        robot = thank(name)
        speak(you, robot)
        break
    elif "bye" in you:
        robot = bye(name)
        speak(you, robot)
        break
    else:
        robot = "I don't understand, please speak again"
        speak(you, robot)
