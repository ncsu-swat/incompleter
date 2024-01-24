# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67172339/to-be-exact-this-is-the-error-im-seeing-nameerror-name-solution-is-not-defi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def containsDuplicate(self, nums: _n_(437180, "List", lambda: List)[_n_(437181, "int", lambda: int)]) -> _n_(437182, "bool", lambda: bool):
    _l_(437200)

    _c_(437185, _a_(437184, _n_(437183, "nums", lambda: nums), "sort"))
    _l_(437186)

    for i in _c_(437191, _n_(437187, "range", lambda: range), 1, _c_(437190, _n_(437188, "len", lambda: len), _n_(437189, "nums", lambda: nums))):
        _l_(437198)

        if _n_(437192, "nums", lambda: nums)[_n_(437193, "i", lambda: i)] == _n_(437194, "nums", lambda: nums)[_n_(437195, "i", lambda: i) - 1]:
            _l_(437197)

            aux = True
            _l_(437196)
            return aux
    aux = False
    _l_(437199)

    return aux