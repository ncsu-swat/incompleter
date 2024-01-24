# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65175611/attributeerror-list-object-has-no-attribute-sample
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while _n_(546144, "min_number", lambda: min_number) <= _n_(546145, "max_number", lambda: max_number):
        _l_(546181)

        random = _c_(546151, _a_(546147, _n_(546146, "random", lambda: random), "sample"), _c_(546149, _n_(546148, "range", lambda: range), 1, 10), _n_(546150, "min_number", lambda: min_number))
        _l_(546152)
        _c_(546155, _n_(546153, "print", lambda: print), _n_(546154, "random", lambda: random))
        _l_(546156)
        for j in _n_(546157, "random", lambda: random):
                _l_(546178)

                element = _c_(546166, _a_(546159, _n_(546158, "wait", lambda: wait), "until"), _c_(546165, _a_(546161, _n_(546160, "EC", lambda: EC), "element_to_be_clickable"), (_a_(546163, _n_(546162, "By", lambda: By), "XPATH"), f'//*[@id="app"]/div/div[3]/div/div[1]/div[{_n_(546164, "j", lambda: j)}]/div')))
                _l_(546167)
                _c_(546170, _a_(546169, _n_(546168, 'element', lambda: element), 'click'))
                _l_(546171)
                _c_(546174, _a_(546173, _n_(546172, 'time', lambda: time), 'sleep'), 1)
                _l_(546175)
                j += _n_(546176, 'j', lambda: j)
                _l_(546177)

        min_number += _n_(546179, 'min_number', lambda: min_number)
        _l_(546180)