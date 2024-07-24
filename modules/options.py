import sys
from modules.utils import *
from simple_term_menu import TerminalMenu

def support():
    clear()
    print("Welcome to the support section. Support Mail : Weatherapp@gmail.com\n")
    print("How can we assist you today?\n")
    options = ["1) The weather app is not accurate or not working.", "2) Other bugs.",
    "3) Suggest other improvements."]
    
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    opt = options[menu_entry_index]
    
    if opt == '1) The weather app is not accurate or not working.':
        print("If there are any issues with the weather app or it's accuracy report it to the support mail written above")
    elif opt == '2) Other bugs.':
        print("If there are any bugs you want to report, report it to the support mail written above. ")    
    elif opt == '3) Suggest other improvements.':
        print("If there is anything you want to suggest us, suggest it to the support mail written above.")  

def aboutus():
    print("This is a small testing project of weather app inside a terminal.\nThis is still in working and you may encounter some bugs.")

def faq():
    print("""
Q: How do I get weather information using this application?
A: Select the "Weather" option from the menu, enter your city name when prompted,
and it will display the current weather information for that city.

Q: What should I do if the weather information is inaccurate or not updating?
A: If you notice inaccuracies or issues with the weather data, please report them to weather@gmail.com.
Our team will investigate and address the problem promptly.

Q: How can I contact customer support?
A: For support inquiries, please email us at support@example.com or 
visit example.com/support to submit a support ticket.

Q: Can I suggest new features or improvements?
A: Yes! We welcome your suggestions and feedback. Please email your ideas to suggestions@example.com.
Your input helps us improve our service.

Q: Is there a way to contribute or support the development of this application?
A: If you enjoy using our application, you can support us by buying us a coffee!
Select the "Buy me a coffee" option from the menu to learn more.

Q: How often is the weather data updated?
A: The weather data is updated regularly from reliable sources.
However, specific update frequencies may vary based on data sources and availability.

Q: Can I customize the settings or preferences in the application?
A: Currently, the application provides basic weather information. 
We are working on adding customization features in future updates.

Q: Is the weather information provided reliable?
A: We strive to provide accurate and reliable weather information.
However, please note that weather forecasts are subject to change based on meteorological conditions.

Q: What platforms does this application support?
A: Our application is designed to run on various platforms, including Windows, macOS, and Linux. 
Ensure you have Python installed to use it.

Q: How can I quit the application?
A: Select the "Quit" option from the menu to exit the application gracefully.
""")

def coffee():
    print("If you enjoy using this program, consider supporting us by buying a coffee at buymeacoffe.com/NiGu")

    
