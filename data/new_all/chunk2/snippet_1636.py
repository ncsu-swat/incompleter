# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68574816/how-to-resolve-error-for-i-in-rangelenval-typeerror-object-of-type-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from time import sleep
    _l_(471527)

except ImportError:
    pass
try:
    import numpy as np
    _l_(471529)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(471531)

except ImportError:
    pass
try:
    from selenium.webdriver.common.keys import Keys
    _l_(471533)

except ImportError:
    pass

options = _c_(471536, _a_(471535, _n_(471534, "webdriver", lambda: webdriver), "ChromeOptions"))
_l_(471537)
_c_(471540, _a_(471539, _n_(471538, "options", lambda: options), "add_argument"), "user-data-dir=C:\\Users\\saksh\\Desktop\\codeing\\Projects\\Connect 4\\chrome profiles\\chrome profile - 1")
_l_(471541)
browser = _c_(471545, _a_(471543, _n_(471542, "webdriver", lambda: webdriver), "Chrome"), options =  _n_(471544, "options", lambda: options) , executable_path = r"C:\Users\saksh\Desktop\codeing\imported items\chromedriver v-90.exe")
_l_(471546)


ROW_COUNT = 6
_l_(471547)
COLUMN_COUNT = 7
_l_(471548)

def create_board():
    _l_(471557)

    board = _c_(471553, _a_(471550, _n_(471549, "np", lambda: np), "zeros"), (_n_(471551, "ROW_COUNT", lambda: ROW_COUNT), _n_(471552, "COLUMN_COUNT", lambda: COLUMN_COUNT)))
    _l_(471554)
    aux = _n_(471555, "board", lambda: board)
    _l_(471556)

    return aux


def send_board(board):
    _l_(471577)

    board = _c_(471563, _n_(471558, "str", lambda: str), _c_(471562, _a_(471560, _n_(471559, "np", lambda: np), "flip"), _n_(471561, "board", lambda: board), 0))
    _l_(471564)
    board  = _c_(471567, _a_(471566, _n_(471565, "board", lambda: board), "replace"), "0", "🔳")
    _l_(471568)
    board = _c_(471571, _a_(471570, _n_(471569, "board", lambda: board), "replace"), "1", "🟢")
    _l_(471572)
    board =  _c_(471575, _a_(471574, _n_(471573, "board", lambda: board), "replace"), "2", "⚫")
    _l_(471576)

board = _c_(471579, _n_(471578, "create_board", lambda: create_board))
_l_(471580)


def sendMessage(message , browser):
    _l_(471594)

    message_box = _c_(471583, _a_(471582, _n_(471581, "browser", lambda: browser), "find_element_by_css_selector"), ".ItkAi > textarea:nth-child(1)")
    _l_(471584)
    _c_(471588, _a_(471586, _n_(471585, "message_box", lambda: message_box), "send_keys"), _n_(471587, "message", lambda: message))
    _l_(471589)
    _a_(471592, _a_(471591, _n_(471590, "message_box", lambda: message_box), "Keys"), "ENTER") 
    _l_(471593) 

# manually go u any instagram dm 
# manually go u any instagram dm 
_c_(471596, _n_(471595, "print", lambda: print), "manually go u any instagram dm , and press enter") 
_l_(471597) 

_c_(471599, _n_(471598, "input", lambda: input), "press enter !!")
_l_(471600)

_c_(471602, _n_(471601, "sleep", lambda: sleep), 5)
_l_(471603)

_c_(471609, _n_(471604, "sendMessage", lambda: sendMessage), _c_(471607, _n_(471605, "send_board", lambda: send_board), _n_(471606, "board", lambda: board)) , _n_(471608, "browser", lambda: browser))
_l_(471610)