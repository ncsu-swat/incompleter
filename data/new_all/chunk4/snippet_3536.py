# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72591020/i-am-trying-to-create-a-password-generator-and-i-keep-getting-this-error-typee
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(581051)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(581053)

except ImportError:
    pass
try:
    from typing import Tuple
    _l_(581055)

except ImportError:
    pass

root = _c_(581057, _n_(581056, "Tk", lambda: Tk))
_l_(581058)

input_box = _c_(581061, _n_(581059, "Entry", lambda: Entry), _n_(581060, "root", lambda: root), width=22, borderwidth=2, bg="#000000")
_l_(581062)
_c_(581065, _a_(581064, _n_(581063, "input_box", lambda: input_box), "grid"), row=0, column=0, columnspan=2)
_l_(581066)
_c_(581069, _a_(581068, _n_(581067, "input_box", lambda: input_box), "insert"), 0, 'Enter the password length:', )
_l_(581070)
random_password = ()
_l_(581071)

def password_generator():
    _l_(581098)

    character_list = ("""QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm
    1234567890`~!@#$%^&*()_+[]\{}|;':",./<>?""")
    _l_(581072)
    num_of_runs = 1
    _l_(581073)
    random_password = ()
    _l_(581074)
    password_length = _c_(581079, _n_(581075, "int", lambda: int), _c_(581078, _a_(581077, _n_(581076, "input_box", lambda: input_box), "get")))
    _l_(581080)
    while _n_(581081, "num_of_runs", lambda: num_of_runs) <= _c_(581084, _n_(581082, "int", lambda: int), _n_(581083, "password_length", lambda: password_length)):
        _l_(581091)

        random_password += _n_(581085, "character_list", lambda: character_list)[_c_(581088, _a_(581087, _n_(581086, "random", lambda: random), "randint"), 0, 91)]
        _l_(581089)
        num_of_runs += 1
        _l_(581090)
    _c_(581096, _a_(581095, _c_(581094, _n_(581092, "Label", lambda: Label), _n_(581093, "random_password", lambda: random_password)), "grid"), row=2, column=0)
    _l_(581097)


my_button = _c_(581102, _n_(581099, "Button", lambda: Button), _n_(581100, "root", lambda: root), text="Click here for your password", 
               command=_n_(581101, "password_generator", lambda: password_generator), fg="#000000", bg="white", )
_l_(581103)
_c_(581106, _a_(581105, _n_(581104, "my_button", lambda: my_button), "grid"), row=1, column=0, columnspan=2)
_l_(581107)

_c_(581110, _a_(581109, _n_(581108, "root", lambda: root), "mainloop"))
_l_(581111)