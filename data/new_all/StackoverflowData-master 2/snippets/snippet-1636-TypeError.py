#Source: https://stackoverflow.com/questions/68574816/how-to-resolve-error-for-i-in-rangelenval-typeerror-object-of-type-none
from time import sleep
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\saksh\\Desktop\\codeing\\Projects\\Connect 4\\chrome profiles\\chrome profile - 1")
browser = webdriver.Chrome(options =  options , executable_path = r"C:\Users\saksh\Desktop\codeing\imported items\chromedriver v-90.exe")


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))

    return board


def send_board(board):
    board = str(np.flip(board, 0))
    board  = board.replace("0", "🔳")
    board = board.replace("1", "🟢")
    board =  board.replace("2", "⚫")
    

board = create_board()


def sendMessage(message , browser):
    message_box = browser.find_element_by_css_selector(".ItkAi > textarea:nth-child(1)")
    message_box.send_keys(message)
    message_box.Keys.ENTER 

# manually go u any instagram dm 
# manually go u any instagram dm 
print("manually go u any instagram dm , and press enter") 

input("press enter !!")

sleep(5)

sendMessage(send_board(board) , browser)