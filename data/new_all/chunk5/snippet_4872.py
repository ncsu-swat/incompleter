# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44230925/python-typeerror-unhashable-type-image
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(673475)

except ImportError:
    pass
try:
    import pyautogui
    _l_(673477)

except ImportError:
    pass

#option = None

def main():
    _l_(673498)

    #find_notification()
    name_coords, reply_coords, text_coords = _c_(673479, _n_(673478, "set_message_coords", lambda: set_message_coords))
    _l_(673480)
    option = _c_(673483, _n_(673481, "read_message", lambda: read_message), _n_(673482, "text_coords", lambda: text_coords))
    _l_(673484)
    _c_(673488, _n_(673485, "player_id", lambda: player_id), _n_(673486, "name_coords", lambda: name_coords), _n_(673487, "option", lambda: option))
    _l_(673489)
    answer = _c_(673491, _n_(673490, "response", lambda: response))
    _l_(673492)
    _c_(673496, _n_(673493, "reply", lambda: reply), _n_(673494, "reply_coords", lambda: reply_coords), _n_(673495, "answer", lambda: answer))
    _l_(673497)


def find_notification():
    _l_(673519)

    while True:
        _l_(673518)

        image = _c_(673501, _a_(673500, _n_(673499, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), 'test.png', grayscale = False, confidence = .9)
        _l_(673502)
        _c_(673505, _n_(673503, "print", lambda: print), _n_(673504, "image", lambda: image))
        _l_(673506)
        if _n_(673507, "image", lambda: image) is not None:
            _l_(673517)

            _c_(673509, _n_(673508, "print", lambda: print), 'Found a waiting message')
            _l_(673510)
            _c_(673514, _a_(673512, _n_(673511, "pyautogui", lambda: pyautogui), "click"), _n_(673513, "image", lambda: image))
            _l_(673515)
            break
            _l_(673516)


def set_message_coords():
    _l_(673553)

    try:
        _l_(673531)

        imagex, imagey = _c_(673522, _a_(673521, _n_(673520, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), 'upper_right_message_corner.png', grayscale = True, confidence = .8)
        _l_(673523)

    except:
        _l_(673530)

        _c_(673525, _n_(673524, "print", lambda: print), 'ERROR I SHOULD BE FINDING "upper_right_message_corner.PNG" EXITING PROGRAM') 
        _l_(673526) 
        aux = ""
        _l_(673529)
        exit(aux)
    name_coords = (_n_(673532, "imagex", lambda: imagex) - 424), _n_(673533, "imagey", lambda: imagey), 378, 50 # The coords of where the players name would be
    _l_(673534) # The coords of where the players name would be
    _c_(673536, _n_(673535, "print", lambda: print), 'Found an open message')
    _l_(673537)
    _c_(673541, _n_(673538, "print", lambda: print), _n_(673539, "imagex", lambda: imagex), _n_(673540, "imagey", lambda: imagey))
    _l_(673542)

    reply_coords = (_n_(673543, "imagex", lambda: imagex) - 251), (_n_(673544, "imagey", lambda: imagey) + 255 ) # Coords of the reply button
    _l_(673545) # Coords of the reply button
    text_coords = (_n_(673546, "imagex", lambda: imagex) - 461), (_n_(673547, "imagey", lambda: imagey) + 45), 430, 45 # Coords of where a players possible response is
    _l_(673548) # Coords of where a players possible response is
    aux = _n_(673549, "name_coords", lambda: name_coords), _n_(673550, "reply_coords", lambda: reply_coords), _n_(673551, "text_coords", lambda: text_coords) # Returns all coord values to be used by other functions
    _l_(673552) # Returns all coord values to be used by other functions
    return aux # Returns all coord values to be used by other functions


def player_id(name_coords, option):
    _l_(673581)

    players = {} # Used to store players names and where in the response is
    _l_(673554) # Used to store players names and where in the response is

    name_image = _c_(673558, _a_(673556, _n_(673555, "pyautogui", lambda: pyautogui), "screenshot"), 'name_test.png', region = _n_(673557, "name_coords", lambda: name_coords)) # Names are screenshots 
    _l_(673559) # Names are screenshots 

    if _n_(673560, "name_image", lambda: name_image) not in _n_(673561, "players", lambda: players):
        _l_(673580)

        _c_(673563, _n_(673562, "print", lambda: print), "User was not previously found, adding to dictionary.")
        _l_(673564)
        _n_(673565, "players", lambda: players)[_n_(673566, "name_image", lambda: name_image)] = None
        _l_(673567)
    else:
        _c_(673569, _n_(673568, "print", lambda: print), "User is previous user.")
        _l_(673570)
        _n_(673571, "players", lambda: players)[_n_(673572, "name_image", lambda: name_image)] = _n_(673573, "players", lambda: players)[_n_(673574, "name_image", lambda: name_image)] + _n_(673575, "option", lambda: option)
        _l_(673576)
        aux = _n_(673577, "players", lambda: players)[_n_(673578, "name_image", lambda: name_image)]
        _l_(673579)
        return aux


def reply(reply_coords, response):
    _l_(673596)

    _c_(673585, _a_(673583, _n_(673582, "pyautogui", lambda: pyautogui), "click"), _n_(673584, "reply_coords", lambda: reply_coords))
    _l_(673586)
    _c_(673590, _a_(673588, _n_(673587, "pyautogui", lambda: pyautogui), "typewrite"), _n_(673589, "response", lambda: response))
    _l_(673591)
    _c_(673594, _a_(673593, _n_(673592, "pyautogui", lambda: pyautogui), "press"), 'enter')
    _l_(673595)


def read_message(text_coords):
    _l_(673667)

    if _c_(673600, _a_(673598, _n_(673597, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '1.png',region = _n_(673599, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673660)

        option = '1'
        _l_(673601)
    elif _c_(673605, _a_(673603, _n_(673602, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '2.png',region = _n_(673604, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673659)

        option = '2'
        _l_(673606)
    elif _c_(673610, _a_(673608, _n_(673607, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '3.png',region = _n_(673609, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673658)

        option = '3'
        _l_(673611)
    elif _c_(673615, _a_(673613, _n_(673612, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '4.png',region = _n_(673614, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673657)

        option = '4'
        _l_(673616)
    elif _c_(673620, _a_(673618, _n_(673617, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '5.png',region = _n_(673619, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673656)

        option = '5'
        _l_(673621)
    elif _c_(673625, _a_(673623, _n_(673622, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '6.png',region = _n_(673624, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673655)

        option = '6'
        _l_(673626)
    elif _c_(673630, _a_(673628, _n_(673627, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '7.png',region = _n_(673629, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673654)

        option = '7'
        _l_(673631)
    elif _c_(673635, _a_(673633, _n_(673632, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '8.png',region = _n_(673634, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673653)

        option = '8'
        _l_(673636)
    elif _c_(673640, _a_(673638, _n_(673637, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '9.png',region = _n_(673639, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673652)

        option = '9'
        _l_(673641)
    elif _c_(673645, _a_(673643, _n_(673642, "pyautogui", lambda: pyautogui), "locateCenterOnScreen"), '0.png',region = _n_(673644, "text_coords", lambda: text_coords),  confidence = .9, grayscale = True):
        _l_(673651)

        option = '0'
        _l_(673646)
    else:
        _c_(673648, _n_(673647, "print", lambda: print), 'ERROR CANT FIND DIGIT ANSWER')
        _l_(673649)
        option = None
        _l_(673650)
        #reply(reply_coords,'ERROR PLEASE ENTER A NUMBER RESPONSE!')
        #main()
    _c_(673663, _n_(673661, "print", lambda: print), _n_(673662, "option", lambda: option))
    _l_(673664)
    aux = _n_(673665, "option", lambda: option)
    _l_(673666)
    return aux


def response(option):
    _l_(673680)

    if _n_(673668, "option", lambda: option) == None:
        _l_(673679)

        aux = "Hello! I am bot made to answer your questions! PM the number for more options! 1: Bounties. 2: Bug Hunting. 3: Looting. 4: Farming."
        _l_(673669)
        return aux
    elif _n_(673670, "option", lambda: option) == '1':
        _l_(673678)

        aux = "The bounty quest allows you to hunt mobs for cash! Location: Castle, steward's room(to the right in the throne room) [PM 1 for specifics, PM 2 for TIPS, PM 3 for possible bounties]"
        _l_(673671)
        return aux
    elif _n_(673672, "option", lambda: option) == '12':
        _l_(673677)

        aux = '1. The bounty box will "drop"(stop following you, and will not pick up anything) after every kill/capture you get, and will require you to call it, or run over it to pick it up again. [PM 1 for more info, PM 9 to go back one level, PM 0 to reset choices]'
        _l_(673673)
        return aux
    elif _n_(673674, "option", lambda: option) == '13':
        _l_(673676)

        aux = '100 green blobs, 20 Lizardons, 75 Pyrats(as homage to the PQ I assume), 75 Rebel soldiers(regular green baddy), 60 dark blobs, 60 rats, 75 snakes, 75 bats, 75 bandits, 80 spiders, 50 archers, or 50 crabs. [PM 9 to go back one level, PM 0 to reset choices]'
        _l_(673675)
        return aux

_c_(673682, _n_(673681, "main", lambda: main))
_l_(673683)