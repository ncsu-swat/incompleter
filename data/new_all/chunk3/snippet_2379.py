# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47389828/attribute-error-when-using-popen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(541169)

except ImportError:
    pass
try:
    import RPi.GPIO as GPIO
    _l_(541171)

except ImportError:
    pass
try:
    import time
    _l_(541173)

except ImportError:
    pass
try:
    import sys
    _l_(541175)

except ImportError:
    pass
try:
    import subprocess
    _l_(541177)

except ImportError:
    pass

_c_(541180, _a_(541179, _n_(541178, "os", lambda: os), "system"), 'raspistill -o image.jpg -w 1280 -h 1024')
_l_(541181)
x = _c_(541184, _a_(541183, _n_(541182, "os", lambda: os), "system"), 'cp image.jpg /home/pi/face_recognition/face_recognition/unknown/unknown.jpg')
_l_(541185)
_c_(541188, _n_(541186, "print", lambda: print), _n_(541187, "x", lambda: x))
_l_(541189)

process = _c_(541192, _a_(541191, _n_(541190, "subprocess", lambda: subprocess), "Popen"), 'python3 cli.py known unknown | cut -d "," -f2', shell=True)
_l_(541193)
_c_(541196, _a_(541195, _n_(541194, "process", lambda: process), "wait"))
_l_(541197)
output = _c_(541200, _a_(541199, _n_(541198, "process", lambda: process), "check_output"))
_l_(541201)
_c_(541204, _n_(541202, "print", lambda: print), _n_(541203, "output", lambda: output))
_l_(541205)

if _n_(541206, "output", lambda: output) == b'unknown_person\n':
    _l_(541283)

    _c_(541211, _a_(541208, _n_(541207, "GPIO", lambda: GPIO), "setmode"), _a_(541210, _n_(541209, "GPIO", lambda: GPIO), "BCM"))
    _l_(541212)
    _c_(541215, _a_(541214, _n_(541213, "GPIO", lambda: GPIO), "setwarnings"), False)
    _l_(541216)
    _c_(541221, _a_(541218, _n_(541217, "GPIO", lambda: GPIO), "setup"), 18,_a_(541220, _n_(541219, "GPIO", lambda: GPIO), "OUT"))
    _l_(541222)
    _c_(541224, _n_(541223, "print", lambda: print), "Red LED on")
    _l_(541225)
    _c_(541230, _a_(541227, _n_(541226, "GPIO", lambda: GPIO), "output"), 18,_a_(541229, _n_(541228, "GPIO", lambda: GPIO), "HIGH"))
    _l_(541231)
    _c_(541234, _a_(541233, _n_(541232, "time", lambda: time), "sleep"), 3)
    _l_(541235)
    _c_(541237, _n_(541236, "print", lambda: print), "Red LED off")
    _l_(541238)
    _c_(541243, _a_(541240, _n_(541239, "GPIO", lambda: GPIO), "output"), 18,_a_(541242, _n_(541241, "GPIO", lambda: GPIO), "LOW"))
    _l_(541244)
else:
    _c_(541249, _a_(541246, _n_(541245, "GPIO", lambda: GPIO), "setmode"), _a_(541248, _n_(541247, "GPIO", lambda: GPIO), "BCM"))
    _l_(541250)
    _c_(541253, _a_(541252, _n_(541251, "GPIO", lambda: GPIO), "setwarnings"), False)
    _l_(541254)
    _c_(541259, _a_(541256, _n_(541255, "GPIO", lambda: GPIO), "setup"), 17,_a_(541258, _n_(541257, "GPIO", lambda: GPIO), "OUT"))
    _l_(541260)
    _c_(541262, _n_(541261, "print", lambda: print), "Green LED on")
    _l_(541263)
    _c_(541268, _a_(541265, _n_(541264, "GPIO", lambda: GPIO), "output"), 17,_a_(541267, _n_(541266, "GPIO", lambda: GPIO), "HIGH"))
    _l_(541269)
    _c_(541272, _a_(541271, _n_(541270, "time", lambda: time), "sleep"), 3)
    _l_(541273)
    _c_(541275, _n_(541274, "print", lambda: print), "Green LED off")
    _l_(541276)
    _c_(541281, _a_(541278, _n_(541277, "GPIO", lambda: GPIO), "output"), 17,_a_(541280, _n_(541279, "GPIO", lambda: GPIO), "LOW"))
    _l_(541282)