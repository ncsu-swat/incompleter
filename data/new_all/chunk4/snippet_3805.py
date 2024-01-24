# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67488541/attributeerror-nonetype-object-has-no-attribute-terminate
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import RPi.GPIO as GPIO
    _l_(635050)

except ImportError:
    pass
try:
    from rpi_lcd import LCD
    _l_(635052)

except ImportError:
    pass
try:
    from time import sleep
    _l_(635054)

except ImportError:
    pass
try:
    import time
    _l_(635056)

except ImportError:
    pass
try:
    from multiprocessing import Process
    _l_(635058)

except ImportError:
    pass


# RPi setup
_c_(635063, _a_(635060, _n_(635059, "GPIO", lambda: GPIO), "setmode"), _a_(635062, _n_(635061, "GPIO", lambda: GPIO), "BCM"))
_l_(635064)
_c_(635067, _a_(635066, _n_(635065, "GPIO", lambda: GPIO), "setwarnings"), False)
_l_(635068)


# Button setup
_c_(635075, _a_(635070, _n_(635069, "GPIO", lambda: GPIO), "setup"), 17, _a_(635072, _n_(635071, "GPIO", lambda: GPIO), "IN"), pull_up_down=_a_(635074, _n_(635073, "GPIO", lambda: GPIO), "PUD_DOWN"))  # Yellow
_l_(635076)  # Yellow
_c_(635083, _a_(635078, _n_(635077, "GPIO", lambda: GPIO), "setup"), 27, _a_(635080, _n_(635079, "GPIO", lambda: GPIO), "IN"), pull_up_down=_a_(635082, _n_(635081, "GPIO", lambda: GPIO), "PUD_DOWN"))  # Blue
_l_(635084)  # Blue


# LCD setup
lcd = _c_(635086, _n_(635085, "LCD", lambda: LCD))
_l_(635087)


# Keypad setup
length = 6
_l_(635088)
col = [19, 13, 6, 5]
_l_(635089)
row = [21, 20, 16, 26]
_l_(635090)

for j in _c_(635092, _n_(635091, "range", lambda: range), 4):
    _l_(635107)

    _c_(635099, _a_(635094, _n_(635093, "GPIO", lambda: GPIO), "setup"), _n_(635095, "col", lambda: col)[_n_(635096, "j", lambda: j)], _a_(635098, _n_(635097, "GPIO", lambda: GPIO), "OUT"))
    _l_(635100)
    _c_(635105, _a_(635102, _n_(635101, "GPIO", lambda: GPIO), "output"), _n_(635103, "col", lambda: col)[_n_(635104, "j", lambda: j)], 1)
    _l_(635106)
for i in _c_(635109, _n_(635108, "range", lambda: range), 4):
    _l_(635120)

    _c_(635118, _a_(635111, _n_(635110, "GPIO", lambda: GPIO), "setup"), _n_(635112, "row", lambda: row)[_n_(635113, "i", lambda: i)], _a_(635115, _n_(635114, "GPIO", lambda: GPIO), "IN"), pull_up_down=_a_(635117, _n_(635116, "GPIO", lambda: GPIO), "PUD_UP"))
    _l_(635119)


# Password checker
def check_keypad(length):
    _l_(635180)

    col = [19, 13, 6, 5]
    _l_(635121)
    row = [21, 20, 16, 26]
    _l_(635122)

    matrix = [["1", "2", "3", "A"],
              ["4", "5", "6", "B"],
              ["7", "8", "9", "C"],
              ["*", "0", "#", "D"]]
    _l_(635123)
    result = ""
    _l_(635124)

    while True:
        _l_(635179)

        for j in _c_(635126, _n_(635125, "range", lambda: range), 4):
            _l_(635178)

            _c_(635131, _a_(635128, _n_(635127, "GPIO", lambda: GPIO), "output"), _n_(635129, "col", lambda: col)[_n_(635130, "j", lambda: j)], 0)
            _l_(635132)

            for i in _c_(635134, _n_(635133, "range", lambda: range), 4):
                _l_(635164)

                if _c_(635139, _a_(635136, _n_(635135, "GPIO", lambda: GPIO), "input"), _n_(635137, "row", lambda: row)[_n_(635138, "i", lambda: i)]) == 0:
                    _l_(635163)

                    _c_(635142, _a_(635141, _n_(635140, "time", lambda: time), "sleep"), 0.02)
                    _l_(635143)
                    result = _n_(635144, "result", lambda: result) + _n_(635145, "matrix", lambda: matrix)[_n_(635146, "i", lambda: i)][_n_(635147, "j", lambda: j)]
                    _l_(635148)
                    _c_(635151, _n_(635149, "print", lambda: print), _n_(635150, "result", lambda: result))
                    _l_(635152)
                    while _c_(635157, _a_(635154, _n_(635153, "GPIO", lambda: GPIO), "input"), _n_(635155, "row", lambda: row)[_n_(635156, "i", lambda: i)]) == 0:
                        _l_(635162)

                        _c_(635160, _a_(635159, _n_(635158, "time", lambda: time), "sleep"), 0.02)
                        _l_(635161)

            _c_(635169, _a_(635166, _n_(635165, "GPIO", lambda: GPIO), "output"), _n_(635167, "col", lambda: col)[_n_(635168, "j", lambda: j)], 1)
            _l_(635170)
            if _c_(635173, _n_(635171, "len", lambda: len), _n_(635172, "result", lambda: result)) >= _n_(635174, "length", lambda: length):
                _l_(635177)

                aux = _n_(635175, "result", lambda: result)
                _l_(635176)
                return aux


