# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54315359/typeerror-check-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(334665)

except ImportError:
    pass

class login(_n_(334666, "object", lambda: object)):
    _l_(334756)

    def check(self):
        _l_(334714)

        _n_(334667, "self", lambda: self).mail = r"([\w\.-]+)@([\w\.-]+)([\w\.-]+)"
        _l_(334668)
        with _c_(334670, _n_(334669, "open", lambda: open), 'login.txt', 'r') as _a_(334672, _n_(334671, "self", lambda: self), "myfile"):
            _l_(334681)

            _n_(334673, "self", lambda: self).line1 = _c_(334679, _a_(334678, _c_(334677, _a_(334676, _a_(334675, _n_(334674, "self", lambda: self), "myfile"), "read")), "replace"), '\n', '')
            _l_(334680)
        with _c_(334683, _n_(334682, "open", lambda: open), 'username.txt', 'r') as _a_(334685, _n_(334684, "self", lambda: self), "usr"):
            _l_(334694)

            _n_(334686, "self", lambda: self).line2 = _c_(334692, _a_(334691, _c_(334690, _a_(334689, _a_(334688, _n_(334687, "self", lambda: self), "usr"), "read")), "replace"), '\n', '')
            _l_(334693)
        if _c_(334701, _a_(334696, _n_(334695, "re", lambda: re), "findall"), _a_(334698, _n_(334697, "self", lambda: self), "mail"), _a_(334700, _n_(334699, "self", lambda: self), "line1")):
            _l_(334708)

            _c_(334703, _n_(334702, "goon", lambda: goon))
            _l_(334704)
        else:
            _c_(334706, _n_(334705, "log", lambda: log))
            _l_(334707)
        _c_(334712, _a_(334711, _a_(334710, _n_(334709, "self", lambda: self), "myfile"), "close"))
        _l_(334713)

    def goon(self):
        _l_(334717)

        try:
            import assistant
            _l_(334716)

        except ImportError:
            pass

    def log(self):
        _l_(334747)

        _n_(334718, "self", lambda: self).file = _c_(334720, _n_(334719, "open", lambda: open), "login.txt", "w")
        _l_(334721)
        _c_(334725, _a_(334724, _a_(334723, _n_(334722, "self", lambda: self), "file"), "truncate"), 0)
        _l_(334726)
        _n_(334727, "self", lambda: self).data = _c_(334729, _n_(334728, "input", lambda: input), "Your email: ")
        _l_(334730)
        _c_(334736, _a_(334733, _a_(334732, _n_(334731, "self", lambda: self), "file"), "write"), _a_(334735, _n_(334734, "self", lambda: self), "data"))
        _l_(334737)
        _c_(334741, _a_(334740, _a_(334739, _n_(334738, "self", lambda: self), "file"), "close"))
        _l_(334742)
        _c_(334745, _a_(334744, _n_(334743, "l", lambda: l), "goon"))
        _l_(334746)

    if _n_(334748, "__name__", lambda: __name__) == '__main__':
        _l_(334755)

        _c_(334749, check) #error
        _l_(334750) #error
        _c_(334751, log)
        _l_(334752)
        _c_(334753, goon)
        _l_(334754)