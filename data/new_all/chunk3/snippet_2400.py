# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46582490/typeerror-ufunc-add-did-not-contain-a-loop-with-signature-for-arima-model
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Cdx = _a_(567256, _n_(567255, "CpcGDP", lambda: CpcGDP), "columns")[0]
_l_(567257)
S = _a_(567259, _n_(567258, "CpcGDP", lambda: CpcGDP), "loc")[:, _n_(567260, "Cdx", lambda: Cdx)]
_l_(567261)
_c_(567265, _a_(567263, _n_(567262, "S", lambda: S), "astype"), _n_(567264, "float", lambda: float))
_l_(567266)