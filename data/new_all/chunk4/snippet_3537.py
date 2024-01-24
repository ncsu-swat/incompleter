# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72591020/i-am-trying-to-create-a-password-generator-and-i-keep-getting-this-error-typee
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(594299)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(594301)

except ImportError:
    pass
try:
    from typing import Tuple
    _l_(594303)

except ImportError:
    pass

root = _c_(594305, _n_(594304, "Tk", lambda: Tk))
_l_(594306)

input_box = _c_(594309, _n_(594307, "Entry", lambda: Entry), _n_(594308, "root", lambda: root), width=22, borderwidth=2, bg="#000000")
_l_(594310)
_c_(594313, _a_(594312, _n_(594311, "input_box", lambda: input_box), "grid"), row=0, column=0, columnspan=2)
_l_(594314)
_c_(594317, _a_(594316, _n_(594315, "input_box", lambda: input_box), "insert"), 0, 'Enter the password length:', )
_l_(594318)
random_password = ()
_l_(594319)

def password_generator():
    _l_(594346)

    character_list = ("""QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm
    1234567890`~!@#$%^&*()_+[]\{}|;':",./<>?""")
    _l_(594320)
    num_of_runs = 1
    _l_(594321)
    random_password = ()
    _l_(594322)
    password_length = _c_(594327, _n_(594323, "int", lambda: int), _c_(594326, _a_(594325, _n_(594324, "input_box", lambda: input_box), "get")))
    _l_(594328)
    while _n_(594329, "num_of_runs", lambda: num_of_runs) <= _c_(594332, _n_(594330, "int", lambda: int), _n_(594331, "password_length", lambda: password_length)):
        _l_(594339)

        random_password += _n_(594333, "character_list", lambda: character_list)[_c_(594336, _a_(594335, _n_(594334, "random", lambda: random), "randint"), 0, 91)]
        _l_(594337)
        num_of_runs += 1
        _l_(594338)
    _c_(594344, _a_(594343, _c_(594342, _n_(594340, "Label", lambda: Label), _n_(594341, "random_password", lambda: random_password)), "grid"), row=2, column=0)
    _l_(594345)


my_button = _c_(594350, _n_(594347, "Button", lambda: Button), _n_(594348, "root", lambda: root), text="Click here for your password", 
               command=_n_(594349, "password_generator", lambda: password_generator), fg="#000000", bg="white", )
_l_(594351)
_c_(594354, _a_(594353, _n_(594352, "my_button", lambda: my_button), "grid"), row=1, column=0, columnspan=2)
_l_(594355)

_c_(594358, _a_(594357, _n_(594356, "root", lambda: root), "mainloop"))
_l_(594359)