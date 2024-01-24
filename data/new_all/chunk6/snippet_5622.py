# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61617089/i-keep-getting-this-error-in-python3-typeerror-an-integer-is-required-got-typ
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(367630)

except ImportError:
    pass
try:
    from os import *
    _l_(367632)

except ImportError:
    pass

nameFile = _c_(367635, _n_(367633, "open", lambda: open), "Names.txt", _n_(367634, "O_APPEND", lambda: O_APPEND))
_l_(367636)
passwordFile = _c_(367639, _n_(367637, "open", lambda: open), "Passwords.txt", _n_(367638, "O_APPEND", lambda: O_APPEND))
_l_(367640)

def SignUp():
    _l_(367771)


    def storeData():
        _l_(367710)


        name = _c_(367643, _a_(367642, _n_(367641, "signupNameEntry", lambda: signupNameEntry), "get"))
        _l_(367644)
        password = _c_(367647, _a_(367646, _n_(367645, "signupPasswordEntry", lambda: signupPasswordEntry), "get"))
        _l_(367648)
        rpassword = _c_(367651, _a_(367650, _n_(367649, "signupRPasswordEntry", lambda: signupRPasswordEntry), "get"))
        _l_(367652)

        _c_(367655, _n_(367653, "print", lambda: print), _n_(367654, "name", lambda: name))
        _l_(367656)
        _c_(367659, _n_(367657, "print", lambda: print), _n_(367658, "password", lambda: password))
        _l_(367660)
        _c_(367663, _n_(367661, "print", lambda: print), _n_(367662, "rpassword", lambda: rpassword))
        _l_(367664)
        _c_(367669, _n_(367665, "print", lambda: print), _c_(367668, _n_(367666, "type", lambda: type), _n_(367667, "name", lambda: name)))
        _l_(367670)
        _c_(367675, _n_(367671, "print", lambda: print), _c_(367674, _n_(367672, "type", lambda: type), _n_(367673, "password", lambda: password)))
        _l_(367676)

        if _n_(367677, "password", lambda: password) == _n_(367678, "rpassword", lambda: rpassword):
            _l_(367709)

            _c_(367680, _n_(367679, "print", lambda: print), "passwords match")
            _l_(367681)
            nameFile = _c_(367683, _n_(367682, "open", lambda: open), "Names.txt", "a")
            _l_(367684)
            passwordFile = _c_(367686, _n_(367685, "open", lambda: open), "Passwords.txt", "a")
            _l_(367687)
            _c_(367691, _a_(367689, _n_(367688, "passwordFile", lambda: passwordFile), "write"), _n_(367690, "password", lambda: password))
            _l_(367692)
            _c_(367696, _a_(367694, _n_(367693, "nameFile", lambda: nameFile), "write"), _n_(367695, "name", lambda: name))
            _l_(367697)
            _c_(367700, _a_(367699, _n_(367698, "passwordFile", lambda: passwordFile), "close"))
            _l_(367701)
            _c_(367704, _a_(367703, _n_(367702, "nameFile", lambda: nameFile), "close"))
            _l_(367705)

        else:
            _c_(367707, _n_(367706, "print", lambda: print), "passwords don't match")
            _l_(367708)


    signup = _c_(367712, _n_(367711, "Toplevel", lambda: Toplevel))
    _l_(367713)
    _c_(367716, _a_(367715, _n_(367714, "signup", lambda: signup), "title"), "Sign Up")
    _l_(367717)

    _c_(367722, _a_(367721, _c_(367720, _n_(367718, "Label", lambda: Label), _n_(367719, "signup", lambda: signup), text="Name", pady=5, padx=5), "grid"), row=1, column=1)
    _l_(367723)
    _c_(367728, _a_(367727, _c_(367726, _n_(367724, "Label", lambda: Label), _n_(367725, "signup", lambda: signup), text="Password", pady=5, padx=5), "grid"), row=2, column=1)
    _l_(367729)
    _c_(367734, _a_(367733, _c_(367732, _n_(367730, "Label", lambda: Label), _n_(367731, "signup", lambda: signup), text="Repeat\nPassword"), "grid"), row=3, column=1)
    _l_(367735)
    signupNameEntry = _c_(367738, _n_(367736, "Entry", lambda: Entry), _n_(367737, "signup", lambda: signup))
    _l_(367739)
    _c_(367742, _a_(367741, _n_(367740, "signupNameEntry", lambda: signupNameEntry), "grid"), row=1, column=2)
    _l_(367743)
    signupPasswordEntry = _c_(367746, _n_(367744, "Entry", lambda: Entry), _n_(367745, "signup", lambda: signup))
    _l_(367747)
    _c_(367750, _a_(367749, _n_(367748, "signupPasswordEntry", lambda: signupPasswordEntry), "grid"), row=2, column=2)
    _l_(367751)
    signupRPasswordEntry = _c_(367754, _n_(367752, "Entry", lambda: Entry), _n_(367753, "signup", lambda: signup))
    _l_(367755)
    _c_(367758, _a_(367757, _n_(367756, "signupRPasswordEntry", lambda: signupRPasswordEntry), "grid"), row=3, column=2)
    _l_(367759)
    signupButton = _c_(367765, _a_(367764, _c_(367763, _n_(367760, "Button", lambda: Button), _n_(367761, "signup", lambda: signup), text="Sign Up", command=_n_(367762, "storeData", lambda: storeData), pady=5, padx=5), "grid"), row=4, column=2)
    _l_(367766)

    _c_(367769, _a_(367768, _n_(367767, "signup", lambda: signup), "mainloop"))
    _l_(367770)