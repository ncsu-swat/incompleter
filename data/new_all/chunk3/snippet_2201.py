# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57766165/attributeerror-nonetype-object-has-no-attribute-split-when-trying-to-split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(572540, _a_(572539, _n_(572538, "df_no_dup", lambda: df_no_dup), "head"))
_l_(572541)



start = _c_(572544, _a_(572543, _n_(572542, "datetime", lambda: datetime), "now"))
_l_(572545)
_n_(572546, "df_no_dup", lambda: df_no_dup)["tag_count"] = _c_(572554, _a_(572548, _n_(572547, "df_no_dup", lambda: df_no_dup)["Tags"], "apply"), lambda text: _c_(572553, _n_(572549, "len", lambda: len), _c_(572552, _a_(572551, _n_(572550, "text", lambda: text), "split"), " ")))
_l_(572555)

_c_(572561, _n_(572556, "print", lambda: print), "Time taken to run this cell :", _c_(572559, _a_(572558, _n_(572557, "datetime", lambda: datetime), "now")) - _n_(572560, "start", lambda: start))
_l_(572562)
_c_(572565, _a_(572564, _n_(572563, "df_no_dup", lambda: df_no_dup), "head"))
_l_(572566)