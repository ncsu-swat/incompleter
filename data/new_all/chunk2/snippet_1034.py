# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52546940/attributeerror-type-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class starts:
    _l_(445363)


    def __init__(self, ans, a, b):
        _l_(445362)


        _n_(445346, "self", lambda: self).ans = _c_(445348, _n_(445347, "input", lambda: input), "Please type the operation to do the function as below \n 1. Sum \n 2. Subtract \n 3. multiply \n 4. divide \n")
        _l_(445349)
        _n_(445350, "self", lambda: self).a = _c_(445354, _n_(445351, "int", lambda: int), _c_(445353, _n_(445352, "input", lambda: input), "please enter the number you want to do the operation with : "))
        _l_(445355)
        _n_(445356, "self", lambda: self).b = _c_(445360, _n_(445357, "int", lambda: int), _c_(445359, _n_(445358, "input", lambda: input), "please enter the number you want to do the operation with : "))
        _l_(445361)


class maths(_n_(445364, "starts", lambda: starts)):
    _l_(445410)

    def __init__(self, sum, subtract, divide, multiply):
        _l_(445409)


        _n_(445365, "self", lambda: self).sum = _n_(445366, "sum", lambda: sum)
        _l_(445367)
        _n_(445368, "self", lambda: self).subtract = _n_(445369, "subtract", lambda: subtract)
        _l_(445370)
        _n_(445371, "self", lambda: self).divide = _n_(445372, "divide", lambda: divide)
        _l_(445373)
        _n_(445374, "self", lambda: self).multiply = _n_(445375, "multiply", lambda: multiply)
        _l_(445376)

        def sum(self, a, b):
            _l_(445384)

            _c_(445382, _n_(445377, "print", lambda: print), _a_(445379, _n_(445378, "self", lambda: self), "a") + _a_(445381, _n_(445380, "self", lambda: self), "b"))
            _l_(445383)
    #
        def subtract(self, a, b):
            _l_(445392)

            _c_(445390, _n_(445385, "print", lambda: print), _a_(445387, _n_(445386, "self", lambda: self), "a") - _a_(445389, _n_(445388, "self", lambda: self), "b"))
            _l_(445391)
    #
        def divide(self, a, b):
            _l_(445400)

            _c_(445398, _n_(445393, "print", lambda: print), _a_(445395, _n_(445394, "self", lambda: self), "a") / _a_(445397, _n_(445396, "self", lambda: self), "b"))
            _l_(445399)
    #
        def multiply(self, a, b):
            _l_(445408)

            _c_(445406, _n_(445401, "print", lambda: print), _a_(445403, _n_(445402, "self", lambda: self), "a") * _a_(445405, _n_(445404, "self", lambda: self), "b"))
            _l_(445407)


class operations(_n_(445411, "maths", lambda: maths)):
    _l_(445491)


    def __init__(self, class_a):
        _l_(445490)


        #super(operations,self).__init__(self.ans, self.a, self.b)
        _c_(445420, _a_(445413, _n_(445412, "super", lambda: super)(), "__init__"), _a_(445415, _n_(445414, "self", lambda: self), "ans"), _a_(445417, _n_(445416, "self", lambda: self), "a"), _a_(445419, _n_(445418, "self", lambda: self), "b"))
        _l_(445421)

        _n_(445422, "self", lambda: self).ans = _a_(445424, _n_(445423, "class_a", lambda: class_a), "ans")
        _l_(445425)

        if _a_(445427, _n_(445426, "class_a", lambda: class_a), "ans") == _a_(445429, _n_(445428, "self", lambda: self), "sum"):
            _l_(445489)

            _c_(445439, _n_(445430, "print", lambda: print), _c_(445438, _a_(445433, _a_(445432, _n_(445431, "starts", lambda: starts), "maths"), "sum"), _a_(445435, _n_(445434, "self", lambda: self), "a"), _a_(445437, _n_(445436, "self", lambda: self), "b")))
            _l_(445440)

        elif _a_(445442, _n_(445441, "class_a", lambda: class_a), "ans") == _a_(445444, _n_(445443, "self", lambda: self), "subtract"):
            _l_(445488)

            _c_(445454, _n_(445445, "print", lambda: print), _c_(445453, _a_(445448, _a_(445447, _n_(445446, "starts", lambda: starts), "maths"), "subtract"), _a_(445450, _n_(445449, "self", lambda: self), "a"), _a_(445452, _n_(445451, "self", lambda: self), "b")))
            _l_(445455)

        elif _a_(445457, _n_(445456, "class_a", lambda: class_a), "ans") == _a_(445459, _n_(445458, "self", lambda: self), "divide"):
            _l_(445487)

            _c_(445469, _n_(445460, "print", lambda: print), _c_(445468, _a_(445463, _a_(445462, _n_(445461, "starts", lambda: starts), "maths"), "divide"), _a_(445465, _n_(445464, "self", lambda: self), "a"), _a_(445467, _n_(445466, "self", lambda: self), "b")))
            _l_(445470)

        else:
            _a_(445472, _n_(445471, "class_a", lambda: class_a), "ans") == _a_(445474, _n_(445473, "self", lambda: self), "multiply")
            _l_(445475)
            _c_(445485, _n_(445476, "print", lambda: print), _c_(445484, _a_(445479, _a_(445478, _n_(445477, "starts", lambda: starts), "maths"), "multiply"), _a_(445481, _n_(445480, "self", lambda: self), "a"), _a_(445483, _n_(445482, "self", lambda: self), "b")))
            _l_(445486)


_c_(445495, _a_(445494, _a_(445493, _n_(445492, "starts", lambda: starts), "maths"), "operations"))
_l_(445496)