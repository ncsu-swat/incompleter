# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60661533/type-error-function-missing-1-required-positional-argument-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(672131)

    def lengthOfLongestSubstring(self, s):
        _l_(672098)

        arr = [_n_(672050, "char1", lambda: char1) for char1 in _n_(672051, "s", lambda: s)]
        _l_(672052)
        help_arr = [_n_(672053, "i", lambda: i)*0 for i in _c_(672055, _n_(672054, "range", lambda: range), 26)]
        _l_(672056)
        sub_strings = []
        _l_(672057)
        sub = ""
        _l_(672058)
        for char in _n_(672059, "s", lambda: s):
            _l_(672093)

            index = _c_(672062, _n_(672060, "ord", lambda: ord), _n_(672061, "char", lambda: char)) - _c_(672064, _n_(672063, "ord", lambda: ord), 'a')
            _l_(672065)
            if _n_(672066, "help_arr", lambda: help_arr)[_n_(672067, "index", lambda: index)] == 0:
                _l_(672092)

                _n_(672068, "help_arr", lambda: help_arr)[_n_(672069, "index", lambda: index)] = _c_(672071, _n_(672070, "int", lambda: int), 1)
                _l_(672072)
                sub += _n_(672073, "char", lambda: char)
                _l_(672074)
            else:
                _c_(672078, _a_(672076, _n_(672075, "sub_strings", lambda: sub_strings), "append"), _n_(672077, "sub", lambda: sub))
                _l_(672079)
                sub = ""
                _l_(672080)
                sub += _n_(672081, "char", lambda: char)
                _l_(672082)
                help_arr = [_n_(672083, "i", lambda: i) * 0 for i in _c_(672085, _n_(672084, "range", lambda: range), 26)]
                _l_(672086)
                _n_(672087, "help_arr", lambda: help_arr)[_n_(672088, "index", lambda: index)] = _c_(672090, _n_(672089, "int", lambda: int), 1)
                _l_(672091)
        _c_(672096, _n_(672094, "max", lambda: max), _n_(672095, "sub_strings", lambda: sub_strings))
        _l_(672097)


    def max(arr):
        _l_(672128)

        max = 0
        _l_(672099)
        index = -1
        _l_(672100)
        for i in _c_(672105, _n_(672101, "range", lambda: range), _c_(672104, _n_(672102, "len", lambda: len), _n_(672103, "arr", lambda: arr))):
            _l_(672119)

            if _c_(672109, _n_(672106, "len", lambda: len), _n_(672107, "arr", lambda: arr)[_n_(672108, "i", lambda: i)]) > _n_(672110, "max", lambda: max):
                _l_(672118)

                max = _c_(672114, _n_(672111, "len", lambda: len), _n_(672112, "arr", lambda: arr)[_n_(672113, "i", lambda: i)])
                _l_(672115)
                index=  _n_(672116, "i", lambda: i)
                _l_(672117)
        aux = _c_(672126, _n_(672120, "print", lambda: print), _c_(672125, _a_(672121, "The answer is '{}', with the length of {}.", "format"), _n_(672122, "arr", lambda: arr)[_n_(672123, "index", lambda: index)], _n_(672124, "max", lambda: max)))
        _l_(672127)
        return aux

    #call to function
    _c_(672129, lengthOfLongestSubstring, "aabcdefffgges")
    _l_(672130)