from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class ButtonBuild:
  def __init__(self):
    self.button = []
    
  def buildbutton(self,key,link):
    self.button.append([InlineKeyboardButton(text=key, url=link)])
  
  def subbutton(self,key,link):
    self.button.append([InlineKeyboardButton(text=key, callback_data=link)])
    
  def build_menu(self,buttons,n_cols,header_buttons=None,footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
  
  def build_menu2(self,buttons,n_cols,header_buttons=None,footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu
    