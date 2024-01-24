# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55331164/typeerror-object-of-type-int-has-no-len-subtraction
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
number_1_raw = _c_(537189, _a_(537188, _n_(537187, "random", lambda: random), "randrange"), 1, 1000)
_l_(537190)
number_1_len = _c_(537193, _n_(537191, "len", lambda: len), _n_(537192, "number_1_raw", lambda: number_1_raw))
_l_(537194)
number_of_zeros = 4 - _n_(537195, "number_1_len", lambda: number_1_len)
_l_(537196)
_c_(537200, _n_(537197, "print", lambda: print), "0" * _n_(537198, "number_of_zeros", lambda: number_of_zeros) + _n_(537199, "number_1_raw", lambda: number_1_raw))
_l_(537201)