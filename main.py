#  /home/gurami/Documents/Python-Projects/.venv/bin/python /home/gurami/Documents/Weather/main.py    
import json
import requests
import sys
from modules.utils import *
from modules.design import *
from modules.api import *
from modules.options import *

clear()

while True:
    opt = greet()
    
    if opt == '1) Weather':
        get_weather(city())

    elif opt == '2) Support':
        support()

    elif opt == '3) About us':
        aboutus()

    elif opt == '4) FAQ':
        faq()

    elif opt == '5) Buy me a coffee':
        coffee()

    elif opt == '6) Quit':
        clear()
        sys.exit()