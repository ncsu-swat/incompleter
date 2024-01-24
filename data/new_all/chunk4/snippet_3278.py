# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76245831/how-do-i-resolve-error-nameerror-name-stream-is-not-defined-pyaudio-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import RPi.GPIO as GPIO
    _l_(580099)

except ImportError:
    pass
# ... (other imports)

# Define global variable 'stream'
stream = None
_l_(580100)

# ... (other code)

def on_turn(pin):
    _l_(580112)

    global paused
    _l_(580101)
    global stream
    _l_(580102)

    if _n_(580103, "stream", lambda: stream) is not None and _c_(580106, _a_(580105, _n_(580104, "stream", lambda: stream), "is_active")):
        _l_(580111)

        _c_(580108, _n_(580107, "print", lambda: print), 'Audio skipped')
        _l_(580109)
        paused = False
        _l_(580110)

# ... (other code)

_c_(580118, _a_(580114, _n_(580113, "GPIO", lambda: GPIO), "add_event_detect"), 27, _a_(580116, _n_(580115, "GPIO", lambda: GPIO), "BOTH"), callback=_n_(580117, "on_turn", lambda: on_turn), bouncetime=200)
_l_(580119)

# ... (rest of the code)