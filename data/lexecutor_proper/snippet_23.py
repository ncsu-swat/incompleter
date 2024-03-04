# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
L = [_c_(62003, _a_(61998, _a_(61997, _n_(61996, "os", lambda: os), "path"), "join"), _c_(62001, _a_(62000, _n_(61999, "os", lambda: os), "getcwd")),_n_(62002, "f", lambda: f)) for f in _c_(62006, _a_(62005, _n_(62004, "os", lambda: os), "listdir"), '.') if _c_(62018, _a_(62009, _a_(62008, _n_(62007, "os", lambda: os), "path"), "isfile"), _c_(62017, _a_(62012, _a_(62011, _n_(62010, "os", lambda: os), "path"), "join"), _c_(62015, _a_(62014, _n_(62013, "os", lambda: os), "getcwd")),_n_(62016, "f", lambda: f)))]
_l_(62019)

