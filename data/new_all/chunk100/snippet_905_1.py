# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def bigram_sequence(text_lst):
    _l_(88826)

    result = [_n_(88813, "a", lambda: a) for ls in _n_(88814, "text_lst", lambda: text_lst) for a in _c_(88822, _n_(88815, "zip", lambda: zip), _c_(88818, _a_(88817, _n_(88816, "ls", lambda: ls), "split"), ' ')[:-1], _c_(88821, _a_(88820, _n_(88819, "ls", lambda: ls), "split"), ' ')[1:])]
    _l_(88823)
    aux = _n_(88824, "result", lambda: result)
    _l_(88825)
    return aux
_c_(88828, _n_(88827, "print", lambda: print), 'Original list:')
_l_(88829)
_c_(88832, _n_(88830, "print", lambda: print), _n_(88831, "text", lambda: text))
_l_(88833)
_c_(88835, _n_(88834, "print", lambda: print), '\nBigram sequence of the said list:')
_l_(88836)
_c_(88841, _n_(88837, "print", lambda: print), _c_(88840, _n_(88838, "bigram_sequence", lambda: bigram_sequence), _n_(88839, "text", lambda: text)))
_l_(88842)