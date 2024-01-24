# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71628072/i-am-getting-the-error-filenotfounderror-errno-2-no-such-file-or-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(642725, _n_(642724, "print", lambda: print), "Dictionary File Path -")
_l_(642726)
filename = _c_(642728, _n_(642727, "input", lambda: input))
_l_(642729)

_c_(642731, _n_(642730, "print", lambda: print), "Words Length -")
_l_(642732)
word_length = _c_(642734, _n_(642733, "input", lambda: input))
_l_(642735)
words = _c_(642737, _n_(642736, "list", lambda: list))
_l_(642738)

with _c_(642741, _n_(642739, "open", lambda: open), _n_(642740, "filename", lambda: filename)) as dict:
    _l_(642758)

    for line in _n_(642742, "dict", lambda: dict):
        _l_(642753)

        if _c_(642745, _n_(642743, "len", lambda: len), _n_(642744, "line", lambda: line)) == _n_(642746, "word_length", lambda: word_length):
            _l_(642752)

            _c_(642750, _a_(642748, _n_(642747, "list", lambda: list), "append"), _n_(642749, "line", lambda: line))
            _l_(642751)
    _c_(642756, _n_(642754, "print", lambda: print), _n_(642755, "words", lambda: words))
    _l_(642757)