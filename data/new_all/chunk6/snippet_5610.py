# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61617089/i-keep-getting-this-error-in-python3-typeerror-an-integer-is-required-got-typ
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(337241)

except ImportError:
    pass
try:
    from os import *
    _l_(337243)

except ImportError:
    pass

nameFile = _c_(337246, _n_(337244, "open", lambda: open), "Names.txt", _n_(337245, "O_APPEND", lambda: O_APPEND))
_l_(337247)
passwordFile = _c_(337250, _n_(337248, "open", lambda: open), "Passwords.txt", _n_(337249, "O_APPEND", lambda: O_APPEND))
_l_(337251)

def SignUp():
    _l_(337382)


    def storeData():
        _l_(337321)


        name = _c_(337254, _a_(337253, _n_(337252, "signupNameEntry", lambda: signupNameEntry), "get"))
        _l_(337255)
        password = _c_(337258, _a_(337257, _n_(337256, "signupPasswordEntry", lambda: signupPasswordEntry), "get"))
        _l_(337259)
        rpassword = _c_(337262, _a_(337261, _n_(337260, "signupRPasswordEntry", lambda: signupRPasswordEntry), "get"))
        _l_(337263)

        _c_(337266, _n_(337264, "print", lambda: print), _n_(337265, "name", lambda: name))
        _l_(337267)
        _c_(337270, _n_(337268, "print", lambda: print), _n_(337269, "password", lambda: password))
        _l_(337271)
        _c_(337274, _n_(337272, "print", lambda: print), _n_(337273, "rpassword", lambda: rpassword))
        _l_(337275)
        _c_(337280, _n_(337276, "print", lambda: print), _c_(337279, _n_(337277, "type", lambda: type), _n_(337278, "name", lambda: name)))
        _l_(337281)
        _c_(337286, _n_(337282, "print", lambda: print), _c_(337285, _n_(337283, "type", lambda: type), _n_(337284, "password", lambda: password)))
        _l_(337287)

        if _n_(337288, "password", lambda: password) == _n_(337289, "rpassword", lambda: rpassword):
            _l_(337320)

            _c_(337291, _n_(337290, "print", lambda: print), "passwords match")
            _l_(337292)
            nameFile = _c_(337294, _n_(337293, "open", lambda: open), "Names.txt", "a")
            _l_(337295)
            passwordFile = _c_(337297, _n_(337296, "open", lambda: open), "Passwords.txt", "a")
            _l_(337298)
            _c_(337302, _a_(337300, _n_(337299, "passwordFile", lambda: passwordFile), "write"), _n_(337301, "password", lambda: password))
            _l_(337303)
            _c_(337307, _a_(337305, _n_(337304, "nameFile", lambda: nameFile), "write"), _n_(337306, "name", lambda: name))
            _l_(337308)
            _c_(337311, _a_(337310, _n_(337309, "passwordFile", lambda: passwordFile), "close"))
            _l_(337312)
            _c_(337315, _a_(337314, _n_(337313, "nameFile", lambda: nameFile), "close"))
            _l_(337316)

        else:
            _c_(337318, _n_(337317, "print", lambda: print), "passwords don't match")
            _l_(337319)


    signup = _c_(337323, _n_(337322, "Toplevel", lambda: Toplevel))
    _l_(337324)
    _c_(337327, _a_(337326, _n_(337325, "signup", lambda: signup), "title"), "Sign Up")
    _l_(337328)

    _c_(337333, _a_(337332, _c_(337331, _n_(337329, "Label", lambda: Label), _n_(337330, "signup", lambda: signup), text="Name", pady=5, padx=5), "grid"), row=1, column=1)
    _l_(337334)
    _c_(337339, _a_(337338, _c_(337337, _n_(337335, "Label", lambda: Label), _n_(337336, "signup", lambda: signup), text="Password", pady=5, padx=5), "grid"), row=2, column=1)
    _l_(337340)
    _c_(337345, _a_(337344, _c_(337343, _n_(337341, "Label", lambda: Label), _n_(337342, "signup", lambda: signup), text="Repeat\nPassword"), "grid"), row=3, column=1)
    _l_(337346)
    signupNameEntry = _c_(337349, _n_(337347, "Entry", lambda: Entry), _n_(337348, "signup", lambda: signup))
    _l_(337350)
    _c_(337353, _a_(337352, _n_(337351, "signupNameEntry", lambda: signupNameEntry), "grid"), row=1, column=2)
    _l_(337354)
    signupPasswordEntry = _c_(337357, _n_(337355, "Entry", lambda: Entry), _n_(337356, "signup", lambda: signup))
    _l_(337358)
    _c_(337361, _a_(337360, _n_(337359, "signupPasswordEntry", lambda: signupPasswordEntry), "grid"), row=2, column=2)
    _l_(337362)
    signupRPasswordEntry = _c_(337365, _n_(337363, "Entry", lambda: Entry), _n_(337364, "signup", lambda: signup))
    _l_(337366)
    _c_(337369, _a_(337368, _n_(337367, "signupRPasswordEntry", lambda: signupRPasswordEntry), "grid"), row=3, column=2)
    _l_(337370)
    signupButton = _c_(337376, _a_(337375, _c_(337374, _n_(337371, "Button", lambda: Button), _n_(337372, "signup", lambda: signup), text="Sign Up", command=_n_(337373, "storeData", lambda: storeData), pady=5, padx=5), "grid"), row=4, column=2)
    _l_(337377)

    _c_(337380, _a_(337379, _n_(337378, "signup", lambda: signup), "mainloop"))
    _l_(337381)