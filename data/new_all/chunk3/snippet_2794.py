# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67488541/attributeerror-nonetype-object-has-no-attribute-terminate
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import RPi.GPIO as GPIO
    _l_(557649)

except ImportError:
    pass
try:
    from rpi_lcd import LCD
    _l_(557651)

except ImportError:
    pass
try:
    from time import sleep
    _l_(557653)

except ImportError:
    pass
try:
    import time
    _l_(557655)

except ImportError:
    pass
try:
    from multiprocessing import Process
    _l_(557657)

except ImportError:
    pass


# RPi setup
_c_(557662, _a_(557659, _n_(557658, "GPIO", lambda: GPIO), "setmode"), _a_(557661, _n_(557660, "GPIO", lambda: GPIO), "BCM"))
_l_(557663)
_c_(557666, _a_(557665, _n_(557664, "GPIO", lambda: GPIO), "setwarnings"), False)
_l_(557667)


# Button setup
_c_(557674, _a_(557669, _n_(557668, "GPIO", lambda: GPIO), "setup"), 17, _a_(557671, _n_(557670, "GPIO", lambda: GPIO), "IN"), pull_up_down=_a_(557673, _n_(557672, "GPIO", lambda: GPIO), "PUD_DOWN"))  # Yellow
_l_(557675)  # Yellow
_c_(557682, _a_(557677, _n_(557676, "GPIO", lambda: GPIO), "setup"), 27, _a_(557679, _n_(557678, "GPIO", lambda: GPIO), "IN"), pull_up_down=_a_(557681, _n_(557680, "GPIO", lambda: GPIO), "PUD_DOWN"))  # Blue
_l_(557683)  # Blue


# LCD setup
lcd = _c_(557685, _n_(557684, "LCD", lambda: LCD))
_l_(557686)


# Keypad setup
length = 6
_l_(557687)
col = [19, 13, 6, 5]
_l_(557688)
row = [21, 20, 16, 26]
_l_(557689)

for j in _c_(557691, _n_(557690, "range", lambda: range), 4):
    _l_(557706)

    _c_(557698, _a_(557693, _n_(557692, "GPIO", lambda: GPIO), "setup"), _n_(557694, "col", lambda: col)[_n_(557695, "j", lambda: j)], _a_(557697, _n_(557696, "GPIO", lambda: GPIO), "OUT"))
    _l_(557699)
    _c_(557704, _a_(557701, _n_(557700, "GPIO", lambda: GPIO), "output"), _n_(557702, "col", lambda: col)[_n_(557703, "j", lambda: j)], 1)
    _l_(557705)
for i in _c_(557708, _n_(557707, "range", lambda: range), 4):
    _l_(557719)

    _c_(557717, _a_(557710, _n_(557709, "GPIO", lambda: GPIO), "setup"), _n_(557711, "row", lambda: row)[_n_(557712, "i", lambda: i)], _a_(557714, _n_(557713, "GPIO", lambda: GPIO), "IN"), pull_up_down=_a_(557716, _n_(557715, "GPIO", lambda: GPIO), "PUD_UP"))
    _l_(557718)


# Password checker
def check_keypad(length):
    _l_(557779)

    col = [19, 13, 6, 5]
    _l_(557720)
    row = [21, 20, 16, 26]
    _l_(557721)

    matrix = [["1", "2", "3", "A"],
              ["4", "5", "6", "B"],
              ["7", "8", "9", "C"],
              ["*", "0", "#", "D"]]
    _l_(557722)
    result = ""
    _l_(557723)

    while True:
        _l_(557778)

        for j in _c_(557725, _n_(557724, "range", lambda: range), 4):
            _l_(557777)

            _c_(557730, _a_(557727, _n_(557726, "GPIO", lambda: GPIO), "output"), _n_(557728, "col", lambda: col)[_n_(557729, "j", lambda: j)], 0)
            _l_(557731)

            for i in _c_(557733, _n_(557732, "range", lambda: range), 4):
                _l_(557763)

                if _c_(557738, _a_(557735, _n_(557734, "GPIO", lambda: GPIO), "input"), _n_(557736, "row", lambda: row)[_n_(557737, "i", lambda: i)]) == 0:
                    _l_(557762)

                    _c_(557741, _a_(557740, _n_(557739, "time", lambda: time), "sleep"), 0.02)
                    _l_(557742)
                    result = _n_(557743, "result", lambda: result) + _n_(557744, "matrix", lambda: matrix)[_n_(557745, "i", lambda: i)][_n_(557746, "j", lambda: j)]
                    _l_(557747)
                    _c_(557750, _n_(557748, "print", lambda: print), _n_(557749, "result", lambda: result))
                    _l_(557751)
                    while _c_(557756, _a_(557753, _n_(557752, "GPIO", lambda: GPIO), "input"), _n_(557754, "row", lambda: row)[_n_(557755, "i", lambda: i)]) == 0:
                        _l_(557761)

                        _c_(557759, _a_(557758, _n_(557757, "time", lambda: time), "sleep"), 0.02)
                        _l_(557760)

            _c_(557768, _a_(557765, _n_(557764, "GPIO", lambda: GPIO), "output"), _n_(557766, "col", lambda: col)[_n_(557767, "j", lambda: j)], 1)
            _l_(557769)
            if _c_(557772, _n_(557770, "len", lambda: len), _n_(557771, "result", lambda: result)) >= _n_(557773, "length", lambda: length):
                _l_(557776)

                aux = _n_(557774, "result", lambda: result)
                _l_(557775)
                return aux


