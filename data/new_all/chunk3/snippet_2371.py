# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48040985/hexdigest-throws-typeerror-required-argument-length-pos-1-not-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import hashlib
    _l_(569728)

except ImportError:
    pass
try:
    import random
    _l_(569730)

except ImportError:
    pass


def dict_attack(pwds):
    _l_(569793)

    f = _c_(569732, _n_(569731, "open", lambda: open), 'Dictionary.txt', 'r')
    _l_(569733)
    words = _c_(569736, _a_(569735, _n_(569734, "f", lambda: f), "readlines"))
    _l_(569737)
    _c_(569740, _a_(569739, _n_(569738, "f", lambda: f), "close"))
    _l_(569741)
    cracked = []
    _l_(569742)
    for pwd in _n_(569743, "pwds", lambda: pwds):
        _l_(569779)

        for w in _n_(569744, "words", lambda: words):
            _l_(569778)

            word = _c_(569747, _a_(569746, _n_(569745, "w", lambda: w), "strip"), '\n')
            _l_(569748)
            word = _c_(569751, _a_(569750, _n_(569749, "word", lambda: word), "strip"), ' ')
            _l_(569752)
            hashed = _c_(569758, _a_(569754, _n_(569753, "hashlib", lambda: hashlib), "md5"), _c_(569757, _a_(569756, _n_(569755, "word", lambda: word), "encode")))
            _l_(569759)
            if _c_(569762, _a_(569761, _n_(569760, "hashed", lambda: hashed), "hexdigest")) == _n_(569763, "pwd", lambda: pwd):
                _l_(569777)

                _c_(569769, _n_(569764, "print", lambda: print), _c_(569768, _a_(569765, "[+] Found {} as {}, updating...", "format"), _n_(569766, "pwd", lambda: pwd), _n_(569767, "word", lambda: word)))
                _l_(569770)
                _c_(569774, _a_(569772, _n_(569771, "cracked", lambda: cracked), "append"), _n_(569773, "word", lambda: word))
                _l_(569775)
                break
                _l_(569776)
    _c_(569789, _n_(569780, "print", lambda: print), _c_(569788, _a_(569781, "[-] {}/{} passwords found!", "format"), _c_(569784, _n_(569782, "len", lambda: len), _n_(569783, "cracked", lambda: cracked)), _c_(569787, _n_(569785, "len", lambda: len), _n_(569786, "pwds", lambda: pwds))))
    _l_(569790)
    aux = _n_(569791, "cracked", lambda: cracked)
    _l_(569792)
    return aux

def main():
    _l_(569851)

    # To generate new ciphertext
    f = _c_(569795, _n_(569794, "open", lambda: open), 'Dictionary.txt', 'r')
    _l_(569796)
    words = _c_(569799, _a_(569798, _n_(569797, "f", lambda: f), "readlines"))
    _l_(569800)
    _c_(569803, _a_(569802, _n_(569801, "f", lambda: f), "close"))
    _l_(569804)
    for b in _c_(569806, _n_(569805, "range", lambda: range), 0, 10):
        _l_(569829)

        _c_(569813, _a_(569808, _n_(569807, "passwords", lambda: passwords), "append"), _c_(569812, _a_(569810, _n_(569809, "random", lambda: random), "choice"), _n_(569811, "words", lambda: words)))
        _l_(569814)
        _n_(569815, "passwords", lambda: passwords)[_n_(569816, "b", lambda: b)] = _c_(569820, _a_(569819, _n_(569817, "passwords", lambda: passwords)[_n_(569818, "b", lambda: b)], "strip"), '\n')
        _l_(569821)
        _n_(569822, "passwords", lambda: passwords)[_n_(569823, "b", lambda: b)] = _c_(569827, _a_(569826, _n_(569824, "passwords", lambda: passwords)[_n_(569825, "b", lambda: b)], "strip"), ' ')
        _l_(569828)
    hashed_passwords = []
    _l_(569830)
    for p in _n_(569831, "passwords", lambda: passwords):
        _l_(569844)

        _c_(569842, _a_(569833, _n_(569832, "hashed_passwords", lambda: hashed_passwords), "append"), _c_(569841, _a_(569840, _c_(569839, _a_(569835, _n_(569834, "hashlib", lambda: hashlib), "md5"), _c_(569838, _a_(569837, _n_(569836, "p", lambda: p), "encode"))), "hexdigest")))
        _l_(569843)
    #print(hashed_passwords)
    _c_(569849, _n_(569845, "print", lambda: print), _c_(569848, _n_(569846, "dict_attack", lambda: dict_attack), _n_(569847, "hashed_passwords", lambda: hashed_passwords)))
    _l_(569850)

_c_(569853, _n_(569852, "main", lambda: main))
_l_(569854)