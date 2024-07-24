from modules.utils import *
from simple_term_menu import TerminalMenu

def greet():
    '''
    Simple greet menu
    
    Simple greet with option menu, making easy to navigate.
    '''
    clear()
    
    # Welcome box on top
    width = term('width')
    top = '-' * width
    side = f'|{" " * (width - 2)}|'
    welcome = 'Welcome to weather cli!'
    
    # Calculate stuff
    welcome_length = len(welcome)
    total_padding = (width - welcome_length - 2)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    
    middle = f'|{" " * left_padding}{welcome}{" " * right_padding}|'
    if len(middle) < width:
        middle += ' ' * (width - len(middle))
    
    print(f'\n{top}')
    print(side)
    print(middle)
    print(side)
    print(f'{top}\n')
        
    options = ['1) Weather', '2) Support', '3) About us', '4) FAQ', '5) Buy me a coffee', '6) Quit']
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    
    return options[menu_entry_index]

def city():
    '''
    Simple city selection menu.
    '''
    clear()
    
    width = term('width')
    top = '-' * width
    side = f'|{" " * (width - 2)}|'
    
    # First Screen
    print(f'\n{top}')
    city = input('  City: ')
    clear()
    
    # Create the content string and calculate padding
    content = f'  City: {city}'
    content_length = len(content)
    total_padding = (width - content_length - 2)  # 2 for the borders
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    
    # Create the formatted output
    middle = f'|{" " * left_padding}{content}{" " * right_padding}|'
    
    # Ensure the middle line is exactly the width of the terminal
    if len(middle) < width:
        middle += ' ' * (width - len(middle))
    
    print(f'\n{top}')
    print(side)
    print(middle)
    print(side)
    print(f'{top}\n')
    
    return city
