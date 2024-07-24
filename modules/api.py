import requests
import sys
from modules.design import *
from simple_term_menu import TerminalMenu 

def get_weather(city):
    '''
    Fetch city info from API
    '''
    # Define url and API 
    key = 'f6f227bea0c24040978115410242407'
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    
    # Define get function
    response = requests.get(url)
    data = response.json()
    
    while True:
        # Terminal Menu
        print()
        options = ['1) Location', '2) Condition', '3) All info', '4) Previous menu', '5) Quit']
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        opt = options[menu_entry_index]
        
        if opt == '1) Location':
            for key, value in data['location'].items():
                print(f'{key}: {value}')
            
        elif opt == '2) Condition':
            for key, value in data['current'].items():
                if key == 'pressure_mb':
                    break
                print(f'{key}: {value}')
          
        elif opt == '3) All info':
            for key, value in data['location'].items():
                print(f'{key}: {value}')
            
            print()
            
            for key, value in data['current'].items():
                if key == 'pressure_mb':
                    break
                print(f'{key}: {value}')
        
        elif opt == '4) Previous menu':
            break
        
        elif opt == '5) Quit':
          sys.exit()
        
    return data