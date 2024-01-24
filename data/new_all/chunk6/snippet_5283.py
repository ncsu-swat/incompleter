# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73700748/nameerror-name-check-balance-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class tree():
    _l_(364919)

    def __init__(self,a=None,lc=None,rc=None):
        _l_(364860)

        _n_(364837, "self", lambda: self).label=_n_(364838, "a", lambda: a)
        _l_(364839)
        _n_(364840, "self", lambda: self).lt=_n_(364841, "lc", lambda: lc)
        _l_(364842)
        _n_(364843, "self", lambda: self).rt=_n_(364844, "rc", lambda: rc)
        _l_(364845)
        if _n_(364846, "a", lambda: a) is not None:
            _l_(364859)

            if _n_(364847, "lc", lambda: lc) is None:
                _l_(364852)

                _n_(364848, "self", lambda: self).lt=_c_(364850, _n_(364849, "tree", lambda: tree))
                _l_(364851)
            if _n_(364853, "rc", lambda: rc) is None:
                _l_(364858)

                _n_(364854, "self", lambda: self).rt=_c_(364856, _n_(364855, "tree", lambda: tree))
                _l_(364857)

    def getLabel(self):
        _l_(364864)

        aux = _a_(364862, _n_(364861, "self", lambda: self), "label")
        _l_(364863)
        return aux

    def isEmpty(self):
        _l_(364868)

        aux = _a_(364866, _n_(364865, "self", lambda: self), "label") is None
        _l_(364867)
        return aux

    def isLeaf(self):
        _l_(364878)

        aux = (_c_(364872, _a_(364871, _a_(364870, _n_(364869, "self", lambda: self), "lt"), "isEmpty")) and _c_(364876, _a_(364875, _a_(364874, _n_(364873, "self", lambda: self), "rt"), "isEmpty")))
        _l_(364877)
        return aux

    def getLc(self):
        _l_(364882)

        aux = _a_(364880, _n_(364879, "self", lambda: self), "lt")
        _l_(364881)
        return aux

    def getRc(self):
        _l_(364886)

        aux = _a_(364884, _n_(364883, "self", lambda: self), "rt")
        _l_(364885)
        return aux
    
    def check_balance(t):
        _l_(364918)

        if _c_(364889, _a_(364888, _n_(364887, "t", lambda: t), "isLeaf")) or _c_(364892, _a_(364891, _n_(364890, "t", lambda: t), "isEmpty")):
            _l_(364894)

            aux = True
            _l_(364893)
            return aux
        if _c_(364899, _a_(364898, _c_(364897, _a_(364896, _n_(364895, "t", lambda: t), "getLc")), "isEmpty")) or _c_(364904, _a_(364903, _c_(364902, _a_(364901, _n_(364900, "t", lambda: t), "getRc")), "isEmpty")):
            _l_(364906)

            aux = False
            _l_(364905)
            return aux
        aux = _c_(364911, _n_(364907, "check_balance", lambda: check_balance), _c_(364910, _a_(364909, _n_(364908, "t", lambda: t), "getLc"))) and _c_(364916, _n_(364912, "check_balance", lambda: check_balance), _c_(364915, _a_(364914, _n_(364913, "t", lambda: t), "getRc")))
        _l_(364917)
        return aux

a = _c_(364933, _n_(364920, "tree", lambda: tree), 1, _c_(364926, _n_(364921, "tree", lambda: tree), 2, _c_(364923, _n_(364922, "tree", lambda: tree), 7), _c_(364925, _n_(364924, "tree", lambda: tree), 8)), _c_(364932, _n_(364927, "tree", lambda: tree), 3, _c_(364929, _n_(364928, "tree", lambda: tree), 7), _c_(364931, _n_(364930, "tree", lambda: tree))))
_l_(364934)
_c_(364939, _n_(364935, "print", lambda: print), _c_(364938, _n_(364936, "check_balance", lambda: check_balance), _n_(364937, "a", lambda: a)))
_l_(364940)