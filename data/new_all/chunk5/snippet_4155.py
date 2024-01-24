# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62198079/my-code-is-giving-me-a-type-error-even-though-i-have-taken-care-of-the-type-pl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os, random, re
    _l_(654186)

except ImportError:
    pass
_c_(654189, _a_(654188, _n_(654187, "os", lambda: os), "chdir"), '.\\american date files')
_l_(654190)
for i in _c_(654192, _n_(654191, "range", lambda: range), 20):
    _l_(654209)

    file = _c_(654203, _n_(654193, "open", lambda: open), f'{_c_(654196, _a_(654195, _n_(654194, "random", lambda: random), "randint"), 1, 12)}-{_c_(654199, _a_(654198, _n_(654197, "random", lambda: random), "randint"), 1, 31)}-{_c_(654202, _a_(654201, _n_(654200, "random", lambda: random), "randint"), 2000, 2099)}', 'w')
    _l_(654204)
    _c_(654207, _a_(654206, _n_(654205, 'file', lambda: file), 'close'))
    _l_(654208)
ame_dates = _c_(654212, _a_(654211, _n_(654210, 'os', lambda: os), 'listdir'))
_l_(654213)
ame_date = _c_(654216, _a_(654215, _n_(654214, 're', lambda: re), 'compile'), r'(\d\d?)-(\d\d?)-(\d\d\d\d)')
_l_(654217)
euro_dates = [_c_(654239, _a_(654219, _n_(654218, 'ame_date', lambda: ame_date), 'sub'), f'{_c_(654225, _a_(654224, _c_(654223, _a_(654221, _n_(654220, "ame_date", lambda: ame_date), "search"), _n_(654222, "date", lambda: date)), "group"), 2)}-{_c_(654231, _a_(654230, _c_(654229, _a_(654227, _n_(654226, "ame_date", lambda: ame_date), "search"), _n_(654228, "date", lambda: date)), "group"), 1)}-{_c_(654237, _a_(654236, _c_(654235, _a_(654233, _n_(654232, "ame_date", lambda: ame_date), "search"), _n_(654234, "date", lambda: date)), "group"), 3)}', _n_(654238, 'date', lambda: date)) for date in _n_(654240, 'ame_dates', lambda: ame_dates)]
_l_(654241)
count = 0
_l_(654242)
for dirname, foldername, filename in _c_(654245, _a_(654244, _n_(654243, 'os', lambda: os), 'walk'), r'E:\pranil\python\doing stuff with python\american date files'):
    _l_(654256)

    replacer = _n_(654246, 'euro_dates', lambda: euro_dates)[_n_(654247, 'count', lambda: count)]
    _l_(654248)
    _c_(654253, _a_(654250, _n_(654249, 'os', lambda: os), 'rename'), _n_(654251, 'filename', lambda: filename), _n_(654252, 'replacer', lambda: replacer))
    _l_(654254)
    count += 1
    _l_(654255)