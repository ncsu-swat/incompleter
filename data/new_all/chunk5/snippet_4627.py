# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53911591/pythontypeerror-cant-multiply-sequence-by-non-int-of-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def polynomial_features(data, deg):
    _l_(695166)

    data_copy=_c_(695148, _a_(695147, _n_(695146, "data", lambda: data), "copy"))
    _l_(695149)
    #print(data_copy.head())
    for i in _c_(695152, _n_(695150, "range", lambda: range), 1,_n_(695151, "deg", lambda: deg)):
        _l_(695163)

        _n_(695153, "data_copy", lambda: data_copy)['X'+_c_(695156, _n_(695154, "str", lambda: str), _n_(695155, "i", lambda: i)+1)]=_n_(695157, "data_copy", lambda: data_copy)['X'+_c_(695160, _n_(695158, "str", lambda: str), _n_(695159, "i", lambda: i))]*_n_(695161, "data_copy", lambda: data_copy)['X1']
        _l_(695162)
    aux = _n_(695164, "data_copy", lambda: data_copy)
    _l_(695165)
    return aux

x_pred = _c_(695172, _a_(695168, _n_(695167, "pd", lambda: pd), "Series"), {'X1':[_n_(695169, "i", lambda: i)/200.0 for i in _c_(695171, _n_(695170, "range", lambda: range), 200)]})
_l_(695173)
y_pred = _c_(695180, _a_(695175, _n_(695174, "model", lambda: model), "predict"), _c_(695179, _n_(695176, "polynomial_features", lambda: polynomial_features), _n_(695177, "x_pred", lambda: x_pred),_n_(695178, "deg", lambda: deg)))
_l_(695181)