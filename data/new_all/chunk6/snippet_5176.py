# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67336013/name-error-self-not-defined-when-calling-a-function-to-create-in-class-vari
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Documents:
    _l_(357725)

    def __init__(self, input_file):
        _l_(357708)

        _n_(357693, "self", lambda: self).input_file_ = _n_(357694, "input_file", lambda: input_file) #List in which each element is a list of tokens
        _l_(357695) #List in which each element is a list of tokens
        
        assert _c_(357699, _n_(357696, "type", lambda: type), _a_(357698, _n_(357697, "self", lambda: self), "input_file_")) is _n_(357700, "list", lambda: list), 'Input file is not a list'
        _l_(357701)
        assert _c_(357705, _n_(357702, "type", lambda: type), _a_(357704, _n_(357703, "self", lambda: self), "input_file_")[0]) is _n_(357706, "list", lambda: list), 'Elements in input file are not lists' #Only checks first instance, not all. But should suffice
        _l_(357707) #Only checks first instance, not all. But should suffice
    def get_vocabulary(self):
        _l_(357721)

        vocabulary = _c_(357714, _n_(357709, "set", lambda: set), [_n_(357710, "el", lambda: el) for lis in _a_(357712, _n_(357711, "self", lambda: self), "input_file_") for el in _n_(357713, "lis", lambda: lis)])
        _l_(357715)
        aux = _n_(357716, "vocabulary", lambda: vocabulary), _c_(357719, _n_(357717, "len", lambda: len), _n_(357718, "vocabulary", lambda: vocabulary)) 
        _l_(357720) 
        return aux 
    
    vocabulary, vocabulary_size = _c_(357723, _a_(357722, self, "get_vocabulary"))
    _l_(357724)