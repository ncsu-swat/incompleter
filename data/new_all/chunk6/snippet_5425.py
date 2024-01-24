# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52786661/typeerror-in-string-requires-string-as-left-operand-not-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
exg = ["I love apple.", 
        "there are lots of health benefits of apple.", 
        "apple is especially hight in Vitamin C,", 
        "alos provide Vitamin A as a powerful antioxidant!"]
_l_(373800)


fruit_list = ["pear", "banana", "mongo", "blueberry", "kiwi", "apple", "orange"]
_l_(373801)

for j in _c_(373806, _n_(373802, "range", lambda: range), 0, _c_(373805, _n_(373803, "len", lambda: len), _n_(373804, "exg", lambda: exg))):
    _l_(373820)

    sentence = _n_(373807, "exg", lambda: exg)[_n_(373808, "j", lambda: j)]
    _l_(373809)
    if _c_(373814, _n_(373810, "any", lambda: any), (_n_(373811, "word", lambda: word) in _n_(373812, "sentence", lambda: sentence) for word in _n_(373813, "fruit_list", lambda: fruit_list))):
        _l_(373819)

        _c_(373817, _n_(373815, "print", lambda: print), _n_(373816, "sentence", lambda: sentence))
        _l_(373818)