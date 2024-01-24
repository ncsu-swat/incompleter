# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49933670/extracting-field-typeerror-string-indices-must-be-integers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def validate_file(f):
    _l_(561570)

    #print('File Header Validation:')

    fname=_c_(561559, _n_(561557, "open", lambda: open), _n_(561558, "f", lambda: f))
    _l_(561560)
    count=0
    _l_(561561)
    for line in _n_(561562, "fname", lambda: fname):
        _l_(561569)

        if 'length' in _n_(561563, "line", lambda: line):
            _l_(561568)

            _c_(561566, _n_(561564, "print", lambda: print), _n_(561565, "line", lambda: line)['length'])
            _l_(561567)


_c_(561572, _n_(561571, "validate_file", lambda: validate_file), "test1.log")
_l_(561573)