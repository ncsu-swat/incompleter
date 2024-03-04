# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(62543)

except ImportError:
    pass
_c_(62547, _a_(62545, _n_(62544, "re", lambda: re), "split"), '; |, ', _n_(62546, "string_to_split", lambda: string_to_split))
_l_(62548)

a='Beautiful, is; better*than\nugly'
_l_(62549)
try:
    import re
    _l_(62551)

except ImportError:
    pass
_c_(62555, _a_(62553, _n_(62552, "re", lambda: re), "split"), '; |, |\*|\n',_n_(62554, "a", lambda: a))
_l_(62556)
['Beautiful', 'is', 'better', 'than', 'ugly']
_l_(62557)

