import requests
import time
import datetime 
import pytz
import json
import urllib.request
import time
import webbrowser
import geocoder
import pyttsx3
import wikipedia
import sqlite3

# Voz de Erwin

def assistant(audio):
    engine = pyttsx3.init()
    # getter: To get the current
    # engine property value
    voices = engine.getProperty('voices')
    # setter method
    # [0] for male voice
    # [1] for female voice
    engine.setProperty('voices', voices[0].id)
    # Method governing assistant's speech
    engine.say(audio)
    # Blocks/processes queued commands
    engine.runAndWait()

def space():
    print('Unfortunately, the space function does not seem to work')

def weather():
    assistant('Please, enter your location')
    location = input('Please, enter your location : ')

    api_complete_link = 'https://api.openweathermap.org/data/2.5/weather?q='+ location +'&appid=08c43f1245cecfbb6611738969af6544'
    api_link = requests.get(api_complete_link)
    api_data = api_link.json()
    temp_in_celcius = int(api_data['main']['temp']) - 273

    time.sleep(1.5)

    assistant(f'The temperature in {location} is: {temp_in_celcius}°C')
    print(f'The temperature in {location} is: {temp_in_celcius}°C')

def my_time():
        tday = datetime.date.today()
        dt_bs = datetime.datetime.now(tz=pytz.timezone('America/Argentina/Buenos_Aires'))
        ftime = dt_bs.strftime('%H:%M:%S')
        print(f'''Local Date: {tday}
                  Local Time: {ftime}''') 

def research():
     # to pull information from Wiki
        assistant("Checking the wikipedia ")
        try:
            command = command.replace("wikipedia", "")
            # it will limit the summary to four lines
            result = wikipedia.summary(command, sentences=4)
            assistant("As per wikipedia")
            assistant(result)
        except wikipedia.exceptions.PageError:
            print('Well, is seems there is nothing on wikipedia for that topic.')
            assistant('Well, is seems there is nothing on wikipedia for that topic.')

def open_medium():
    assistant("Opening Medium.com")
                # the function reaches out to the
                # default browser
    webbrowser.open("www.medium.com")

def open_google():
    assistant("Opening Google ")
    webbrowser.open("www.google.com")

def new_user_function():
    try:
        conn = sqlite3.connect('perfiles.db')

        cursor = conn.cursor()

        first_name = name
        last_name = input('What is your last name? ')
        age = input('Age: ')

        cursor.execute('INSERT INTO perfiles VALUES(:first_name, :last_name, :age)',
            {
                'first_name' : first_name,
                'last_name' : last_name,
                'age'   : age
            })
        conn.commit()

                
        conn.close()
    except NameError:
        print('Apologies, but it looks like you are not a new user.')


# Inicio
print('New User? (y/n) ')
intro = input('> ')
new_user = False

if intro.lower() == 'y':
    assistant('Greetings Sir or Madamme, what is your name?')
    print('Greetings Sr or Madamme, what is your name?')
    new_user = True
    name = input('> ')

    assistant(f'Nice to meet you {name}, I am Erwin')
    print(f'Nice to meet you {name}, I am Erwin')
else:
    conn = sqlite3.connect('perfiles.db')

    cursor = conn.cursor()
    
    list_of_pw = cursor.execute('SELECT last_name FROM perfiles.db')

    print('Plese, enter your last name')
    command = ('> ')
    if command in list_of_pw:
        print('welcome')
    else:
        ('nope')

    conn.close()

time.sleep(1)

print('*type h for options ')

while True:

    command = input('> ')  

    if command == 'h':
        print('''Please, type one of the following options:

        1. 'space': for ISS location and current crew
        2. 'weather': for local temperature
        3. 'time': for local day and time
        4. 'research': wikipidia information
        5. 'open medium/google': medium so as to open default browser, google to directly open google.
        6. 'new user': to contribute with my (Erwin) database.
        7. 'bye': to quit the program
        ''')
        assistant('''Please, type one of the following options:

                1. 'space': for ISS location and current crew
                2. 'weather': for local temperature
                3. 'time': for local day and time
                4. 'research': wikipidia information
                5. 'open medium/google': medium so as to open default browser, google to directly open google.
                6. 'new user': to contribute with my (Erwin) database.
                7. 'bye': to quit the program
                ''')

    elif command =='space':
        space()

    elif command == 'weather':
        weather()

    elif command == 'time':
        my_time()

    elif "research" in command:
        #research()
        print('Temporaly unavailable')
        
    elif "open medium" in command:
        open_medium()
    
    elif "open google" in command:
        open_google()

    elif 'new user' in command and new_user == True:
        new_user_function()

    elif 'bye' in command:
        print('bye')
        assistant('bye')
        break

        





                



