# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41433908/attributeerror-when-trying-to-use-colorama-not-a-good-title-i-know
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from colorama import Fore, Back, Style, init
    _l_(408931)

except ImportError:
    pass
_c_(408933, _n_(408932, "init", lambda: init))
_l_(408934)
def colorprint(str1, str2):
    _l_(408943)

    _c_(408941, _n_(408935, "print", lambda: print), _a_(408937, _n_(408936, "Fore", lambda: Fore), "str2") + _n_(408938, "str1", lambda: str1) + _a_(408940, _n_(408939, "Fore", lambda: Fore), "WHITE"))
    _l_(408942)
_c_(408945, _n_(408944, "colorprint", lambda: colorprint), "words", "GREEN")
_l_(408946)