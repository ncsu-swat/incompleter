# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/12541370/typeerror-encoding-is-an-invalid-keyword-argument-for-this-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(413627)

    import tkinter as tk
    _l_(413620)
    from tkinter import *
    _l_(413621)
except:
    _l_(413626)

    try:
        import Tkinter as tk
        _l_(413623)

    except ImportError:
        pass
    try:
        from Tkinter import *
        _l_(413625)

    except ImportError:
        pass
try:
    import time
    _l_(413629)

except ImportError:
    pass
try:
    import sys
    _l_(413631)

except ImportError:
    pass
try:
    import os
    _l_(413633)

except ImportError:
    pass
try:
    import random
    _l_(413635)

except ImportError:
    pass

flashcards = {}
_l_(413636)


def Flashcards(key, trans, PoS):
    _l_(413681)

    if not _n_(413637, "key", lambda: key) in _n_(413638, "flashcards", lambda: flashcards):
        _l_(413680)

        _n_(413639, "flashcards", lambda: flashcards)[_n_(413640, "key", lambda: key)] = [[_n_(413641, "trans", lambda: trans)], [_n_(413642, "PoS", lambda: PoS)]]
        _l_(413643)
    else:
        x = []
        _l_(413644)
        for item in _n_(413645, "flashcards", lambda: flashcards)[_n_(413646, "key", lambda: key)][0]:
            _l_(413652)

            _c_(413650, _a_(413648, _n_(413647, "x", lambda: x), "append"), _n_(413649, "item", lambda: item))
            _l_(413651)
        _c_(413656, _a_(413654, _n_(413653, "x", lambda: x), "append"), _n_(413655, "trans", lambda: trans))
        _l_(413657)
        _n_(413658, "flashcards", lambda: flashcards)[_n_(413659, "key", lambda: key)][0] = _n_(413660, "x", lambda: x)
        _l_(413661)
        x = []
        _l_(413662)
        for item in _n_(413663, "flashcards", lambda: flashcards)[_n_(413664, "key", lambda: key)][1]:
            _l_(413670)

            _c_(413668, _a_(413666, _n_(413665, "x", lambda: x), "append"), _n_(413667, "item", lambda: item))
            _l_(413669)
        _c_(413674, _a_(413672, _n_(413671, "x", lambda: x), "append"), _n_(413673, "PoS", lambda: PoS))
        _l_(413675)
        _n_(413676, "flashcards", lambda: flashcards)[_n_(413677, "key", lambda: key)][1] = _n_(413678, "x", lambda: x)
        _l_(413679)


def ImportGaeilge():
    _l_(413706)

    flashcards = {}
    _l_(413682)
    with _c_(413684, _n_(413683, "open", lambda: open), 'gaeilge_flashcard_mode.txt','r', encoding='utf8') as file:
        _l_(413705)

        for line in _n_(413685, "file", lambda: file):
            _l_(413704)

            line1 = _c_(413690, _a_(413689, _c_(413688, _a_(413687, _n_(413686, "line", lambda: line), "rstrip")), "split"), "=")
            _l_(413691)
            key = _n_(413692, "line1", lambda: line1)[0]
            _l_(413693)
            trans = _n_(413694, "line1", lambda: line1)[1]
            _l_(413695)
            PoS = _n_(413696, "line1", lambda: line1)[2]
            _l_(413697)
            _c_(413702, _n_(413698, "Flashcards", lambda: Flashcards), _n_(413699, "key", lambda: key), _n_(413700, "trans", lambda: trans), _n_(413701, "PoS", lambda: PoS))
            _l_(413703)

def Gaeilge():
    _l_(413781)

    numberCorrect = 0
    _l_(413707)
    totalCards = 0
    _l_(413708)
    _c_(413710, _n_(413709, "ImportGaeilge", lambda: ImportGaeilge))
    _l_(413711)
    wrongCards = {}
    _l_(413712)
    x = _c_(413714, _n_(413713, "input", lambda: input), 'Hit "ENTER" to begin. (Type "quit" to quit)')
    _l_(413715)
    while _n_(413716, "x", lambda: x) != _n_(413717, "quit", lambda: quit):
        _l_(413780)

        _c_(413720, _a_(413719, _n_(413718, "os", lambda: os), "system"), 'cls')
        _l_(413721)
        _c_(413724, _a_(413723, _n_(413722, "time", lambda: time), "sleep"), 1.3)
        _l_(413725)
        card = _c_(413728, _a_(413727, _n_(413726, "flashcards", lambda: flashcards), "popitem"))
        _l_(413729)
        if _n_(413730, "card", lambda: card) == "":
            _l_(413737)

## WRONG CARDS
            _c_(413732, _n_(413731, "print", lambda: print), "Deck one complete.")
            _l_(413733)
            _c_(413735, _n_(413734, "Gaeilge", lambda: Gaeilge))
            _l_(413736)
        _c_(413739, _n_(413738, "print", lambda: print), "\n\n")
        _l_(413740)
        _c_(413745, _n_(413741, "print", lambda: print), _c_(413744, _n_(413742, "str", lambda: str), _n_(413743, "card", lambda: card)[0])+":")
        _l_(413746)
        x = _c_(413748, _n_(413747, "input", lambda: input), "\t:")
        _l_(413749)
        if _n_(413750, "x", lambda: x) == 'quit':
            _l_(413769)

            break
            _l_(413751)
        else:
            right = False
            _l_(413752)
            for item in _n_(413753, "card", lambda: card)[1]:
                _l_(413762)

                if _n_(413754, "x", lambda: x) == _n_(413755, "card", lambda: card)[1]:
                    _l_(413761)

                    right = True
                    _l_(413756)
                    _c_(413758, _n_(413757, "print", lambda: print), "\nCorrect!")
                    _l_(413759)
                    numberCorrect += 1
                    _l_(413760)
            if _n_(413763, "right", lambda: right) == False:
                _l_(413768)

                _c_(413766, _n_(413764, "print", lambda: print), _n_(413765, "card", lambda: card)[0])
                _l_(413767)

        totalCards += 1
        _l_(413770)
        _c_(413778, _n_(413771, "print", lambda: print), "Correct answers:", _c_(413774, _n_(413772, "str", lambda: str), _n_(413773, "numberCorrect", lambda: numberCorrect)) +"/"+_c_(413777, _n_(413775, "str", lambda: str), _n_(413776, "totalCards", lambda: totalCards)))
        _l_(413779)


_c_(413783, _n_(413782, "Gaeilge", lambda: Gaeilge))
_l_(413784)