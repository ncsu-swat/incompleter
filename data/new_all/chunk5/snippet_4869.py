# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44230925/python-typeerror-unhashable-type-image
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(649360)

except ImportError:
    pass
try:
    import pyautogui
    _l_(649362)

except ImportError:
    pass

#option = None

def main():
    _l_(649383)

    #find_notification()
    name_coords, reply_coords, text_coords = _c_(649364, _n_(649363, "set_message_coords", lambda: set_message_coords))
    _l_(649365)
    option = _c_(649368, _n_(649366, "read_message", lambda: read_message), _n_(649367, "text_coords", lambda: text_coords))
    _l_(649369)
    _c_(649373, _n_(649370, "player_id", lambda: player_id), _n_(649371, "name_coords", lambda: name_coords), _n_(649372, "option", lambda: option))
    _l_(649374)
    answer = _c_(649376, _n_(649375, "response", lambda: response))
    _l_(649377)
    _c_(649381, _n_(649378, "reply", lambda: reply), _n_(649379, "reply_coords", lambda: reply_coords), _n_(649380, "answer", lambda: answer))
    _l_(649382)


def find_notification():
    _l_(649404)

    while True:
        _l_(649403)

        image = _c_(649386, _a_(649385, _n_(649384, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), 'test.png', grayscale = False, confidence = .9)
        _l_(649387)
        _c_(649390, _n_(649388, "print", lambda: print), _n_(649389, "image", lambda: image))
        _l_(649391)
        if _n_(649392, "image", lambda: image) is not None:
            _l_(649402)

            _c_(649394, _n_(649393, "print", lambda: print), 'Found a waiting message')
            _l_(649395)
            _c_(649399, _a_(649397, _n_(649396, "pyautogui", lambda: pyautogui), "click"), _n_(649398, "image", lambda: image))
            _l_(649400)
            break
            _l_(649401)


def set_message_coords():
    _l_(649438)

    try:
        _l_(649416)

        imagex, imagey = _c_(649407, _a_(649406, _n_(649405, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), 'upper_right_message_corner.png', grayscale = True, confidence = .8)
        _l_(649408)

    except:
        _l_(649415)

        _c_(649410, _n_(649409, "print", lambda: print), 'ERROR I SHOULD BE FINDING "upper_right_message_corner.PNG" EXITING PROGRAM') 
        _l_(649411) 
        aux = ""
        _l_(649414)
        exit(aux)
    name_coords = (_n_(649417, "imagex", lambda: imagex) - 424), _n_(649418, "imagey", lambda: imagey), 378, 50 # The coords of where the players name would be
    _l_(649419) # The coords of where the players name would be
    _c_(649421, _n_(649420, "print", lambda: print), 'Found an open message')
    _l_(649422)
    _c_(649426, _n_(649423, "print", lambda: print), _n_(649424, "imagex", lambda: imagex), _n_(649425, "imagey", lambda: imagey))
    _l_(649427)

    reply_coords = (_n_(649428, "imagex", lambda: imagex) - 251), (_n_(649429, "imagey", lambda: imagey) + 255 ) # Coords of the reply button
    _l_(649430) # Coords of the reply button
    text_coords = (_n_(649431, "imagex", lambda: imagex) - 461), (_n_(649432, "imagey", lambda: imagey) + 45), 430, 45 # Coords of where a players possible response is
    _l_(649433) # Coords of where a players possible response is
    aux = _n_(649434, "name_coords", lambda: name_coords), _n_(649435, "reply_coords", lambda: reply_coords), _n_(649436, "text_coords", lambda: text_coords) # Returns all coord values to be used by other functions
    _l_(649437) # Returns all coord values to be used by other functions
    return aux # Returns all coord values to be used by other functions


def player_id(name_coords, option):
    _l_(649466)

    players = {} # Used to store players names and where in the response is
    _l_(649439) # Used to store players names and where in the response is

    name_image = _c_(649443, _a_(649441, _n_(649440, "pyautogui", lambda: pyautogui), "screenshot"), 'name_test.png', region = _n_(649442, "name_coords", lambda: name_coords)) # Names are screenshots 
    _l_(649444) # Names are screenshots 

    if _n_(649445, "name_image", lambda: name_image) not in _n_(649446, "players", lambda: players):
        _l_(649465)

        _c_(649448, _n_(649447, "print", lambda: print), "User was not previously found, adding to dictionary.")
        _l_(649449)
        _n_(649450, "players", lambda: players)[_n_(649451, "name_image", lambda: name_image)] = None
        _l_(649452)
    else:
        _c_(649454, _n_(649453, "print", lambda: print), "User is previous user.")
        _l_(649455)
        _n_(649456, "players", lambda: players)[_n_(649457, "name_image", lambda: name_image)] = _n_(649458, "players", lambda: players)[_n_(649459, "name_image", lambda: name_image)] + _n_(649460, "option", lambda: option)
        _l_(649461)
        aux = _n_(649462, "players", lambda: players)[_n_(649463, "name_image", lambda: name_image)]
        _l_(649464)
        return aux


def reply(reply_coords, response):
    _l_(649481)

    _c_(649470, _a_(649468, _n_(649467, "pyautogui", lambda: pyautogui), "click"), _n_(649469, "reply_coords", lambda: reply_coords))
    _l_(649471)
    _c_(649475, _a_(649473, _n_(649472, "pyautogui", lambda: pyautogui), "typewrite"), _n_(649474, "response", lambda: response))
    _l_(649476)
    _c_(649479, _a_(649478, _n_(649477, "pyautogui", lambda: pyautogui), "press"), 'enter')
    _l_(649480)


def read_message(text_coords):
    _l_(649552)

    if _c_(649485, _a_(649483, _n_(649482, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '1.png',region = _n_(649484, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649545)

        option = '1'
        _l_(649486)
    elif _c_(649490, _a_(649488, _n_(649487, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '2.png',region = _n_(649489, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649544)

        option = '2'
        _l_(649491)
    elif _c_(649495, _a_(649493, _n_(649492, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '3.png',region = _n_(649494, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649543)

        option = '3'
        _l_(649496)
    elif _c_(649500, _a_(649498, _n_(649497, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '4.png',region = _n_(649499, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649542)

        option = '4'
        _l_(649501)
    elif _c_(649505, _a_(649503, _n_(649502, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '5.png',region = _n_(649504, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649541)

        option = '5'
        _l_(649506)
    elif _c_(649510, _a_(649508, _n_(649507, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '6.png',region = _n_(649509, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649540)

        option = '6'
        _l_(649511)
    elif _c_(649515, _a_(649513, _n_(649512, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '7.png',region = _n_(649514, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649539)

        option = '7'
        _l_(649516)
    elif _c_(649520, _a_(649518, _n_(649517, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '8.png',region = _n_(649519, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649538)

        option = '8'
        _l_(649521)
    elif _c_(649525, _a_(649523, _n_(649522, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '9.png',region = _n_(649524, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649537)

        option = '9'
        _l_(649526)
    elif _c_(649530, _a_(649528, _n_(649527, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '0.png',region = _n_(649529, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(649536)

        option = '0'
        _l_(649531)
    else:
        _c_(649533, _n_(649532, "print", lambda: print), 'ERROR CANT FIND DIGIT ANSWER')
        _l_(649534)
        option = None
        _l_(649535)
        #reply(reply_coords,'ERROR PLEASE ENTER A NUMBER RESPONSE!')
        #main()
    _c_(649548, _n_(649546, "print", lambda: print), _n_(649547, "option", lambda: option))
    _l_(649549)
    aux = _n_(649550, "option", lambda: option)
    _l_(649551)
    return aux


def response(option):
    _l_(649565)

    if _n_(649553, "option", lambda: option) == None:
        _l_(649564)

        aux = "Hello! I am bot made to answer your questions! PM the number for more options! 1: Bounties. 2: Bug Hunting. 3: Looting. 4: Farming."
        _l_(649554)
        return aux
    elif _n_(649555, "option", lambda: option) == '1':
        _l_(649563)

        aux = "The bounty quest allows you to hunt mobs for cash! Location: Castle, steward's room(to the right in the throne room) [PM 1 for specifics, PM 2 for TIPS, PM 3 for possible bounties]"
        _l_(649556)
        return aux
    elif _n_(649557, "option", lambda: option) == '12':
        _l_(649562)

        aux = '1. The bounty box will "drop"(stop following you, and will not pick up anything) after every kill/capture you get, and will require you to call it, or run over it to pick it up again. [PM 1 for more info, PM 9 to go back one level, PM 0 to reset choices]'
        _l_(649558)
        return aux
    elif _n_(649559, "option", lambda: option) == '13':
        _l_(649561)

        aux = '100 green blobs, 20 Lizardons, 75 Pyrats(as homage to the PQ I assume), 75 Rebel soldiers(regular green baddy), 60 dark blobs, 60 rats, 75 snakes, 75 bats, 75 bandits, 80 spiders, 50 archers, or 50 crabs. [PM 9 to go back one level, PM 0 to reset choices]'
        _l_(649560)
        return aux

_c_(649567, _n_(649566, "main", lambda: main))
_l_(649568)