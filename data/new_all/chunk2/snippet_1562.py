# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77438731/fixing-datatype-error-in-oracledb-from-python-ora-01790
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = [1,2,None,4,5,6]
_l_(435835)
sql = """
SELECT :1 AS ID, :2 AS pkey, :3 AS issuenum FROM dual  UNION ALL
SELECT :4 AS ID, :5 AS pkey, :6 AS issuenum FROM dual 
"""
_l_(435836)

cur = _c_(435839, _a_(435838, _n_(435837, "con", lambda: con), "cursor"))
_l_(435840)
_c_(435845, _a_(435842, _n_(435841, "cur", lambda: cur), "execute"), _n_(435843, "sql", lambda: sql), _n_(435844, "data", lambda: data))
_l_(435846)
data = _c_(435849, _a_(435848, _n_(435847, "cur", lambda: cur), "fetchall"))
_l_(435850)