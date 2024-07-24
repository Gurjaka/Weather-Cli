#  /home/gurami/Documents/Python-Projects/.venv/bin/python /home/gurami/Documents/Weather/main.py    
# import modules
import json
import requests
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
    opt = greet()
    
    # process user choice
    if opt == '1) Weather':
        # option 1: Get weather information for a city
        get_weather(city())

    elif opt == '2) Support':
        # option 2: Display support information
        support()

    elif opt == '3) About us':
        # option 3: Display information about the team
        aboutus()

    elif opt == '4) FAQ':
        # option 4: Display frequently asked questions
        faq()

    elif opt == '5) Buy me a coffee':
        # option 5: Support the developer by buying coffee
        coffee()

    elif opt == '6) Quit':
        # option 6: exit the program
        clear()
        sys.exit()  # exit the program
