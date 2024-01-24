# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54315359/typeerror-check-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(342309)

except ImportError:
    pass

class login(_n_(342310, "object", lambda: object)):
    _l_(342400)

    def check(self):
        _l_(342358)

        _n_(342311, "self", lambda: self).mail = r"([\w\.-]+)@([\w\.-]+)([\w\.-]+)"
        _l_(342312)
        with _c_(342314, _n_(342313, "open", lambda: open), 'login.txt', 'r') as _a_(342316, _n_(342315, "self", lambda: self), "myfile"):
            _l_(342325)

            _n_(342317, "self", lambda: self).line1 = _c_(342323, _a_(342322, _c_(342321, _a_(342320, _a_(342319, _n_(342318, "self", lambda: self), "myfile"), "read")), "replace"), '\n', '')
            _l_(342324)
        with _c_(342327, _n_(342326, "open", lambda: open), 'username.txt', 'r') as _a_(342329, _n_(342328, "self", lambda: self), "usr"):
            _l_(342338)

            _n_(342330, "self", lambda: self).line2 = _c_(342336, _a_(342335, _c_(342334, _a_(342333, _a_(342332, _n_(342331, "self", lambda: self), "usr"), "read")), "replace"), '\n', '')
            _l_(342337)
        if _c_(342345, _a_(342340, _n_(342339, "re", lambda: re), "findall"), _a_(342342, _n_(342341, "self", lambda: self), "mail"), _a_(342344, _n_(342343, "self", lambda: self), "line1")):
            _l_(342352)

            _c_(342347, _n_(342346, "goon", lambda: goon))
            _l_(342348)
        else:
            _c_(342350, _n_(342349, "log", lambda: log))
            _l_(342351)
        _c_(342356, _a_(342355, _a_(342354, _n_(342353, "self", lambda: self), "myfile"), "close"))
        _l_(342357)

    def goon(self):
        _l_(342361)

        try:
            import assistant
            _l_(342360)

        except ImportError:
            pass

    def log(self):
        _l_(342391)

        _n_(342362, "self", lambda: self).file = _c_(342364, _n_(342363, "open", lambda: open), "login.txt", "w")
        _l_(342365)
        _c_(342369, _a_(342368, _a_(342367, _n_(342366, "self", lambda: self), "file"), "truncate"), 0)
        _l_(342370)
        _n_(342371, "self", lambda: self).data = _c_(342373, _n_(342372, "input", lambda: input), "Your email: ")
        _l_(342374)
        _c_(342380, _a_(342377, _a_(342376, _n_(342375, "self", lambda: self), "file"), "write"), _a_(342379, _n_(342378, "self", lambda: self), "data"))
        _l_(342381)
        _c_(342385, _a_(342384, _a_(342383, _n_(342382, "self", lambda: self), "file"), "close"))
        _l_(342386)
        _c_(342389, _a_(342388, _n_(342387, "l", lambda: l), "goon"))
        _l_(342390)

    if _n_(342392, "__name__", lambda: __name__) == '__main__':
        _l_(342399)

        _c_(342393, check) #error
        _l_(342394) #error
        _c_(342395, log)
        _l_(342396)
        _c_(342397, goon)
        _l_(342398)