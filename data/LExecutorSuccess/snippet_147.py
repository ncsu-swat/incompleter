# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
person = {'name': 'Mary', 'age': 25}
_l_(1548759)
one_year_later = {**_n_(1548760, "person", lambda: person), 'age': 26}  # does not mutate person dict
_l_(1548761)  # does not mutate person dict

one_year_later = _c_(1548764, _n_(1548762, "dict", lambda: dict), _n_(1548763, "person", lambda: person), age=26)
_l_(1548765)