# Start sequence
def starter():
    _l_(635291)


    global password
    _l_(635181)
    x = 0
    _l_(635182)

    _c_(635185, _a_(635184, _n_(635183, "lcd", lambda: lcd), "text"), "Starting...", 1)
    _l_(635186)
    _c_(635188, _n_(635187, "sleep", lambda: sleep), 5)
    _l_(635189)
    _c_(635192, _a_(635191, _n_(635190, "lcd", lambda: lcd), "clear"))
    _l_(635193)
    _c_(635196, _a_(635195, _n_(635194, "lcd", lambda: lcd), "text"), "Input a password", 1)
    _l_(635197)

    matrix = [["1", "2", "3", "A"],
              ["4", "5", "6", "B"],
              ["7", "8", "9", "C"],
              ["*", "0", "#", "D"]]
    _l_(635198)
    passwordmaker = ""
    _l_(635199)

    while _n_(635200, "x", lambda: x) != 1:
        _l_(635265)

        _c_(635204, _a_(635202, _n_(635201, "lcd", lambda: lcd), "text"), _n_(635203, "passwordmaker", lambda: passwordmaker), 2)
        _l_(635205)
        for j in _c_(635207, _n_(635206, "range", lambda: range), 4):
            _l_(635248)

            _c_(635212, _a_(635209, _n_(635208, "GPIO", lambda: GPIO), "output"), _n_(635210, "col", lambda: col)[_n_(635211, "j", lambda: j)], 0)
            _l_(635213)

            for i in _c_(635215, _n_(635214, "range", lambda: range), 4):
                _l_(635241)

                if _c_(635220, _a_(635217, _n_(635216, "GPIO", lambda: GPIO), "input"), _n_(635218, "row", lambda: row)[_n_(635219, "i", lambda: i)]) == 0:
                    _l_(635240)

                    _c_(635223, _a_(635222, _n_(635221, "time", lambda: time), "sleep"), 0.02)
                    _l_(635224)
                    passwordmaker = _n_(635225, "passwordmaker", lambda: passwordmaker) + _n_(635226, "matrix", lambda: matrix)[_n_(635227, "i", lambda: i)][_n_(635228, "j", lambda: j)]
                    _l_(635229)
                    # print(passwordmaker)  # thingy
                    while _c_(635234, _a_(635231, _n_(635230, "GPIO", lambda: GPIO), "input"), _n_(635232, "row", lambda: row)[_n_(635233, "i", lambda: i)]) == 0:
                        _l_(635239)

                        _c_(635237, _a_(635236, _n_(635235, "time", lambda: time), "sleep"), 0.02)
                        _l_(635238)
            _c_(635246, _a_(635243, _n_(635242, "GPIO", lambda: GPIO), "output"), _n_(635244, "col", lambda: col)[_n_(635245, "j", lambda: j)], 1)
            _l_(635247)
        if _c_(635251, _n_(635249, "len", lambda: len), _n_(635250, "passwordmaker", lambda: passwordmaker)) == 6:
            _l_(635264)

            _c_(635255, _a_(635253, _n_(635252, "lcd", lambda: lcd), "text"), _n_(635254, "passwordmaker", lambda: passwordmaker), 2)
            _l_(635256)
            password = _n_(635257, "passwordmaker", lambda: passwordmaker)
            _l_(635258)
            _c_(635261, _n_(635259, "print", lambda: print), "Password - " + _n_(635260, "password", lambda: password))
            _l_(635262)
            x = 1
            _l_(635263)
    _c_(635267, _n_(635266, "sleep", lambda: sleep), 0.5)
    _l_(635268)
    _c_(635271, _a_(635270, _n_(635269, "lcd", lambda: lcd), "clear"))
    _l_(635272)
    _c_(635275, _a_(635274, _n_(635273, "lcd", lambda: lcd), "text"), "Initiating", 1)
    _l_(635276)
    _c_(635279, _a_(635278, _n_(635277, "lcd", lambda: lcd), "text"), "startup sequence", 2)
    _l_(635280)
    _c_(635282, _n_(635281, "sleep", lambda: sleep), 2)
    _l_(635283)
    _c_(635286, _a_(635285, _n_(635284, "lcd", lambda: lcd), "clear"))
    _l_(635287)
    _c_(635289, _n_(635288, "sleep", lambda: sleep), 0.5)
    _l_(635290)


