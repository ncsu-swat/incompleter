# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59905138/python-error-typeerror-fit-missing-2-required-positional-arguments-x-and
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn import tree
    _l_(529533)

except ImportError:
    pass

#[height,weight,shoe size]

X = [181,80,44], [177,70,43], [160,60,38], [154, 54,37]
_l_(529534)

Y = ['male','female','female','female']
_l_(529535)

clf = _a_(529537, _n_(529536, "tree", lambda: tree), "DecisionTreeClassifier")
_l_(529538)

clf = _c_(529543, _a_(529540, _n_(529539, "clf", lambda: clf), "fit"), _n_(529541, "X", lambda: X),_n_(529542, "Y", lambda: Y))
_l_(529544)

prediciton = _c_(529547, _a_(529546, _n_(529545, "clf", lambda: clf), "predict"), [[190,70,43]])
_l_(529548)

_c_(529550, 'print', _n_(529549, "prediciton", lambda: prediciton))
_l_(529551)