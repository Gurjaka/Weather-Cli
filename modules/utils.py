import os
import shutil

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
  
def term(n):
  width, height = shutil.get_terminal_size()
  
  if n == 'width':
    return width
  elif n == 'height':
    return height
  else:
    return False