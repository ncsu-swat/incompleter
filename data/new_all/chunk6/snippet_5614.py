# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61617089/i-keep-getting-this-error-in-python3-typeerror-an-integer-is-required-got-typ
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(340526)

except ImportError:
    pass
try:
    from os import *
    _l_(340528)

except ImportError:
    pass

nameFile = _c_(340531, _n_(340529, "open", lambda: open), "Names.txt", _n_(340530, "O_APPEND", lambda: O_APPEND))
_l_(340532)
passwordFile = _c_(340535, _n_(340533, "open", lambda: open), "Passwords.txt", _n_(340534, "O_APPEND", lambda: O_APPEND))
_l_(340536)

def SignUp():
    _l_(340667)


    def storeData():
        _l_(340606)


        name = _c_(340539, _a_(340538, _n_(340537, "signupNameEntry", lambda: signupNameEntry), "get"))
        _l_(340540)
        password = _c_(340543, _a_(340542, _n_(340541, "signupPasswordEntry", lambda: signupPasswordEntry), "get"))
        _l_(340544)
        rpassword = _c_(340547, _a_(340546, _n_(340545, "signupRPasswordEntry", lambda: signupRPasswordEntry), "get"))
        _l_(340548)

        _c_(340551, _n_(340549, "print", lambda: print), _n_(340550, "name", lambda: name))
        _l_(340552)
        _c_(340555, _n_(340553, "print", lambda: print), _n_(340554, "password", lambda: password))
        _l_(340556)
        _c_(340559, _n_(340557, "print", lambda: print), _n_(340558, "rpassword", lambda: rpassword))
        _l_(340560)
        _c_(340565, _n_(340561, "print", lambda: print), _c_(340564, _n_(340562, "type", lambda: type), _n_(340563, "name", lambda: name)))
        _l_(340566)
        _c_(340571, _n_(340567, "print", lambda: print), _c_(340570, _n_(340568, "type", lambda: type), _n_(340569, "password", lambda: password)))
        _l_(340572)

        if _n_(340573, "password", lambda: password) == _n_(340574, "rpassword", lambda: rpassword):
            _l_(340605)

            _c_(340576, _n_(340575, "print", lambda: print), "passwords match")
            _l_(340577)
            nameFile = _c_(340579, _n_(340578, "open", lambda: open), "Names.txt", "a")
            _l_(340580)
            passwordFile = _c_(340582, _n_(340581, "open", lambda: open), "Passwords.txt", "a")
            _l_(340583)
            _c_(340587, _a_(340585, _n_(340584, "passwordFile", lambda: passwordFile), "write"), _n_(340586, "password", lambda: password))
            _l_(340588)
            _c_(340592, _a_(340590, _n_(340589, "nameFile", lambda: nameFile), "write"), _n_(340591, "name", lambda: name))
            _l_(340593)
            _c_(340596, _a_(340595, _n_(340594, "passwordFile", lambda: passwordFile), "close"))
            _l_(340597)
            _c_(340600, _a_(340599, _n_(340598, "nameFile", lambda: nameFile), "close"))
            _l_(340601)

        else:
            _c_(340603, _n_(340602, "print", lambda: print), "passwords don't match")
            _l_(340604)


    signup = _c_(340608, _n_(340607, "Toplevel", lambda: Toplevel))
    _l_(340609)
    _c_(340612, _a_(340611, _n_(340610, "signup", lambda: signup), "title"), "Sign Up")
    _l_(340613)

    _c_(340618, _a_(340617, _c_(340616, _n_(340614, "Label", lambda: Label), _n_(340615, "signup", lambda: signup), text="Name", pady=5, padx=5), "grid"), row=1, column=1)
    _l_(340619)
    _c_(340624, _a_(340623, _c_(340622, _n_(340620, "Label", lambda: Label), _n_(340621, "signup", lambda: signup), text="Password", pady=5, padx=5), "grid"), row=2, column=1)
    _l_(340625)
    _c_(340630, _a_(340629, _c_(340628, _n_(340626, "Label", lambda: Label), _n_(340627, "signup", lambda: signup), text="Repeat\nPassword"), "grid"), row=3, column=1)
    _l_(340631)
    signupNameEntry = _c_(340634, _n_(340632, "Entry", lambda: Entry), _n_(340633, "signup", lambda: signup))
    _l_(340635)
    _c_(340638, _a_(340637, _n_(340636, "signupNameEntry", lambda: signupNameEntry), "grid"), row=1, column=2)
    _l_(340639)
    signupPasswordEntry = _c_(340642, _n_(340640, "Entry", lambda: Entry), _n_(340641, "signup", lambda: signup))
    _l_(340643)
    _c_(340646, _a_(340645, _n_(340644, "signupPasswordEntry", lambda: signupPasswordEntry), "grid"), row=2, column=2)
    _l_(340647)
    signupRPasswordEntry = _c_(340650, _n_(340648, "Entry", lambda: Entry), _n_(340649, "signup", lambda: signup))
    _l_(340651)
    _c_(340654, _a_(340653, _n_(340652, "signupRPasswordEntry", lambda: signupRPasswordEntry), "grid"), row=3, column=2)
    _l_(340655)
    signupButton = _c_(340661, _a_(340660, _c_(340659, _n_(340656, "Button", lambda: Button), _n_(340657, "signup", lambda: signup), text="Sign Up", command=_n_(340658, "storeData", lambda: storeData), pady=5, padx=5), "grid"), row=4, column=2)
    _l_(340662)

    _c_(340665, _a_(340664, _n_(340663, "signup", lambda: signup), "mainloop"))
    _l_(340666)