# Timer
def timer():
    _l_(635323)


    timeA = 41  # 40 + 1
    _l_(635292)  # 40 + 1
    while _n_(635293, "timeA", lambda: timeA) != 0:
        _l_(635310)

        _c_(635295, _n_(635294, "sleep", lambda: sleep), 1)
        _l_(635296)
        timeA = _n_(635297, "timeA", lambda: timeA) - 1
        _l_(635298)
        _c_(635304, _a_(635300, _n_(635299, "lcd", lambda: lcd), "text"), _c_(635303, _n_(635301, "str", lambda: str), _n_(635302, "timeA", lambda: timeA)), 1)
        _l_(635305)
        _c_(635308, _n_(635306, "print", lambda: print), _n_(635307, "timeA", lambda: timeA))
        _l_(635309)
    _c_(635313, _a_(635312, _n_(635311, "p2", lambda: p2), "terminate"))
    _l_(635314)
    _c_(635317, _a_(635316, _n_(635315, "lcd", lambda: lcd), "clear"))
    _l_(635318)
    _c_(635321, _a_(635320, _n_(635319, "lcd", lambda: lcd), "text"), "Boom!", 1)
    _l_(635322)


# Code
def code():
    _l_(635386)


    y1 = 3  # Amount of tries
    _l_(635324)  # Amount of tries
    y2 = 0
    _l_(635325)

    for y in _c_(635327, _n_(635326, "range", lambda: range), 3):
        _l_(635350)


        # Password from keypad
        y1str = _c_(635330, _n_(635328, "str", lambda: str), _n_(635329, "y1", lambda: y1))
        _l_(635331)
        text = "( " + _n_(635332, "y1str", lambda: y1str) + " / 3 )"
        _l_(635333)
        _c_(635337, _a_(635335, _n_(635334, "lcd", lambda: lcd), "text"), _n_(635336, "text", lambda: text), 2)
        _l_(635338)
        result = _c_(635341, _n_(635339, "check_keypad", lambda: check_keypad), _n_(635340, "length", lambda: length))
        _l_(635342)
        y1 = _n_(635343, "y1", lambda: y1) - 1
        _l_(635344)

        # Password check
        if _n_(635345, "result", lambda: result) == _n_(635346, "password", lambda: password):
            _l_(635349)

            y2 = 1
            _l_(635347)
            break
            _l_(635348)

    # Correct password
    if _n_(635351, "y2", lambda: y2) == 1:
        _l_(635385)

        _c_(635354, _a_(635353, _n_(635352, "p1", lambda: p1), "terminate"))
        _l_(635355)
        _c_(635358, _a_(635357, _n_(635356, "lcd", lambda: lcd), "clear"))
        _l_(635359)
        _c_(635362, _a_(635361, _n_(635360, "lcd", lambda: lcd), "text"), "Deactivated", 1)
        _l_(635363)
        _c_(635365, _n_(635364, "sleep", lambda: sleep), 10)
        _l_(635366)

    # Incorrect password
    elif _n_(635367, "y1", lambda: y1) == 0 & _n_(635368, "y2", lambda: y2) == 0:
        _l_(635384)

        _c_(635371, _a_(635370, _n_(635369, "p1", lambda: p1), "terminate"))
        _l_(635372)
        _c_(635375, _a_(635374, _n_(635373, "lcd", lambda: lcd), "clear"))
        _l_(635376)
        _c_(635379, _a_(635378, _n_(635377, "lcd", lambda: lcd), "text"), "Boom!", 1)
        _l_(635380)
        _c_(635382, _n_(635381, "sleep", lambda: sleep), 10)
        _l_(635383)


# Multiprocessing setup
p1 = _c_(635389, _n_(635387, "Process", lambda: Process), target=_n_(635388, "timer", lambda: timer))
_l_(635390)
p2 = _c_(635393, _n_(635391, "Process", lambda: Process), target=_n_(635392, "code", lambda: code))
_l_(635394)


# Stuff
_c_(635396, _n_(635395, "starter", lambda: starter))
_l_(635397)
_c_(635400, _a_(635399, _n_(635398, "p1", lambda: p1), "start"))
_l_(635401)
_c_(635404, _a_(635403, _n_(635402, "p2", lambda: p2), "start"))
_l_(635405)