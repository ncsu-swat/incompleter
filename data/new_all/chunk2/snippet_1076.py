# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43578116/dictionary-error-typeerror-str-object-does-not-support-item-assignment
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(448661)

except ImportError:
    pass

f = _c_(448663, _n_(448662, "open", lambda: open), "save")
_l_(448664)
forbidden = _c_(448667, _a_(448666, _n_(448665, "f", lambda: f), "readline"))
_l_(448668)
forbiddens = _c_(448671, _a_(448670, _n_(448669, "f", lambda: f), "readline"))
_l_(448672)
dictionary = _c_(448675, _a_(448674, _n_(448673, "f", lambda: f), "readline"))
_l_(448676)
stop = 0
_l_(448677)
global arguments
_l_(448678)
_c_(448680, _n_(448679, "print", lambda: print), "phonebook os by me")
_l_(448681)

def write():
    _l_(448699)

    global forbidden
    _l_(448682)
    global forbiddens
    _l_(448683)
    global dictionary
    _l_(448684)
    f = _c_(448686, _n_(448685, "open", lambda: open), "save")
    _l_(448687)
    _c_(448693, _a_(448689, _n_(448688, "f", lambda: f), "write"), _n_(448690, "forbidden", lambda: forbidden) and '\n' and _n_(448691, "forbiddens", lambda: forbiddens) and '\n' and _n_(448692, "dictionary", lambda: dictionary))
    _l_(448694)
    _c_(448697, _a_(448696, _n_(448695, "f", lambda: f), "close"))
    _l_(448698)

def add_cc():
    _l_(448731)

    global forbidden
    _l_(448700)
    global dictionary
    _l_(448701)
    global arguments
    _l_(448702)
    name = _n_(448703, "arguments", lambda: arguments)[1]
    _l_(448704)
    number = _c_(448707, _n_(448705, "int", lambda: int), _n_(448706, "arguments", lambda: arguments)[2])
    _l_(448708)
    if _n_(448709, "name", lambda: name) in _n_(448710, "forbidden", lambda: forbidden):
        _l_(448724)

        _c_(448712, _n_(448711, "print", lambda: print), "403: forbidden!")
        _l_(448713)
    elif _n_(448714, "name", lambda: name) in _n_(448715, "dictionary", lambda: dictionary):
        _l_(448723)

        _c_(448717, _n_(448716, "print", lambda: print), "406: Not acceptable! This item is already in the dictionary!")
        _l_(448718)
    else:
        _n_(448719, "dictionary", lambda: dictionary)[_n_(448720, "name", lambda: name)] = _n_(448721, "number", lambda: number)
        _l_(448722)
    _c_(448726, _n_(448725, "write", lambda: write))
    _l_(448727)
    _c_(448729, _n_(448728, "start", lambda: start))
    _l_(448730)

def del_cc():
    _l_(448743)

    global arguments
    _l_(448732)
    global dictionary
    _l_(448733)
    name = _n_(448734, "arguments", lambda: arguments)[1]
    _l_(448735)
    del dictionary[name]
    _l_(448736)
    _c_(448738, _n_(448737, "write", lambda: write))
    _l_(448739)
    _c_(448741, _n_(448740, "start", lambda: start))
    _l_(448742)

def get_cc():
    _l_(448769)

    global arguments
    _l_(448744)
    global forbidden
    _l_(448745)
    global dictionary
    _l_(448746)
    name = _n_(448747, "arguments", lambda: arguments)[1]
    _l_(448748)
    if _n_(448749, "name", lambda: name) in _n_(448750, "dictionary", lambda: dictionary):
        _l_(448765)

        _c_(448754, _n_(448751, "print", lambda: print), _n_(448752, "dictionary", lambda: dictionary)[_n_(448753, "name", lambda: name)])
        _l_(448755)
    elif _n_(448756, "name", lambda: name) in _n_(448757, "forbidden", lambda: forbidden):
        _l_(448764)

        _c_(448759, _n_(448758, "print", lambda: print), "403: Forbidden!")
        _l_(448760)
    else:
        _c_(448762, _n_(448761, "print", lambda: print), "404: Item not Found.")
        _l_(448763)
    _c_(448767, _n_(448766, "start", lambda: start))
    _l_(448768)