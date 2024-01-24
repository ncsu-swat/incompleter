# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/26830872/attributeerror-function-object-has-no-attribute-upper
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(453894)

except ImportError:
    pass
try:
    import os.path
    _l_(453896)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(453898)

except ImportError:
    pass

def encode():
    _l_(454042)

    array = []
    _l_(453899)
    temp_array = []
    _l_(453900)
    i = 0
    _l_(453901)
    m = _a_(453903, _n_(453902, "message", lambda: message), "get")
    _l_(453904)
    m = _c_(453907, _a_(453906, _n_(453905, "m", lambda: m), "upper"))
    _l_(453908)
    _c_(453912, _a_(453910, _n_(453909, "array", lambda: array), "append"), _n_(453911, "m", lambda: m))
    _l_(453913)
    o = _c_(453916, _a_(453915, _n_(453914, "offset", lambda: offset), "get"))
    _l_(453917)
    _c_(453921, _a_(453919, _n_(453918, "array", lambda: array), "append"), _n_(453920, "o", lambda: o))
    _l_(453922)
    length = _c_(453925, _n_(453923, "len", lambda: len), _n_(453924, "array", lambda: array)[0])
    _l_(453926)
    while _n_(453927, "length", lambda: length) > _n_(453928, "i", lambda: i):
        _l_(453997)

        temp = _n_(453929, "array", lambda: array)[0][_n_(453930, "i", lambda: i)]
        _l_(453931)
        if _n_(453932, "temp", lambda: temp) == " ":
            _l_(453996)

            _c_(453936, _a_(453934, _n_(453933, "temp_array", lambda: temp_array), "append"), _n_(453935, "temp", lambda: temp))
            _l_(453937)
            i = _n_(453938, "i", lambda: i) + 1
            _l_(453939)
        elif _n_(453940, "temp", lambda: temp) == ".":
            _l_(453995)

            _c_(453944, _a_(453942, _n_(453941, "temp_array", lambda: temp_array), "append"), _n_(453943, "temp", lambda: temp))
            _l_(453945)
            i = _n_(453946, "i", lambda: i) + 1
            _l_(453947)
        elif (_c_(453950, _n_(453948, "ord", lambda: ord), _n_(453949, "temp", lambda: temp)) + _n_(453951, "o", lambda: o)) <= 90 and (_c_(453954, _n_(453952, "ord", lambda: ord), _n_(453953, "temp", lambda: temp)) + _n_(453955, "o", lambda: o)) >= 65:
            _l_(453994)

            #print("Easy option")
            temp = _c_(453958, _n_(453956, "ord", lambda: ord), _n_(453957, "temp", lambda: temp))
            _l_(453959)
            temp = _n_(453960, "temp", lambda: temp) + _n_(453961, "o", lambda: o)
            _l_(453962)
            temp = _c_(453965, _n_(453963, "chr", lambda: chr), _n_(453964, "temp", lambda: temp))
            _l_(453966)
            _c_(453970, _a_(453968, _n_(453967, "temp_array", lambda: temp_array), "append"), _n_(453969, "temp", lambda: temp))
            _l_(453971)
            i = _n_(453972, "i", lambda: i) + 1
            _l_(453973)
        else:
            #print("Hard option")
            temp = _c_(453976, _n_(453974, "ord", lambda: ord), _n_(453975, "temp", lambda: temp))
            _l_(453977)
            temp = _n_(453978, "temp", lambda: temp) + _n_(453979, "o", lambda: o)
            _l_(453980)
            temp = (_n_(453981, "temp", lambda: temp) % 90) + 64
            _l_(453982)
            temp = _c_(453985, _n_(453983, "chr", lambda: chr), _n_(453984, "temp", lambda: temp))
            _l_(453986)
            _c_(453990, _a_(453988, _n_(453987, "temp_array", lambda: temp_array), "append"), _n_(453989, "temp", lambda: temp))
            _l_(453991)
            i = _n_(453992, "i", lambda: i) + 1
            _l_(453993)
    i = _n_(453998, "i", lambda: i) - 1
    _l_(453999)
    temp = _n_(454000, "temp_array", lambda: temp_array)[_n_(454001, "i", lambda: i)]
    _l_(454002)
    while _n_(454003, "i", lambda: i) > 0:
        _l_(454010)

        i = _n_(454004, "i", lambda: i) - 1
        _l_(454005)
        temp = _n_(454006, "temp_array", lambda: temp_array)[_n_(454007, "i", lambda: i)] + _n_(454008, "temp", lambda: temp) 
        _l_(454009) 
    _c_(454014, _a_(454012, _n_(454011, "array", lambda: array), "append"), _n_(454013, "temp", lambda: temp))
    _l_(454015)
    word = (_n_(454016, "array", lambda: array)[2])
    _l_(454017)
    _c_(454020, _n_(454018, "print", lambda: print), _n_(454019, "word", lambda: word))
    _l_(454021)
    my_file = _c_(454023, _n_(454022, "open", lambda: open), "messages.txt", "a") #Open the file messages or if it does not exist create it
    _l_(454024) #Open the file messages or if it does not exist create it
    for item in _n_(454025, "array", lambda: array):
        _l_(454037)

        _c_(454031, _a_(454027, _n_(454026, "my_file", lambda: my_file), "write"), _c_(454030, _n_(454028, "str", lambda: str), _n_(454029, "item", lambda: item)))    #Write them to file
        _l_(454032)    #Write them to file
        _c_(454035, _a_(454034, _n_(454033, "my_file", lambda: my_file), "write"), "\n")         #New line
        _l_(454036)         #New line
    _c_(454040, _a_(454039, _n_(454038, "my_file", lambda: my_file), "close"))                 #Close the file
    _l_(454041)                 #Close the file


gui = _c_(454044, _n_(454043, "Tk", lambda: Tk))
_l_(454045)

_c_(454048, _a_(454047, _n_(454046, "gui", lambda: gui), "title"), "Caesar Cypher Encoder")
_l_(454049)

_c_(454055, _a_(454054, _c_(454053, _n_(454050, "Button", lambda: Button), _n_(454051, "gui", lambda: gui), text="Encode", command=_n_(454052, "encode", lambda: encode)), "grid"), row = 3, column = 0)
_l_(454056)
_c_(454061, _a_(454060, _c_(454059, _n_(454057, "Label", lambda: Label), _n_(454058, "gui", lambda: gui), text = "Message"), "grid"), row = 1, column =0)
_l_(454062)
_c_(454067, _a_(454066, _c_(454065, _n_(454063, "Label", lambda: Label), _n_(454064, "gui", lambda: gui), text = "Offset"), "grid"), row = 1, column =1)
_l_(454068)
message = _c_(454071, _n_(454069, "Entry", lambda: Entry), _n_(454070, "gui", lambda: gui))
_l_(454072)
_c_(454075, _a_(454074, _n_(454073, "message", lambda: message), "grid"), row=2, column=0)
_l_(454076)
offset = _c_(454080, _n_(454077, "Scale", lambda: Scale), _n_(454078, "gui", lambda: gui), from_=1, to=25, orient=_n_(454079, "HORIZONTAL", lambda: HORIZONTAL))
_l_(454081)
_c_(454084, _a_(454083, _n_(454082, "offset", lambda: offset), "grid"), row=2, column=1)
_l_(454085)

_c_(454087, _n_(454086, "mainloop", lambda: mainloop))
_l_(454088)