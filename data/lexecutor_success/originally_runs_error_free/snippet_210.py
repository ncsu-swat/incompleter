# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12453580/how-to-concatenate-join-items-in-a-list-to-a-single-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
words = ['this', 'is', 'a', 'sentence']
_l_(1543294)
_c_(1543297, _a_(1543295, '-', "join"), _n_(1543296, "words", lambda: words))
_l_(1543298)
'this-is-a-sentence'
_l_(1543299)
_c_(1543302, _a_(1543300, ' ', "join"), _n_(1543301, "words", lambda: words))
_l_(1543303)
'this is a sentence'
_l_(1543304)

