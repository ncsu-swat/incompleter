# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4564559/get-exception-description-and-stack-trace-which-caused-an-exception-all-as-a-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(1547363)

    ...
    _l_(1547352)
except _n_(1547353, "Exception", lambda: Exception) as e:
    _l_(1547362)

    _c_(1547360, _n_(1547354, "print", lambda: print), _c_(1547359, _a_(1547356, _n_(1547355, "traceback", lambda: traceback), "print_tb"), _a_(1547358, _n_(1547357, "e", lambda: e), "__traceback__")))
    _l_(1547361)

