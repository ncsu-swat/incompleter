# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4697882/how-can-i-find-all-matches-to-a-regular-expression-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(64169, _a_(64168, _n_(64167, "re", lambda: re), "findall"), r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')
_l_(64170)
# Output: ['cats', 'dogs']

[_c_(64173, _a_(64172, _n_(64171, "x", lambda: x), "group")) for x in _c_(64176, _a_(64175, _n_(64174, "re", lambda: re), "finditer"), r'all (.*?) are', 'all cats are smarter than dogs, all dogs are dumber than cats')]
_l_(64177)
# Output: ['all cats are', 'all dogs are']

