# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1539593, _n_(1539592, "len", lambda: len), 'Öl')  # German word for 'oil' with 2 characters
_l_(1539594)  # German word for 'oil' with 2 characters
2
_l_(1539595)
_c_(1539597, _a_(1539596, 'Öl', "encode"), 'UTF-8')  # convert str to bytes 
_l_(1539598)  # convert str to bytes 
b'\xc3\x96l'
_l_(1539599)
_c_(1539603, _n_(1539600, "len", lambda: len), _c_(1539602, _a_(1539601, 'Öl', "encode"), 'UTF-8'))  # 3 bytes encode 2 characters !
_l_(1539604)  # 3 bytes encode 2 characters !
3
_l_(1539605)

