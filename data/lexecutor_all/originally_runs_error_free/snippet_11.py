# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/136097/difference-between-staticmethod-and-classmethod
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Apple:
    _l_(1547662)


    _counter = 0
    _l_(1547634)

    @_n_(1547635, "staticmethod", lambda: staticmethod)
    def about_apple():
        _l_(1547639)

        _c_(1547637, _n_(1547636, "print", lambda: print), 'Apple is good for you.')
        _l_(1547638)

    @_n_(1547640, "classmethod", lambda: classmethod)
    def make_apple_juice(cls, number_of_apples):
        _l_(1547653)

        _c_(1547642, _n_(1547641, "print", lambda: print), 'Making juice:')
        _l_(1547643)
        for i in _c_(1547646, _n_(1547644, "range", lambda: range), _n_(1547645, "number_of_apples", lambda: number_of_apples)):
            _l_(1547652)

            _c_(1547650, _a_(1547648, _n_(1547647, "cls", lambda: cls), "_juice_this"), _n_(1547649, "i", lambda: i))
            _l_(1547651)

    @_n_(1547654, "classmethod", lambda: classmethod)
    def _juice_this(cls, apple):
        _l_(1547661)

        _c_(1547657, _n_(1547655, "print", lambda: print), 'Juicing apple %d...' % _n_(1547656, "apple", lambda: apple))
        _l_(1547658)
        _n_(1547659, "cls", lambda: cls)._counter += 1
        _l_(1547660)

