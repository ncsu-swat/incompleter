# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74389747/attributeerror-what-am-i-doing-wrong-here
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from spellCheck import SpellCheck
    _l_(393246)

except ImportError:
    pass
#from spellCheck import bcolors

def main():
    _l_(393262)

    choice = _c_(393248, _n_(393247, "input", lambda: input), "Enter the word to look for:\n> ")
    _l_(393249)
    initial = _c_(393251, _n_(393250, "SpellCheck", lambda: SpellCheck))
    _l_(393252)
    _c_(393255, _a_(393254, _n_(393253, "initial", lambda: initial), "__init__"))
    _l_(393256)
    _c_(393260, _a_(393258, _n_(393257, "initial", lambda: initial), "linearSearch"), _n_(393259, "choice", lambda: choice))
    _l_(393261)
_c_(393264, _n_(393263, "main", lambda: main))
_l_(393265)