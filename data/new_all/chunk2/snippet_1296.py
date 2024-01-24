# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54003962/typeerror-nonetype-object-is-not-iterable-when-applying-decorator-to-generato
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def decor(func):
    _l_(453522)

    def wrapper(*args, **kwargs):
        _l_(453519)

        func_name = _a_(453495, _n_(453494, "func", lambda: func), "__name__")
        _l_(453496)
        is_generator = "_generator" in _n_(453497, "func_name", lambda: func_name)
        _l_(453498)
        if _n_(453499, "is_generator", lambda: is_generator):
            _l_(453518)

            for item in _c_(453503, _n_(453500, "func", lambda: func), *_n_(453501, "args", lambda: args), **_n_(453502, "kwargs", lambda: kwargs)):
                _l_(453508)

                _c_(453506, _n_(453504, "print", lambda: print), _n_(453505, "item", lambda: item))
                _l_(453507)
        else:
            res = _c_(453512, _n_(453509, "func", lambda: func), *_n_(453510, "args", lambda: args), **_n_(453511, "kwargs", lambda: kwargs))
            _l_(453513)
            _c_(453516, _n_(453514, "print", lambda: print), _n_(453515, "res", lambda: res))
            _l_(453517)
    aux = _n_(453520, "wrapper", lambda: wrapper)
    _l_(453521)
    return aux

@_n_(453523, "decor", lambda: decor)            
def f():
    _l_(453525)

    aux = "a"
    _l_(453524)
    return aux

@_n_(453526, "decor", lambda: decor)    
def f_generator():
    _l_(453531)

    for i in _c_(453528, _n_(453527, "range", lambda: range), 2):
        _l_(453530)

        yield "b"
        _l_(453529)

_c_(453533, _n_(453532, "f", lambda: f))
_l_(453534)

""" Output: a """

for item in _c_(453536, _n_(453535, "f_generator", lambda: f_generator)):
    _l_(453541)

    _c_(453539, _n_(453537, "print", lambda: print), "Processing item ", _n_(453538, "item", lambda: item))
    _l_(453540)

"""
Output:
b
b
Traceback (most recent call last):
  File "test.py", line 27, in <module>
      for item in f_generator():
TypeError: 'NoneType' object is not iterable
"""