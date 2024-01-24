# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73015092/why-am-i-getting-type-error-on-list-but-it-works-on-list-append
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
text_to_list = _c_(445666, _n_(445664, "list", lambda: list), _n_(445665, "text", lambda: text))
_l_(445667)
list_to_number = []
_l_(445668)
for letter in _n_(445669, "text_to_list", lambda: text_to_list):
    _l_(445680)

    cipher_num = _c_(445673, _a_(445671, _n_(445670, "alphabet", lambda: alphabet), "index"), _n_(445672, "letter", lambda: letter))
    _l_(445674)
    _c_(445678, _a_(445676, _n_(445675, "list_to_number", lambda: list_to_number), "append"), _n_(445677, "cipher_num", lambda: cipher_num))
    _l_(445679)