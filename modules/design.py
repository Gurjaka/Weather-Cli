from modules.utils import *

def welcome():
    # Welcome box on top
    top, side, width = border()
    
    print(f'\n{top}\n{side}\n{txt('Weather CLI')}\n{side}\n{top}')

def greet():
    '''
    Simple greet menu
    
    Simple greet with option menu, making easy to navigate.
    '''
    clear()

    welcome()

    top, side, width = border()

    print(f'{top}\n{side}\n{txt('1) Location')}\n{txt('2) Support')}\n{txt('3) About us')}\n{txt('4) FAQ')}\n{txt('5) Buy me a coffee')}\n{txt('6) Quit')}\n{side}\n{top}')

    opt = padding('Choose operation: ')
    
    return opt

def city():
    '''
    Simple city selection menu.
    '''
    clear()
    top, side, width = border()
    
    # First Screen
    borderText(' Location: ')
    city = padding('  City: ')

    clear()
    
    # Create the content string and calculate padding
    borderText(f'  City: {city}')
    
    return city
