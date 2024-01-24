# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20051405/attribute-error-using-biopython-bio-searchio-convert
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Bio import SearchIO
    _l_(601560)

except ImportError:
    pass
try:
    import os
    _l_(601562)

except ImportError:
    pass

blast_out= "some_path"
_l_(601563)
parsed_out="some_path"
_l_(601564)

_c_(601568, _a_(601566, _n_(601565, "os", lambda: os), "chdir"), _n_(601567, "blast_out", lambda: blast_out))
_l_(601569)
all_files = _c_(601573, _a_(601571, _n_(601570, "os", lambda: os), "listdir"), _n_(601572, "blast_out", lambda: blast_out))
_l_(601574)

for single_file in _n_(601575, "all_files", lambda: all_files):
    _l_(601597)

    _c_(601578, _n_(601576, "print", lambda: print), "Current file is: " + _n_(601577, "single_file", lambda: single_file))
    _l_(601579)

    #define handles
    in_file = _n_(601580, "single_file", lambda: single_file)
    _l_(601581)
    in_fmt = 'blast-xml'
    _l_(601582)
    out_file = _n_(601583, "parsed_out", lambda: parsed_out) + _n_(601584, "single_file", lambda: single_file) + '.tab'
    _l_(601585)
    out_fmt = 'blast-tab'
    _l_(601586)
    out_kwarg = {'comments': True}
    _l_(601587)

    _c_(601595, _a_(601589, _n_(601588, "SearchIO", lambda: SearchIO), "convert"), _n_(601590, "in_file", lambda: in_file), _n_(601591, "in_fmt", lambda: in_fmt), _n_(601592, "out_file", lambda: out_file), _n_(601593, "out_fmt", lambda: out_fmt), out_kwargs=_n_(601594, "out_kwarg", lambda: out_kwarg))
    _l_(601596)

_c_(601599, _n_(601598, "print", lambda: print), "\nFinished Parsing File.\n")
_l_(601600)