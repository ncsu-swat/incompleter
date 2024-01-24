# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52233295/typeerrora-bytes-like-object-is-required-not-str-when-reading-from-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
authors_file_handler = _c_(415036, _n_(415034, "open", lambda: open), _n_(415035, "authors_file", lambda: authors_file), "r")
_l_(415037)
authors = _c_(415041, _a_(415039, _n_(415038, "pickle", lambda: pickle), "load"), _n_(415040, "authors_file_handler", lambda: authors_file_handler))
_l_(415042)
_c_(415045, _a_(415044, _n_(415043, "authors_file_handler", lambda: authors_file_handler), "close"))
_l_(415046)