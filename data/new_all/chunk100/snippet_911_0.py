# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def duplicate_letters(text):
    _l_(91738)

    word_list = _c_(91723, _a_(91722, _n_(91721, "text", lambda: text), "split"))
    _l_(91724)
    for word in _n_(91725, "word_list", lambda: word_list):
        _l_(91736)

        if _c_(91728, _n_(91726, "len", lambda: len), _n_(91727, "word", lambda: word)) > _c_(91733, _n_(91729, "len", lambda: len), _c_(91732, _n_(91730, "set", lambda: set), _n_(91731, "word", lambda: word))):
            _l_(91735)

            aux = False
            _l_(91734)
            return aux
    aux = True
    _l_(91737)
    return aux
_c_(91740, _n_(91739, "print", lambda: print), 'Original text:')
_l_(91741)
_c_(91744, _n_(91742, "print", lambda: print), _n_(91743, "text", lambda: text))
_l_(91745)
_c_(91747, _n_(91746, "print", lambda: print), 'Check whether any word in the said sting contains duplicate characrters or not!')
_l_(91748)
_c_(91753, _n_(91749, "print", lambda: print), _c_(91752, _n_(91750, "duplicate_letters", lambda: duplicate_letters), _n_(91751, "text", lambda: text)))
_l_(91754)
text = 'Python Exercise.'
_l_(91755)
_c_(91757, _n_(91756, "print", lambda: print), '\nOriginal text:')
_l_(91758)
_c_(91761, _n_(91759, "print", lambda: print), _n_(91760, "text", lambda: text))
_l_(91762)
_c_(91764, _n_(91763, "print", lambda: print), 'Check whether any word in the said sting contains duplicate characrters or not!')
_l_(91765)
_c_(91770, _n_(91766, "print", lambda: print), _c_(91769, _n_(91767, "duplicate_letters", lambda: duplicate_letters), _n_(91768, "text", lambda: text)))
_l_(91771)
text = 'The wait is over.'
_l_(91772)
_c_(91774, _n_(91773, "print", lambda: print), '\nOriginal text:')
_l_(91775)
_c_(91778, _n_(91776, "print", lambda: print), _n_(91777, "text", lambda: text))
_l_(91779)
_c_(91781, _n_(91780, "print", lambda: print), 'Check whether any word in the said sting contains duplicate characrters or not!')
_l_(91782)
_c_(91787, _n_(91783, "print", lambda: print), _c_(91786, _n_(91784, "duplicate_letters", lambda: duplicate_letters), _n_(91785, "text", lambda: text)))
_l_(91788)