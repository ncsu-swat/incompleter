# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50089536/typeerror-integer-argument-expected-got-float-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import string
    _l_(425920)

except ImportError:
    pass

f = _c_(425922, _n_(425921, "open", lambda: open), 'data/hamlet.txt', 'r')
_l_(425923)
text = _c_(425926, _a_(425925, _n_(425924, "f", lambda: f), "read"))
_l_(425927)

alphabet_freq = []
_l_(425928)

for c in _a_(425930, _n_(425929, "string", lambda: string), "ascii_lowercase") :
    _l_(425945)

    _c_(425943, _a_(425932, _n_(425931, "alphabet_freq", lambda: alphabet_freq), "append"), _c_(425936, _a_(425934, _n_(425933, "text", lambda: text), "count"), _n_(425935, "c", lambda: c)) + _c_(425942, _a_(425938, _n_(425937, "text", lambda: text), "count"), _c_(425941, _a_(425940, _n_(425939, "c", lambda: c), "upper"))))
    _l_(425944)

alphabet_freq_sum = 0
_l_(425946)

for _ in _n_(425947, "alphabet_freq", lambda: alphabet_freq) :
    _l_(425950)

    alphabet_freq_sum +=_n_(425948, "_", lambda: _)
    _l_(425949)

letter_frequency = []
_l_(425951)

for _ in _n_(425952, "alphabet_freq", lambda: alphabet_freq) :
    _l_(425959)

    _c_(425957, _a_(425954, _n_(425953, "letter_frequency", lambda: letter_frequency), "append"), ( _n_(425955, "_", lambda: _) / _n_(425956, "alphabet_freq_sum", lambda: alphabet_freq_sum)) * 100)
    _l_(425958)

alphabets = _c_(425963, _n_(425960, "list", lambda: list), _a_(425962, _n_(425961, "string", lambda: string), "ascii_lowercase"))
_l_(425964)

letter_frequency_in_freq_order = []
_l_(425965)

for _ in _n_(425966, "letter_frequency", lambda: letter_frequency) :
    _l_(425977)

    _c_(425975, _a_(425968, _n_(425967, "letter_frequency_in_freq_order", lambda: letter_frequency_in_freq_order), "append"), _c_(425974, _a_(425970, _n_(425969, "letter_frequency", lambda: letter_frequency), "pop"), _c_(425973, _n_(425971, "max", lambda: max), _n_(425972, "letter_frequency", lambda: letter_frequency))))
    _l_(425976)

_c_(425981, _n_(425978, "print", lambda: print), _n_(425979, "letter_frequency_in_freq_order", lambda: letter_frequency_in_freq_order),_n_(425980, "letter_frequency", lambda: letter_frequency))
_l_(425982)