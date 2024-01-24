# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68554023/typeerror-init-subclass-takes-no-keyword-arguments-related-to-subclass-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from abc import ABC, abstractmethod
    _l_(394145)

except ImportError:
    pass

class Pipeline(_n_(394146, "ABC", lambda: ABC)):
    _l_(394162)


    @_n_(394147, "abstractmethod", lambda: abstractmethod)
    def read_data(self):
        _l_(394149)

        pass
        _l_(394148)
    
    def __init__(self, **kwargs):
        _l_(394161)

        _n_(394150, "self", lambda: self).raw_data = _c_(394153, _a_(394152, _n_(394151, "self", lambda: self), "read_data"))        
        _l_(394154)        
        _n_(394155, "self", lambda: self).process_data = _a_(394157, _n_(394156, "self", lambda: self), "raw_data")[_a_(394159, _n_(394158, "self", lambda: self), "used_cols")]
        _l_(394160)

   
class case1(_n_(394163, "Pipeline", lambda: Pipeline)):
    _l_(394172)

    def read_data(self):
        _l_(394168)

        aux = _c_(394166, _a_(394165, _n_(394164, "pd", lambda: pd), "read_csv"), "file location") # just hard coding for the file location
        _l_(394167) # just hard coding for the file location
        return aux # just hard coding for the file location
       
    @_n_(394169, "property", lambda: property)
    def used_cols(self):
        _l_(394171)

        aux = ['col_1', 'col_2','col_3','col_4']
        _l_(394170)
        return aux