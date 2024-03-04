# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/735975/static-methods-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(65028, _a_(65027, _n_(65026, "ClassName", lambda: ClassName), "StaticMethod"))
_l_(65029)

class ClassName(_n_(65030, "object", lambda: object)):
    _l_(65034)


    @_n_(65031, "staticmethod", lambda: staticmethod)
    def static_method(kwarg1=None):
        _l_(65033)

        '''return a value that is a function of kwarg1'''
        _l_(65032)

class ClassName(_n_(65035, "object", lambda: object)):
    _l_(65041)


    def static_method(kwarg1=None):
        _l_(65037)

        '''return a value that is a function of kwarg1'''
        _l_(65036)

    static_method = _c_(65039, _n_(65038, "staticmethod", lambda: staticmethod), static_method)
    _l_(65040)

_c_(65044, _a_(65043, _n_(65042, "ClassName", lambda: ClassName), "static_method"))
_l_(65045)

class ClassName(_n_(65046, "object", lambda: object)):
    _l_(65050)


    @_n_(65047, "classmethod", lambda: classmethod)
    def class_method(cls, kwarg1=None):
        _l_(65049)

        '''return a value that is a function of the class and kwarg1'''
        _l_(65048)

new_instance = _c_(65053, _a_(65052, _n_(65051, "ClassName", lambda: ClassName), "class_method"))
_l_(65054)

new_dict = _c_(65057, _a_(65056, _n_(65055, "dict", lambda: dict), "fromkeys"), ['key1', 'key2'])
_l_(65058)

