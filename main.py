#  /home/gurami/Documents/Python-Projects/.venv/bin/python /home/gurami/Documents/Weather/main.py    
# import modules
import sys
from modules.utils import *
from modules.design import *
from modules.api import *
from modules.options import *

# clear the console screen
clear()

# main loop for user interaction
while True:
    # display greeting and menu options, and get user choice
    # process user choice
    match greet():
        case '1':
            # option 1: Get weather information for a city
            get_weather(city())

        case '2':
            # option 2: Display support information
            support()

        case '3':
            # option 3: Display information about the team
            aboutus()

        case '4':
            # option 4: Display frequently asked questions
            faq()

        case '5':
            # option 5: Support the developer by buying coffee
            coffee()

        case '6':
            # option 6: exit the program
            clear()
            sys.exit()  # exit the program
