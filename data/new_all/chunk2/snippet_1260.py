# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61232050/typeerror-numpy-bool-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(449313)

except ImportError:
    pass


def rad_to_deg(x):
    _l_(449320)

    deg = _n_(449314, "x", lambda: x)*180/_a_(449316, _n_(449315, "np", lambda: np), "pi")
    _l_(449317)
    aux = _n_(449318, "deg", lambda: deg)
    _l_(449319)
    return aux

def flag_PA(x,bornes_test):
    _l_(449358)

    index_0_test = _c_(449326, _n_(449321, "int", lambda: int), _c_(449325, _a_(449323, _n_(449322, "np", lambda: np), "where"), _n_(449324, "bornes_test", lambda: bornes_test)==0)[0][0])
    _l_(449327)
    for i in _c_(449330, _n_(449328, "range", lambda: range), _n_(449329, "index_0_test", lambda: index_0_test)):
        _l_(449355)

        cond1 = _c_(449337, _n_(449331, "any", lambda: any), _n_(449332, "bornes_test", lambda: bornes_test)[_n_(449333, "i", lambda: i)] <= _n_(449334, "x", lambda: x) < _n_(449335, "bornes_test", lambda: bornes_test)[_n_(449336, "i", lambda: i)+1])
        _l_(449338)
        cond2 = _c_(449345, _n_(449339, "any", lambda: any), _n_(449340, "bornes_test", lambda: bornes_test)[_n_(449341, "i", lambda: i)]+180 <= _n_(449342, "x", lambda: x) < _n_(449343, "bornes_test", lambda: bornes_test)[_n_(449344, "i", lambda: i)+1]+180)
        _l_(449346)
        if _c_(449351, _a_(449348, _n_(449347, "np", lambda: np), "logical_or"), _n_(449349, "cond1", lambda: cond1),_n_(449350, "cond2", lambda: cond2))==True :
            _l_(449354)

            flag_test=_n_(449352, "i", lambda: i) 
            _l_(449353) 
    aux = _n_(449356, "flag_test", lambda: flag_test)
    _l_(449357)
    return aux


##################################### DATA READING ###########################

# Trouver les fichiers en Bande L et Bande N 


bornes_PA = _c_(449361, _a_(449360, _n_(449359, "np", lambda: np), "linspace"), -180,180,18+1)
_l_(449362)

lambda_fichier       = _c_(449365, _a_(449364, _n_(449363, "np", lambda: np), "linspace"), 3E-6,11E-6)
_l_(449366)
u_coord_fichier      = _c_(449369, _a_(449368, _n_(449367, "np", lambda: np), "linspace"), 1,40)
_l_(449370)
v_coord_fichier      = _c_(449373, _a_(449372, _n_(449371, "np", lambda: np), "linspace"), 1,40)
_l_(449374)
baseline_fichier     = _c_(449387, _a_(449386, _c_(449385, _a_(449376, _n_(449375, "np", lambda: np), "sqrt"), _c_(449380, _a_(449378, _n_(449377, "np", lambda: np), "array"), _n_(449379, "u_coord_fichier", lambda: u_coord_fichier))**2+_c_(449384, _a_(449382, _n_(449381, "np", lambda: np), "array"), _n_(449383, "v_coord_fichier", lambda: v_coord_fichier))**2), "tolist"))
_l_(449388)
for l in _c_(449393, _n_(449389, "range", lambda: range), _c_(449392, _n_(449390, "len", lambda: len), _n_(449391, "lambda_fichier", lambda: lambda_fichier))):
    _l_(449417)

    for b in _c_(449398, _n_(449394, "range", lambda: range), _c_(449397, _n_(449395, "len", lambda: len), _n_(449396, "baseline_fichier", lambda: baseline_fichier))):
        _l_(449416)

        deg = _c_(449407, _n_(449399, "rad_to_deg", lambda: rad_to_deg), _c_(449406, _a_(449401, _n_(449400, "np", lambda: np), "arctan2"), _n_(449402, "u_coord_fichier", lambda: u_coord_fichier)[_n_(449403, "b", lambda: b)],_n_(449404, "v_coord_fichier", lambda: v_coord_fichier)[_n_(449405, "b", lambda: b)]))
        _l_(449408)
        result = _c_(449414, _n_(449409, "int", lambda: int), _c_(449413, _n_(449410, "flag_PA", lambda: flag_PA), _n_(449411, "deg", lambda: deg),_n_(449412, "bornes_PA", lambda: bornes_PA)))
        _l_(449415)