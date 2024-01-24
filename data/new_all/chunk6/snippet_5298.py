# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72181000/attribute-error-module-teradatasql-has-no-attribute-connect-please-solve-th
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(367293, _a_(367292, _n_(367291, "cursor", lambda: cursor), "execute"), "insert into voltab (?, ?)", [
        [1, "abc"],
        [2, "def"],
        [3, "ghi"]])
_l_(367294)

_c_(367297, _a_(367296, _n_(367295, "cursor", lambda: cursor), "execute"), "select * from voltab order by 1")
_l_(367298)
[ _c_(367301, _n_(367299, "print", lambda: print), _n_(367300, "row", lambda: row)) for row in _c_(367304, _a_(367303, _n_(367302, "cur", lambda: cur), "fetchall")) ]
_l_(367305)
_c_(367308, _a_(367307, _n_(367306, "connect", lambda: connect), "commit"))
_l_(367309)