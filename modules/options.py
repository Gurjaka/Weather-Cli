import sys
from modules.utils import *

def support():
    '''
    Support page.
    
    Option menu for different types of support.
    '''
    top, side, width, = border()
    clear()

    print(f'\n{top}\n{side}\n{txt('Welcome to the support section.')}\n{txt('How can we assist you today?')}\n{side}\n{top}')
    
    print(f'{top}\n{side}\n{txt('1) The weather app is not accurate or not working')}\n{txt('2) Other Bugs')}\n{txt('3) Suggest other improvements')}\n{txt('4) Previous menu')}{txt('5) Quit')}\n{side}\n{top}')

    opt = padding('Choose operation: ')

    match opt:
        case '1':
            clear()
            borderText("If there are any issues with the weather app or it's accuracy, open issue request on our github.")
            padding('Type anything to exit: ')

        case '2':
            clear()
            borderText("If there are any bugs you want to report, open issue/pull request on our github.")    
            padding('Type anything to exit: ')

        case '3':
            clear()
            borderText("If there is anything you want to suggest us, make a pull request on our github.")
            padding('Type anything to exit: ')

def aboutus():
    '''
    Simple info about us.
    '''
    top, side, width = border()
    clear()

    print(f'\n{top}\n{side}\n{txt("This is a small testing project of weather app inside a terminal.")}\n{txt('This is app is still in beta, and you may encounter some bugs.')}\n{side}\n{top}')

    padding('type anything to exit: ')

def faq():
    '''
    FAQ page.
    '''
    top, side, width, = border()
    clear()

    print(f'\n{top}\n{side}')
    print(f'''{txt('Q: How do I get weather information using this application?')}
{txt('A: Select the "Weather" option from the menu, enter your city name when prompted,')}
{txt('and it will display the current weather information for that city.')}
{side}
{txt('Q: What should I do if the weather information is inaccurate or not updating?')}
{txt('A: If you notice inaccuracies or issues with the weather data, please open issue request on our github.')}
{txt('Our team will investigate and address the problem promptly.')}
{side}
{txt('Q: How can I contact customer support?')}
{txt('A: For support inquiries, please email us at support@example.com or')}
{txt('visit example.com/support to submit a support ticket.')}
{side}
{txt('Q: Can I suggest new features or improvements?')}
{txt('A: Yes! We welcome your suggestions and feedback. Please open pull request on out github.')}
{txt('Your feedback helps us improve our service.')}
{side}
{txt('Q: Is there a way to contribute or support the development of this application?')}
{txt('A: If you enjoy using our application, you can support us by buying us a coffee!')}
{txt('Select the "Buy me a coffee" option from the menu to learn more.')}
{txt('If you want to contribute to the project, start by creating pull request for new feature!')}
{side}
{txt('Q: How often is the weather data updated?')}
{txt('A: The weather data is updated regularly from reliable sources.')}
{txt('However, specific update frequencies may vary based on data sources and availability.')}
{side}
{txt('Q: Can I customize the settings or preferences in the application?')}
{txt('A: Currently, the application provides basic weather information.')}
{txt('We are working on adding customization features in future updates.')}
{side}
{txt('Q: Is the weather information provided reliable?')}
{txt('A: We strive to provide accurate and reliable weather information.')}
{txt('However, please note that weather forecasts are subject to change based on meteorological conditions.')}
{side}
{txt('Q: What platforms does this application support?')}
{txt('A: Our application is designed to run on various platforms, including Windows, macOS, and Linux.')}
{txt('Ensure you have Python installed to use it.')}
{side}
{txt('Q: How can I quit the application?')}
{txt('A: Select the "Quit" option from the menu to exit the application gracefully.')}
''')
    print(f'{side}\n{top}')
    padding('Type anything to exit: ')

def coffee():
    '''
    Buy coffee page.
    '''
    clear()
    borderText("If you enjoy using this program, consider supporting us at buymeacoffe.com/NiGu")
    padding('Type anything to exit: ')
    
