# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71344431/lambda-helper-function-with-typeerror-not-supported-between-instances-of-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def search_clinic(search, array):
    _l_(591874)

    new_array = []
    _l_(591824)
    exact_match = []
    _l_(591825)
    partial_match = []
    _l_(591826)
    no_match = []
    _l_(591827)
    # finding mathces and storing them
    for clinic in _n_(591828, "array", lambda: array):
        _l_(591850)

        if _n_(591829, "search", lambda: search) == _n_(591830, "clinic", lambda: clinic):
            _l_(591849)

            _c_(591834, _a_(591832, _n_(591831, "exact_match", lambda: exact_match), "append"), _n_(591833, "clinic", lambda: clinic))
            _l_(591835)
        elif _n_(591836, "search", lambda: search) in _n_(591837, "clinic", lambda: clinic):
            _l_(591848)

            _c_(591841, _a_(591839, _n_(591838, "partial_match", lambda: partial_match), "append"), _n_(591840, "clinic", lambda: clinic))
            _l_(591842)
        else:
            _c_(591846, _a_(591844, _n_(591843, "no_match", lambda: no_match), "append"), _n_(591845, "clinic", lambda: clinic))
            _l_(591847)
    # ordering the stored values to one array 
    for clinic in _n_(591851, "exact_match", lambda: exact_match):
        _l_(591857)

        _c_(591855, _a_(591853, _n_(591852, "new_array", lambda: new_array), "append"), _n_(591854, "clinic", lambda: clinic))
        _l_(591856)
    for clinic in _n_(591858, "partial_match", lambda: partial_match):
        _l_(591864)

        _c_(591862, _a_(591860, _n_(591859, "new_array", lambda: new_array), "append"), _n_(591861, "clinic", lambda: clinic))
        _l_(591863)
    for clinic in _n_(591865, "no_match", lambda: no_match):
        _l_(591871)

        _c_(591869, _a_(591867, _n_(591866, "new_array", lambda: new_array), "append"), _n_(591868, "clinic", lambda: clinic))
        _l_(591870)
    aux = _n_(591872, "new_array", lambda: new_array)
    _l_(591873)
    return aux
#O(n) linear function   
_c_(591878, _n_(591875, "print", lambda: print), _c_(591877, _n_(591876, "search_clinic", lambda: search_clinic), 'care corp', ['healthcare corp', 'healthcare group', 'care corp', "345gyht", "zelthcare corp", "zelthcare group"]))
_l_(591879)

# I was unsatisfied with the above solution and went back to attempting to use key= 
def helper(clinic, search):
    _l_(591893)

    if _c_(591883, _a_(591881, _n_(591880, "clinic", lambda: clinic), "find"), _n_(591882, "search", lambda: search)) != -1:
        _l_(591892)

        _c_(591887, _a_(591885, _n_(591884, "clinic", lambda: clinic), "find"), _n_(591886, "search", lambda: search))
        _l_(591888)
        aux = _c_(591890, _n_(591889, "float", lambda: float), 'inf')
        _l_(591891)
        # use inf to push clinics without search to end of the list
        return aux
def search_clinic2(search, array):
    _l_(591902)

    aux = _c_(591900, _n_(591894, "sorted", lambda: sorted), _n_(591895, "array", lambda: array), key= lambda clinic: _c_(591899, _n_(591896, "helper", lambda: helper), _n_(591897, "clinic", lambda: clinic), _n_(591898, "search", lambda: search)))
    _l_(591901)
    return aux

_c_(591906, _n_(591903, "print", lambda: print), _c_(591905, _n_(591904, "search_clinic2", lambda: search_clinic2), 'care corp', ['healthcare corp', 'healthcare group', 'care corp', "345gyht", "zelthcare corp", "zelthcare group"]))
_l_(591907)