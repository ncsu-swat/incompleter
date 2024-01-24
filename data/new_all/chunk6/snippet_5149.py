# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77441584/attributeerror-tuple-object-has-no-attribute-split-options-list-using-pick
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
quizzes = _c_(374227, _a_(374226, _n_(374225, "os", lambda: os), "listdir"))
_l_(374228)
title = '-----------\n QUIZZABLE \n-----------\n   Quiz    \n-----------'
_l_(374229)
options = [_n_(374230, "quizzes", lambda: quizzes), 'Return']
_l_(374231)
option, index = _c_(374235, _n_(374232, "pick", lambda: pick), _n_(374233, "options", lambda: options), _n_(374234, "title", lambda: title), indicator='[>]', default_index=0)
_l_(374236)