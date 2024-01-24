# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71490260/my-pyautogui-script-is-raising-typeerror-nonetype-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while _c_(600165, _a_(600164, _n_(600163, "keyboard", lambda: keyboard), "is_pressed"), 'q') == False:
    _l_(600199)


    pic = _c_(600168, _a_(600167, _n_(600166, "pyautogui", lambda: pyautogui), "screenshot"), region=(360,158,1900,1025))
    _l_(600169)

    width, height = _a_(600171, _n_(600170, "pic", lambda: pic), "size")
    _l_(600172)

    if _c_(600175, _a_(600174, _n_(600173, "pyautogui", lambda: pyautogui), "locateOnScreen"), 'greenlightning.png', region=(360,158,1900,1025), grayscale=True, confidence=0.8) != None:
        _l_(600198)

        lightningloc = _c_(600178, _a_(600177, _n_(600176, "pyautogui", lambda: pyautogui), "locateOnScreen"), 'greenlightning.png')
        _l_(600179)
        x = _n_(600180, "lightningloc", lambda: lightningloc)[0]
        _l_(600181)
        y = _n_(600182, "lightningloc", lambda: lightningloc)[1]
        _l_(600183)
        _c_(600188, _a_(600185, _n_(600184, "pyautogui", lambda: pyautogui), "click"), _n_(600186, "x", lambda: x), _n_(600187, "y", lambda: y) - 50)
        _l_(600189)
        _c_(600192, _a_(600191, _n_(600190, "time", lambda: time), "sleep"), 0.2)
        _l_(600193)
    else:
        _c_(600196, _a_(600195, _n_(600194, "time", lambda: time), "sleep"), 0.1)
        _l_(600197)