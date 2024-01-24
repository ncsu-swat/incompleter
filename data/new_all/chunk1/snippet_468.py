# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/26064701/appendleft-iterating-deque-function-attributeerror-list-object-has-no-attrib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import deque
    _l_(416938)

except ImportError:
    pass

list_stack = []
_l_(416939)
list_queue = ([])
_l_(416940)
string_to_list = "This is a sentence with more than six words."
_l_(416941)

string_to_list = _c_(416944, _a_(416943, _n_(416942, "string_to_list", lambda: string_to_list), "split"))
_l_(416945)

for i in _n_(416946, "string_to_list", lambda: string_to_list):
    _l_(416957)

    _c_(416950, _a_(416948, _n_(416947, "list_stack", lambda: list_stack), "append"), _n_(416949, "i", lambda: i))
    _l_(416951)
    _c_(416955, _a_(416953, _n_(416952, "list_queue", lambda: list_queue), "appendleft"), _n_(416954, "i", lambda: i))
    _l_(416956)
_c_(416960, _n_(416958, "print", lambda: print), "The variable created as a stack" ,_n_(416959, "list_stack", lambda: list_stack))
_l_(416961)
_c_(416964, _n_(416962, "print", lambda: print), "The variable created as a queue" ,_n_(416963, "list_queue", lambda: list_queue))
_l_(416965)