# Start sequence
def starter():
    _l_(557890)


    global password
    _l_(557780)
    x = 0
    _l_(557781)

    _c_(557784, _a_(557783, _n_(557782, "lcd", lambda: lcd), "text"), "Starting...", 1)
    _l_(557785)
    _c_(557787, _n_(557786, "sleep", lambda: sleep), 5)
    _l_(557788)
    _c_(557791, _a_(557790, _n_(557789, "lcd", lambda: lcd), "clear"))
    _l_(557792)
    _c_(557795, _a_(557794, _n_(557793, "lcd", lambda: lcd), "text"), "Input a password", 1)
    _l_(557796)

    matrix = [["1", "2", "3", "A"],
              ["4", "5", "6", "B"],
              ["7", "8", "9", "C"],
              ["*", "0", "#", "D"]]
    _l_(557797)
    passwordmaker = ""
    _l_(557798)

    while _n_(557799, "x", lambda: x) != 1:
        _l_(557864)

        _c_(557803, _a_(557801, _n_(557800, "lcd", lambda: lcd), "text"), _n_(557802, "passwordmaker", lambda: passwordmaker), 2)
        _l_(557804)
        for j in _c_(557806, _n_(557805, "range", lambda: range), 4):
            _l_(557847)

            _c_(557811, _a_(557808, _n_(557807, "GPIO", lambda: GPIO), "output"), _n_(557809, "col", lambda: col)[_n_(557810, "j", lambda: j)], 0)
            _l_(557812)

            for i in _c_(557814, _n_(557813, "range", lambda: range), 4):
                _l_(557840)

                if _c_(557819, _a_(557816, _n_(557815, "GPIO", lambda: GPIO), "input"), _n_(557817, "row", lambda: row)[_n_(557818, "i", lambda: i)]) == 0:
                    _l_(557839)

                    _c_(557822, _a_(557821, _n_(557820, "time", lambda: time), "sleep"), 0.02)
                    _l_(557823)
                    passwordmaker = _n_(557824, "passwordmaker", lambda: passwordmaker) + _n_(557825, "matrix", lambda: matrix)[_n_(557826, "i", lambda: i)][_n_(557827, "j", lambda: j)]
                    _l_(557828)
                    # print(passwordmaker)  # thingy
                    while _c_(557833, _a_(557830, _n_(557829, "GPIO", lambda: GPIO), "input"), _n_(557831, "row", lambda: row)[_n_(557832, "i", lambda: i)]) == 0:
                        _l_(557838)

                        _c_(557836, _a_(557835, _n_(557834, "time", lambda: time), "sleep"), 0.02)
                        _l_(557837)
            _c_(557845, _a_(557842, _n_(557841, "GPIO", lambda: GPIO), "output"), _n_(557843, "col", lambda: col)[_n_(557844, "j", lambda: j)], 1)
            _l_(557846)
        if _c_(557850, _n_(557848, "len", lambda: len), _n_(557849, "passwordmaker", lambda: passwordmaker)) == 6:
            _l_(557863)

            _c_(557854, _a_(557852, _n_(557851, "lcd", lambda: lcd), "text"), _n_(557853, "passwordmaker", lambda: passwordmaker), 2)
            _l_(557855)
            password = _n_(557856, "passwordmaker", lambda: passwordmaker)
            _l_(557857)
            _c_(557860, _n_(557858, "print", lambda: print), "Password - " + _n_(557859, "password", lambda: password))
            _l_(557861)
            x = 1
            _l_(557862)
    _c_(557866, _n_(557865, "sleep", lambda: sleep), 0.5)
    _l_(557867)
    _c_(557870, _a_(557869, _n_(557868, "lcd", lambda: lcd), "clear"))
    _l_(557871)
    _c_(557874, _a_(557873, _n_(557872, "lcd", lambda: lcd), "text"), "Initiating", 1)
    _l_(557875)
    _c_(557878, _a_(557877, _n_(557876, "lcd", lambda: lcd), "text"), "startup sequence", 2)
    _l_(557879)
    _c_(557881, _n_(557880, "sleep", lambda: sleep), 2)
    _l_(557882)
    _c_(557885, _a_(557884, _n_(557883, "lcd", lambda: lcd), "clear"))
    _l_(557886)
    _c_(557888, _n_(557887, "sleep", lambda: sleep), 0.5)
    _l_(557889)


