# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72176562/getting-typeerror-insertstop-takes-0-positional-arguments-but-1-was-given-w
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(583886)

except ImportError:
    pass
try:
    import os
    _l_(583888)

except ImportError:
    pass
try:
    import sys
    _l_(583890)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(583892)

except ImportError:
    pass

# Creates the Tkinter form named "screen"
screen = _c_(583894, _n_(583893, "Tk", lambda: Tk))
_l_(583895)
_c_(583898, _a_(583897, _n_(583896, "screen", lambda: screen), "geometry"), "550x645")
_l_(583899)
_c_(583902, _a_(583901, _n_(583900, "screen", lambda: screen), "title"), "Test")
_l_(583903)
# Initialize frames
menuframe = _c_(583906, _n_(583904, "Frame", lambda: Frame), _n_(583905, "screen", lambda: screen),
                  height=60,width=600,bg="gray",pady=5)
_l_(583907)
inputframe = _c_(583910, _n_(583908, "Frame", lambda: Frame), _n_(583909, "screen", lambda: screen),
                   height=300,width=600,pady=5)
_l_(583911)
outputframe = _c_(583914, _n_(583912, "Frame", lambda: Frame), _n_(583913, "screen", lambda: screen),
                   height=290,width=600,pady=5)
_l_(583915)

# Packs the frames so they will display
_c_(583918, _a_(583917, _n_(583916, "menuframe", lambda: menuframe), "pack"))
_l_(583919)
_c_(583922, _a_(583921, _n_(583920, "inputframe", lambda: inputframe), "pack"))
_l_(583923)
_c_(583926, _a_(583925, _n_(583924, "outputframe", lambda: outputframe), "pack"))
_l_(583927)


#==STOPBOX==#

stopbox=_c_(583931, _n_(583928, "Text", lambda: Text), _n_(583929, "inputframe", lambda: inputframe),yscrollcommand=1,height= 10,width=20,
               padx=3,pady=3,relief=_n_(583930, "GROOVE", lambda: GROOVE),bg="gray79")
_l_(583932)
_c_(583935, _a_(583934, _n_(583933, "stopbox", lambda: stopbox), "place"), x=345, y=90)
_l_(583936)

def insertstop():
    _l_(583952)

    global stop_vanconv
    _l_(583937)
    stop_vanconv=_c_(583940, _a_(583939, _n_(583938, "stop_entry", lambda: stop_entry), "get"))
    _l_(583941)
    _c_(583946, _a_(583943, _n_(583942, "stopbox", lambda: stopbox), "insert"), _n_(583944, "END", lambda: END), _n_(583945, "stop_vanconv", lambda: stop_vanconv) + "\n")
    _l_(583947)
    _c_(583950, _a_(583949, _n_(583948, "stop_entry", lambda: stop_entry), "delete"), "0","end")
    _l_(583951)

stoplist_label = _c_(583955, _n_(583953, "Label", lambda: Label), _n_(583954, "inputframe", lambda: inputframe),
                       text="Type stop locations and press" + '\n' +
                       "the Add Stop button to insert a new stop.")
_l_(583956)
_c_(583959, _a_(583958, _n_(583957, "stoplist_label", lambda: stoplist_label), "place"), x=100, y=150)
_l_(583960)

stop_entry = _c_(583963, _n_(583961, "Entry", lambda: Entry), _n_(583962, "inputframe", lambda: inputframe),
                      textvariable = " ")
_l_(583964)
_c_(583967, _a_(583966, _n_(583965, "stop_entry", lambda: stop_entry), "place"), x=150, y=190)
_l_(583968)

addstopbutton = _c_(583972, _n_(583969, "Button", lambda: Button), _n_(583970, "inputframe", lambda: inputframe),text="Add Stop",padx=20,pady=0,
                       activebackground="darkslategray4",command=_n_(583971, "insertstop", lambda: insertstop))
_l_(583973)
_c_(583976, _a_(583975, _n_(583974, "addstopbutton", lambda: addstopbutton), "place"), x=160, y=220)
_l_(583977)

_c_(583981, _a_(583979, _n_(583978, "stop_entry", lambda: stop_entry), "bind"), '<Return>',_n_(583980, "insertstop", lambda: insertstop))
_l_(583982)

_c_(583985, _a_(583984, _n_(583983, "screen", lambda: screen), "mainloop"))
_l_(583986)