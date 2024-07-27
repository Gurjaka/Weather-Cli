import requests
import sys
from modules.design import *

def get_weather(city):
    '''
    Fetch city info from API.
    
    Get data from API and display according to users choice.
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
        top, side, width = border()

        print(f'{top}\n{side}\n{txt('Option Menu:')}\n{side}\n{txt('1) Location')}\n{txt('2) Condition')}\n{txt('3) All info')}\n{txt('4) Previous menu')}\n{txt('5) Quit')}\n{side}\n{top}')
        
        opt = padding('Choose option:')
        
        match opt:
            case '1':
                clear()
                top, side, width = border()

                welcome()

                print(f'{top}\n{side}')
                for key, value in data['location'].items():
                    if key == 'name':
                        print(txt(value))
                    print(txt(f'{key}: {value}'))
                print(f'{side}\n{top}')
                
            case '2':
                clear()
                welcome()

                print(f'{top}\n{side}')
                for key, value in data['current'].items():
                    if key == 'pressure_mb':
                        break
                    print(txt(f'{key}: {value}'))
                print(f'{side}\n{top}')
            
            case '3':
                clear()
                welcome()

                print(f'{top}\n{side}')
                print(f'{txt('Location: ')}\n{side}')

                for key, value in data['location'].items():
                    if key == 'name':
                        print(txt(value))
                    print(txt(f'{key}: {value}'))
                
                print(f'{side}\n{txt('Condition: ')}\n{side}')
                for key, value in data['current'].items():
                    if key == 'pressure_mb':
                        break
                    print(txt(f'{key}: {value}'))

                print(f'{side}\n{top}')
            
            case '4':
                break
        
            case '5':
                sys.exit()
        
    return data