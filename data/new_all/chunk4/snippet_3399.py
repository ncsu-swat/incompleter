# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74895052/python-attributeerror-module-core-has-no-attribute-children
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(637750)

except ImportError:
    pass
try:
    from core.screen_manager import WindowManager
    _l_(637752)

except ImportError:
    pass


class VaccinationCalendarApp(_n_(637753, "MDApp", lambda: MDApp)):
    _l_(637761)

    def build(self):
        _l_(637760)

        _a_(637755, _n_(637754, "self", lambda: self), "theme_cls").primary_palette = "Green"
        _l_(637756)
        aux = _c_(637758, _n_(637757, "WindowManager", lambda: WindowManager))
        _l_(637759)
        return aux


if _n_(637762, "__name__", lambda: __name__) == "__main__":
    _l_(637768)

    _c_(637766, _a_(637765, _c_(637764, _n_(637763, "VaccinationCalendarApp", lambda: VaccinationCalendarApp)), "run"))
    _l_(637767)