# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67958138/how-to-fix-attributeerror-nonetype-object-has-no-attribute-group
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from googletrans import Translator, constants
    _l_(472622)

except ImportError:
    pass
try:
    from pprint import print
    _l_(472624)

except ImportError:
    pass


# init the Google API translator
translator = _c_(472626, _n_(472625, "Translator", lambda: Translator))
_l_(472627)

# translate a spanish text to english text (by default)
translation = _c_(472630, _a_(472629, _n_(472628, "translator", lambda: translator), "translate"), "Hola Mundo")
_l_(472631)


_c_(472643, _n_(472632, "print", lambda: print), _c_(472642, _a_(472633, "{} ({}) --> {} ({})", "format"), _a_(472635, _n_(472634, "translation", lambda: translation), "origin"), _a_(472637, _n_(472636, "translation", lambda: translation), "src"), _a_(472639, _n_(472638, "translation", lambda: translation), "text"), _a_(472641, _n_(472640, "translation", lambda: translation), "dest")))
_l_(472644)