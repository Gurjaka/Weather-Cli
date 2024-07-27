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
  
def txt(text):
  top, side, width = border()

  # Calculate stuff
  text_length = len(text)
  total_padding = (width - text_length - 2)
  left_padding = total_padding // 2
  right_padding = total_padding - left_padding
  
  middle = f'|{" " * left_padding}{text}{" " * right_padding}|'
  if len(middle) < width:
      middle += ' ' * (width - len(middle))
  
  return middle

def border():
  width = term('width')
  top = '-' * width
  side = f'|{" " * (width - 2)}|'

  return top, side, width

def borderText(text):
  top, side, width = border()
  print(f'\n{top}\n{side}\n{txt(text)}\n{side}\n{top}')

def padding(text):
  top, side, width = border()

  text_length = len(text)
  total_padding = (width - text_length - 2)
  left_padding = total_padding // 2
  opt = input(f'{" "*left_padding}{text} ')

  return opt