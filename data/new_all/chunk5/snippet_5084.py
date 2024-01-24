# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73656349/typeerror-list-indices-must-be-integers-or-slices-not-str-when-i-try-to-iterat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
colloquial_numbers = ['veinti[\\s|-|]tres', 'veinti[\\s|-|]dos', 'veinti[\\s|-|]uno', 'veinte', 'tres', 'dos', 'uno']
_l_(683776)

symbolic_numbers = ['23', '22', '21', '20', '3', '2', '1']
_l_(683777)

body = ''
_l_(683778)
for n in _n_(683779, "coloquial_numbers", lambda: coloquial_numbers):
    _l_(683787)

    body += _c_(683785, _a_(683780, """    input_text = re.sub(r"{}", "{}", input_text)\n""", "format"), _n_(683781, "coloquial_numbers", lambda: coloquial_numbers)[_n_(683782, "n", lambda: n)], _n_(683783, "symbolic_numbers", lambda: symbolic_numbers)[_n_(683784, "n", lambda: n)])
    _l_(683786)

_c_(683792, _n_(683788, "print", lambda: print), _c_(683791, _n_(683789, "repr", lambda: repr), _n_(683790, "body", lambda: body)))
_l_(683793)