# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60661533/type-error-function-missing-1-required-positional-argument-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(701250)

    def lengthOfLongestSubstring(self, s):
        _l_(701217)

        arr = [_n_(701169, "char1", lambda: char1) for char1 in _n_(701170, "s", lambda: s)]
        _l_(701171)
        help_arr = [_n_(701172, "i", lambda: i)*0 for i in _c_(701174, _n_(701173, "range", lambda: range), 26)]
        _l_(701175)
        sub_strings = []
        _l_(701176)
        sub = ""
        _l_(701177)
        for char in _n_(701178, "s", lambda: s):
            _l_(701212)

            index = _c_(701181, _n_(701179, "ord", lambda: ord), _n_(701180, "char", lambda: char)) - _c_(701183, _n_(701182, "ord", lambda: ord), 'a')
            _l_(701184)
            if _n_(701185, "help_arr", lambda: help_arr)[_n_(701186, "index", lambda: index)] == 0:
                _l_(701211)

                _n_(701187, "help_arr", lambda: help_arr)[_n_(701188, "index", lambda: index)] = _c_(701190, _n_(701189, "int", lambda: int), 1)
                _l_(701191)
                sub += _n_(701192, "char", lambda: char)
                _l_(701193)
            else:
                _c_(701197, _a_(701195, _n_(701194, "sub_strings", lambda: sub_strings), "append"), _n_(701196, "sub", lambda: sub))
                _l_(701198)
                sub = ""
                _l_(701199)
                sub += _n_(701200, "char", lambda: char)
                _l_(701201)
                help_arr = [_n_(701202, "i", lambda: i) * 0 for i in _c_(701204, _n_(701203, "range", lambda: range), 26)]
                _l_(701205)
                _n_(701206, "help_arr", lambda: help_arr)[_n_(701207, "index", lambda: index)] = _c_(701209, _n_(701208, "int", lambda: int), 1)
                _l_(701210)
        _c_(701215, _n_(701213, "max", lambda: max), _n_(701214, "sub_strings", lambda: sub_strings))
        _l_(701216)


    def max(arr):
        _l_(701247)

        max = 0
        _l_(701218)
        index = -1
        _l_(701219)
        for i in _c_(701224, _n_(701220, "range", lambda: range), _c_(701223, _n_(701221, "len", lambda: len), _n_(701222, "arr", lambda: arr))):
            _l_(701238)

            if _c_(701228, _n_(701225, "len", lambda: len), _n_(701226, "arr", lambda: arr)[_n_(701227, "i", lambda: i)]) > _n_(701229, "max", lambda: max):
                _l_(701237)

                max = _c_(701233, _n_(701230, "len", lambda: len), _n_(701231, "arr", lambda: arr)[_n_(701232, "i", lambda: i)])
                _l_(701234)
                index=  _n_(701235, "i", lambda: i)
                _l_(701236)
        aux = _c_(701245, _n_(701239, "print", lambda: print), _c_(701244, _a_(701240, "The answer is '{}', with the length of {}.", "format"), _n_(701241, "arr", lambda: arr)[_n_(701242, "index", lambda: index)], _n_(701243, "max", lambda: max)))
        _l_(701246)
        return aux

    #call to function
    _c_(701248, lengthOfLongestSubstring, "aabcdefffgges")
    _l_(701249)