# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54620191/list-comprehension-returntypeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
album_1974 = [_n_(455102, "row", lambda: row) for row in _n_(455103, "album", lambda: album) if _c_(455106, _n_(455104, "is_valid_year", lambda: is_valid_year), _n_(455105, "row", lambda: row)["Year"]=="1974")] #this is list comprehension 
_l_(455107) #this is list comprehension 
_c_(455112, _n_(455108, "print", lambda: print), "No of album in 1974 released:",_c_(455111, _n_(455109, "len", lambda: len), _n_(455110, "album_1974", lambda: album_1974)))
_l_(455113)