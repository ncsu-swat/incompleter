# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46989736/class-def-self-attributeerror-xx-object-has-no-attribute-xx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import hashlib
    _l_(601683)

except ImportError:
    pass
class Sicherheit:
    _l_(601830)

    passwordFile = 'usercreds.tmp'
    _l_(601684)
    def Signup(self):
        _l_(601753)

        _n_(601685, "self", lambda: self).isSigned = False # !!! self.isSigned
        _l_(601686) # !!! self.isSigned
        _c_(601688, _n_(601687, "print", lambda: print), "Sie müssen sich erst anmelden!\n")
        _l_(601689)
        usernameInput = _c_(601691, _n_(601690, "input", lambda: input), "Bitte geben Sie Ihren Nutzername ein: \n")
        _l_(601692)
        passwordInput = _c_(601694, _n_(601693, "input", lambda: input), "Bitte geben Sie Ihr Passwort ein: \n")
        _l_(601695)
        usernameInputHashed = _c_(601701, _a_(601697, _n_(601696, "hashlib", lambda: hashlib), "sha512"), _c_(601700, _a_(601699, _n_(601698, "usernameInput", lambda: usernameInput), "encode")))
        _l_(601702)
        passwordInputHashed = _c_(601708, _a_(601704, _n_(601703, "hashlib", lambda: hashlib), "sha512"), _c_(601707, _a_(601706, _n_(601705, "passwordInput", lambda: passwordInput), "encode")))
        _l_(601709)

        with _c_(601713, _n_(601710, "open", lambda: open), _a_(601712, _n_(601711, "self", lambda: self), "passwordFile"), 'w') as f:
            _l_(601740)

            _c_(601721, _a_(601715, _n_(601714, "f", lambda: f), "write"), _c_(601720, _n_(601716, "str", lambda: str), _c_(601719, _a_(601718, _n_(601717, "usernameInputHashed", lambda: usernameInputHashed), "hexdigest"))))
            _l_(601722)
            _c_(601725, _a_(601724, _n_(601723, "f", lambda: f), "write"), '\n')
            _l_(601726)
            _c_(601734, _a_(601728, _n_(601727, "f", lambda: f), "write"), _c_(601733, _n_(601729, "str", lambda: str), _c_(601732, _a_(601731, _n_(601730, "passwordInputHashed", lambda: passwordInputHashed), "hexdigest"))))
            _l_(601735)
            _c_(601738, _a_(601737, _n_(601736, "f", lambda: f), "close"))
            _l_(601739)

        _n_(601741, "self", lambda: self).isSigned = True  # !!! self.isSigned
        _l_(601742)  # !!! self.isSigned
        _c_(601744, _n_(601743, "print", lambda: print), "Anmeldung war erfolgreich!\n")
        _l_(601745)
        _c_(601747, _n_(601746, "print", lambda: print), "======================================================\n")
        _l_(601748)
        _c_(601751, _a_(601750, _n_(601749, "self", lambda: self), "Login"))  # Moves onto the login def
        _l_(601752)  # Moves onto the login def

    def Login(self):
        _l_(601817)

        _c_(601755, _n_(601754, "print", lambda: print), "Sie müssen sich einloggen!\n")
        _l_(601756)

        usernameEntry = _c_(601758, _n_(601757, "input", lambda: input), "Bitte geben Sie Ihren Nutzername ein: \n")
        _l_(601759)
        passwordEntry = _c_(601761, _n_(601760, "input", lambda: input), "Bitte geben Sie Ihr Passwort ein: \n")
        _l_(601762)
        usernameEntry = _c_(601768, _a_(601764, _n_(601763, "hashlib", lambda: hashlib), "sha512"), _c_(601767, _a_(601766, _n_(601765, "usernameEntry", lambda: usernameEntry), "encode")))
        _l_(601769)
        passwordEntry = _c_(601775, _a_(601771, _n_(601770, "hashlib", lambda: hashlib), "sha512"), _c_(601774, _a_(601773, _n_(601772, "passwordEntry", lambda: passwordEntry), "encode")))
        _l_(601776)
        usernameEntryHashed = _c_(601779, _a_(601778, _n_(601777, "usernameEntry", lambda: usernameEntry), "hexdigest"))
        _l_(601780)
        passwordEntryHashed = _c_(601783, _a_(601782, _n_(601781, "passwordEntry", lambda: passwordEntry), "hexdigest"))
        _l_(601784)

        with _c_(601788, _n_(601785, "open", lambda: open), _a_(601787, _n_(601786, "self", lambda: self), "passwordFile")) as r:
            _l_(601801)

            info = _c_(601791, _a_(601790, _n_(601789, "r", lambda: r), "readlines"))
            _l_(601792)
            usernameInFile = _c_(601795, _a_(601794, _n_(601793, "info", lambda: info)[0], "rstrip"))
            _l_(601796)
            passwordInFile = _c_(601799, _a_(601798, _n_(601797, "info", lambda: info)[1], "rstrip"))
            _l_(601800)

        if _n_(601802, "usernameEntryHashed", lambda: usernameEntryHashed) == _n_(601803, "usernameInFile", lambda: usernameInFile) and _n_(601804, "passwordEntryHashed", lambda: passwordEntryHashed) == _n_(601805, "passwordInFile", lambda: passwordInFile):
            _l_(601816)

            _c_(601807, _n_(601806, "print", lambda: print), "Anmeldung war erfolgreich!\n")
            _l_(601808)

        else:
            _c_(601810, _n_(601809, "print", lambda: print), "Anmeldung war nicht erfolgreich!!!\n")
            _l_(601811)
            _c_(601814, _a_(601813, _n_(601812, "self", lambda: self), "Login"))
            _l_(601815)

    def CheckSign(self):
        _l_(601829)

        if _a_(601819, _n_(601818, "self", lambda: self), "isSigned") == True:
            _l_(601828)

            _c_(601822, _a_(601821, _n_(601820, "self", lambda: self), "Login"))
            _l_(601823)
        else:
            _c_(601826, _a_(601825, _n_(601824, "self", lambda: self), "Signup"))
            _l_(601827)
Kontrolle = _c_(601832, _n_(601831, "Sicherheit", lambda: Sicherheit))
_l_(601833)
_c_(601836, _a_(601835, _n_(601834, "Kontrolle", lambda: Kontrolle), "CheckSign"))
_l_(601837)