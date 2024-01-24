# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59810726/typeerror-after-cancel-takes-2-positional-arguments-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(671919)

except ImportError:
    pass
try:
    from time import sleep
    _l_(671921)

except ImportError:
    pass
try:
    import os
    _l_(671923)

except ImportError:
    pass
try:
    import sys
    _l_(671925)

except ImportError:
    pass
times1 = 0
_l_(671926)
times2 = 1
_l_(671927)
def quit_():
    _l_(671936)

    _c_(671930, _a_(671929, _n_(671928, "screen", lambda: screen), "destroy"))
    _l_(671931)
    _c_(671934, _a_(671933, _n_(671932, "sys", lambda: sys), "exit"))
    _l_(671935)
def run():
    _l_(671986)

    global times1
    _l_(671937)
    global times2
    _l_(671938)
    times1 += 1
    _l_(671939)
    bpm = _c_(671942, _a_(671941, _n_(671940, "bpm_", lambda: bpm_), "get"))
    _l_(671943)
    _c_(671947, _a_(671945, _n_(671944, "entry", lambda: entry), "delete"), 0, _n_(671946, "END", lambda: END))
    _l_(671948)
    bpm = _c_(671951, _n_(671949, "int", lambda: int), _n_(671950, "bpm", lambda: bpm))
    _l_(671952)
    bpm = _n_(671953, "bpm", lambda: bpm)/60
    _l_(671954)
    bpm = 1/_n_(671955, "bpm", lambda: bpm)
    _l_(671956)
    def run_():
        _l_(671982)

        global times1
        _l_(671957)
        global times2
        _l_(671958)
        _c_(671961, _n_(671959, "sleep", lambda: sleep), _n_(671960, "bpm", lambda: bpm))
        _l_(671962)
        _c_(671965, _a_(671964, _n_(671963, "os", lambda: os), "system"), "afplay metronome.wav&")
        _l_(671966)
        _c_(671970, _a_(671968, _n_(671967, "screen", lambda: screen), "after"), 1,_n_(671969, "run_", lambda: run_))
        _l_(671971)
        if _n_(671972, "times1", lambda: times1) > _n_(671973, "times2", lambda: times2):
            _l_(671981)

            _c_(671977, _a_(671975, _n_(671974, "screen", lambda: screen), "after_cancel"), 1,_n_(671976, "run_", lambda: run_))
            _l_(671978)
            times1 = 0
            _l_(671979)
            times2 = 1
            _l_(671980)
    _c_(671984, _n_(671983, "run_", lambda: run_))
    _l_(671985)
def main():
    _l_(672039)

    global bpm_
    _l_(671987)
    global entry
    _l_(671988)
    bpm_ = _c_(671990, _n_(671989, "StringVar", lambda: StringVar))
    _l_(671991)
    _c_(671996, _a_(671995, _c_(671994, _n_(671992, "Label", lambda: Label), _n_(671993, "screen", lambda: screen), text=""), "pack"))
    _l_(671997)
    _c_(672002, _a_(672001, _c_(672000, _n_(671998, "Label", lambda: Label), _n_(671999, "screen", lambda: screen), text = "enter a bpm"), "pack"))
    _l_(672003)
    entry = _c_(672007, _n_(672004, "Entry", lambda: Entry), _n_(672005, "screen", lambda: screen), textvariable=_n_(672006, "bpm_", lambda: bpm_))
    _l_(672008)
    _c_(672011, _a_(672010, _n_(672009, "entry", lambda: entry), "pack"))
    _l_(672012)
    _c_(672017, _a_(672016, _c_(672015, _n_(672013, "Label", lambda: Label), _n_(672014, "screen", lambda: screen), text=""), "pack"))
    _l_(672018)
    _c_(672024, _a_(672023, _c_(672022, _n_(672019, "Button", lambda: Button), _n_(672020, "screen", lambda: screen), text = "enter", command = _n_(672021, "run", lambda: run)), "pack"))
    _l_(672025)
    _c_(672030, _a_(672029, _c_(672028, _n_(672026, "Label", lambda: Label), _n_(672027, "screen", lambda: screen), text=""), "pack"))
    _l_(672031)
    _c_(672037, _a_(672036, _c_(672035, _n_(672032, "Button", lambda: Button), _n_(672033, "screen", lambda: screen), text = "quit", command = _n_(672034, "quit_", lambda: quit_)), "pack"))
    _l_(672038)
screen = _c_(672041, _n_(672040, "Tk", lambda: Tk))
_l_(672042)
_c_(672044, _n_(672043, "main", lambda: main))
_l_(672045)
_c_(672048, _a_(672047, _n_(672046, "screen", lambda: screen), "mainloop"))
_l_(672049)