# Timer
def timer():
    _l_(557922)


    timeA = 41  # 40 + 1
    _l_(557891)  # 40 + 1
    while _n_(557892, "timeA", lambda: timeA) != 0:
        _l_(557909)

        _c_(557894, _n_(557893, "sleep", lambda: sleep), 1)
        _l_(557895)
        timeA = _n_(557896, "timeA", lambda: timeA) - 1
        _l_(557897)
        _c_(557903, _a_(557899, _n_(557898, "lcd", lambda: lcd), "text"), _c_(557902, _n_(557900, "str", lambda: str), _n_(557901, "timeA", lambda: timeA)), 1)
        _l_(557904)
        _c_(557907, _n_(557905, "print", lambda: print), _n_(557906, "timeA", lambda: timeA))
        _l_(557908)
    _c_(557912, _a_(557911, _n_(557910, "p2", lambda: p2), "terminate"))
    _l_(557913)
    _c_(557916, _a_(557915, _n_(557914, "lcd", lambda: lcd), "clear"))
    _l_(557917)
    _c_(557920, _a_(557919, _n_(557918, "lcd", lambda: lcd), "text"), "Boom!", 1)
    _l_(557921)


# Code
def code():
    _l_(557985)


    y1 = 3  # Amount of tries
    _l_(557923)  # Amount of tries
    y2 = 0
    _l_(557924)

    for y in _c_(557926, _n_(557925, "range", lambda: range), 3):
        _l_(557949)


        # Password from keypad
        y1str = _c_(557929, _n_(557927, "str", lambda: str), _n_(557928, "y1", lambda: y1))
        _l_(557930)
        text = "( " + _n_(557931, "y1str", lambda: y1str) + " / 3 )"
        _l_(557932)
        _c_(557936, _a_(557934, _n_(557933, "lcd", lambda: lcd), "text"), _n_(557935, "text", lambda: text), 2)
        _l_(557937)
        result = _c_(557940, _n_(557938, "check_keypad", lambda: check_keypad), _n_(557939, "length", lambda: length))
        _l_(557941)
        y1 = _n_(557942, "y1", lambda: y1) - 1
        _l_(557943)

        # Password check
        if _n_(557944, "result", lambda: result) == _n_(557945, "password", lambda: password):
            _l_(557948)

            y2 = 1
            _l_(557946)
            break
            _l_(557947)

    # Correct password
    if _n_(557950, "y2", lambda: y2) == 1:
        _l_(557984)

        _c_(557953, _a_(557952, _n_(557951, "p1", lambda: p1), "terminate"))
        _l_(557954)
        _c_(557957, _a_(557956, _n_(557955, "lcd", lambda: lcd), "clear"))
        _l_(557958)
        _c_(557961, _a_(557960, _n_(557959, "lcd", lambda: lcd), "text"), "Deactivated", 1)
        _l_(557962)
        _c_(557964, _n_(557963, "sleep", lambda: sleep), 10)
        _l_(557965)

    # Incorrect password
    elif _n_(557966, "y1", lambda: y1) == 0 & _n_(557967, "y2", lambda: y2) == 0:
        _l_(557983)

        _c_(557970, _a_(557969, _n_(557968, "p1", lambda: p1), "terminate"))
        _l_(557971)
        _c_(557974, _a_(557973, _n_(557972, "lcd", lambda: lcd), "clear"))
        _l_(557975)
        _c_(557978, _a_(557977, _n_(557976, "lcd", lambda: lcd), "text"), "Boom!", 1)
        _l_(557979)
        _c_(557981, _n_(557980, "sleep", lambda: sleep), 10)
        _l_(557982)


# Multiprocessing setup
p1 = _c_(557988, _n_(557986, "Process", lambda: Process), target=_n_(557987, "timer", lambda: timer))
_l_(557989)
p2 = _c_(557992, _n_(557990, "Process", lambda: Process), target=_n_(557991, "code", lambda: code))
_l_(557993)


# Stuff
_c_(557995, _n_(557994, "starter", lambda: starter))
_l_(557996)
_c_(557999, _a_(557998, _n_(557997, "p1", lambda: p1), "start"))
_l_(558000)
_c_(558003, _a_(558002, _n_(558001, "p2", lambda: p2), "start"))
_l_(558004)