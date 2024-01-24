# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51690799/why-is-a-nameerror-raised-when-using-a-list-compression-at-the-class-level
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
...
_l_(403149)
class Planet:
    _l_(403178)

    ATMOSPHERE_GASES = {
        'N2':(67.59, 28.0134),
        'O2':(28.04, 31.9988),
        'CO2':(0.0114, 44.00995),
        'CH4':(0.00015, 16.04303),
        'Ar':(1.105, 39.948),
        'Ne':(1.003, 20.179),
        'He':(0.719, 4.0026),
        'Kr':(0.45, 83.80),
        'H2':(0.001, 2.01594),
        'Xe':(0.23, 131.30)}
    _l_(403150)
    ATMOSPHERE_GASES['Other'] = _c_(403166, _n_(403151, "tuple", lambda: tuple), [100-_c_(403156, _n_(403152, "sum", lambda: sum), [_n_(403153, "x", lambda: x)[0] for x in _c_(403155, _a_(403154, ATMOSPHERE_GASES, "values"))]), _c_(403161, _n_(403157, "sum", lambda: sum), [_n_(403158, "x", lambda: x)[1] for x in _c_(403160, _a_(403159, ATMOSPHERE_GASES, "values"))])/_c_(403165, _n_(403162, "len", lambda: len), _c_(403164, _a_(403163, ATMOSPHERE_GASES, "values")))])
    _l_(403167)
    ATMOSPHERE_GASES_MOLAR_MASS = _c_(403175, _n_(403168, "sum", lambda: sum), [_c_(403172, _n_(403169, "sum", lambda: sum), _n_(403170, "ATMOSPHERE_GASES", lambda: ATMOSPHERE_GASES)[_n_(403171, "x", lambda: x)]) for x in _c_(403174, _a_(403173, ATMOSPHERE_GASES, "keys"))])/100
    _l_(403176)
    ...
    _l_(403177)