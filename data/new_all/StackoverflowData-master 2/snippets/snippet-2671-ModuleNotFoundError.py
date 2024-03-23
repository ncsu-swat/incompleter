#Source: https://stackoverflow.com/questions/67318569/attributeerror-int-object-has-no-attribute-pack
from tkinter import *

# Window
window = Tk()
window.title('Minecraft Generator')
window.geometry("1080x600")
window.minsize(1080, 600)
window.maxsize(1080, 600)
window.iconbitmap('assets/img/logo.ico')

# Config
window.config(background='#627f1f')

#Composants

    # Main Menu Title
TITLE_FRAME = Frame(window, bg='#627f1f')
MAIN_MENU_TITLE = Label(TITLE_FRAME, text='Minecraft Generator' , font=("Courrier", 40), bg='#627f1f' , fg='white')
MAIN_MENU_SUBTITLE = Label(TITLE_FRAME, text='A Minecraft Generator for all needs !' , font=("Courrier", 15), bg='#627f1f' , fg='white')

    # Main Menu TellRaw
MAIN_MENU_TELLRAW_BUTTON = Button(TITLE_FRAME, text='Tellraw Command', bg='white' , fg='#627f1f' , font=("Courrier News", 15))
MAIN_MENU_TELLRAW_IMAGE = Canvas(window, width=157, height=100)
MAIN_MENU_TELLRAW_IMAGE = MAIN_MENU_TELLRAW_IMAGE.create_image((157, 100), image=PhotoImage(file='assets/img/tellraw_logo.png'))

# Packing

    # Title Frame
MAIN_MENU_TITLE.pack()
MAIN_MENU_SUBTITLE.pack()
TITLE_FRAME.pack(side='top')

    # TellRaw
MAIN_MENU_TELLRAW_BUTTON.pack(pady=25)
MAIN_MENU_TELLRAW_IMAGE.pack()

# Display Window
window.mainloop()