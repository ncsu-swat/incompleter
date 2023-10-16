# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def scaler(self, numericals):
    _l_(1541126)

    scaler = _c_(1541100, _n_(1541099, "MinMaxScaler", lambda: MinMaxScaler))
    _l_(1541101)
    _a_(1541104, _a_(1541103, _n_(1541102, "self", lambda: self), "data"), "loc")[:, _n_(1541105, "numericals", lambda: numericals)[0]] = _c_(1541112, _a_(1541107, _n_(1541106, "scaler", lambda: scaler), "fit_transform"), _a_(1541110, _a_(1541109, _n_(1541108, "self", lambda: self), "data"), "loc")[:, _n_(1541111, "numericals", lambda: numericals)[0]])
    _l_(1541113)
    _a_(1541116, _a_(1541115, _n_(1541114, "self", lambda: self), "data"), "loc")[:, _n_(1541117, "numericals", lambda: numericals)[1]] = _c_(1541124, _a_(1541119, _n_(1541118, "scaler", lambda: scaler), "fit_transform"), _a_(1541122, _a_(1541121, _n_(1541120, "self", lambda: self), "data"), "loc")[:, _n_(1541123, "numericals", lambda: numericals)[1]])
    _l_(1541125)

def scaler(self, numericals):
    _l_(1541154)

    scaler = _c_(1541128, _n_(1541127, "MinMaxScaler", lambda: MinMaxScaler))
    _l_(1541129)
    _a_(1541132, _a_(1541131, _n_(1541130, "self", lambda: self), "data"), "loc")[:][_n_(1541133, "numericals", lambda: numericals)[0]] = _c_(1541140, _a_(1541135, _n_(1541134, "scaler", lambda: scaler), "fit_transform"), _a_(1541138, _a_(1541137, _n_(1541136, "self", lambda: self), "data"), "loc")[:][_n_(1541139, "numericals", lambda: numericals)[0]])
    _l_(1541141)
    _a_(1541144, _a_(1541143, _n_(1541142, "self", lambda: self), "data"), "loc")[:][_n_(1541145, "numericals", lambda: numericals)[1]] = _c_(1541152, _a_(1541147, _n_(1541146, "scaler", lambda: scaler), "fit_transform"), _a_(1541150, _a_(1541149, _n_(1541148, "self", lambda: self), "data"), "loc")[:][_n_(1541151, "numericals", lambda: numericals)[1]])
    _l_(1541153)

