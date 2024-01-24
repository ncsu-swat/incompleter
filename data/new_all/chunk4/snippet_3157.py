# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36404680/nameerror-name-is-not-defined-for-user-input
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class user:
    _l_(614809)

    def __init__(self, usrName, pWord):
        _l_(614782)

        _n_(614776, "self", lambda: self).usrName = _n_(614777, "usrName", lambda: usrName)
        _l_(614778)
        _n_(614779, "self", lambda: self).pWord = _n_(614780, "pWord", lambda: pWord)
        _l_(614781)

    def createUsrPw(self):
        _l_(614808)

        f = _c_(614784, _n_(614783, "open", lambda: open), "usrName.txt", "a")
        _l_(614785)
        _c_(614789, _a_(614787, _n_(614786, "f", lambda: f), "write"), _n_(614788, "usrName", lambda: usrName))
        _l_(614790)
        _c_(614793, _a_(614792, _n_(614791, "f", lambda: f), "write"), "   ")
        _l_(614794)
        _c_(614798, _a_(614796, _n_(614795, "f", lambda: f), "write"), _n_(614797, "pWord", lambda: pWord))
        _l_(614799)
        _c_(614802, _a_(614801, _n_(614800, "f", lambda: f), "write"), "\n")
        _l_(614803)
        _c_(614806, _a_(614805, _n_(614804, "f", lambda: f), "close"))
        _l_(614807)


usr1 = _c_(614811, _n_(614810, "user", lambda: user), "Ben", "testPw")
_l_(614812)

_c_(614815, _a_(614814, _n_(614813, "usr1", lambda: usr1), "createUsrPw"))
_l_(614816)