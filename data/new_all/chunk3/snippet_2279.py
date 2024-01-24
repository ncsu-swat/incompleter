# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53651955/nameerror-name-is-not-defined-a-variable-defined-if-a-conditon-is-met
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def collect_data(text):
    _l_(544839)

    for line in _n_(544803, "text", lambda: text):
        _l_(544838)

        key, match = _c_(544806, _n_(544804, "parse_lines", lambda: parse_lines), _n_(544805, "line", lambda: line)) #here I am parsing using a dict and regular expressions
        _l_(544807) #here I am parsing using a dict and regular expressions

        if _n_(544808, "key", lambda: key) == _n_(544809, "something_1", lambda: something_1):
            _l_(544837)

            var1 = _c_(544812, _a_(544811, _n_(544810, "match", lambda: match), "group"), 1)
            _l_(544813)
            _c_(544817, _a_(544815, _n_(544814, "list1", lambda: list1), "append"), _n_(544816, "var1", lambda: var1))
            _l_(544818)

        elif _n_(544819, "key", lambda: key) == _n_(544820, "something_2", lambda: something_2):
            _l_(544836)

            var2 = _c_(544823, _a_(544822, _n_(544821, "match", lambda: match), "group"), 2)
            _l_(544824)
            _c_(544828, _a_(544826, _n_(544825, "list2", lambda: list2), "append"), _n_(544827, "var2", lambda: var2))
            _l_(544829)

        elif _n_(544830, "key", lambda: key) == _n_(544831, "something_3", lambda: something_3):
            _l_(544835)

            _c_(544833, _n_(544832, "func", lambda: func))
            _l_(544834)

def func():
    _l_(544856)

    for element in _n_(544840, "elements", lambda: elements) :
        _l_(544855)

        if _n_(544841, "element", lambda: element) == _n_(544842, "element1", lambda: element1):
            _l_(544854)

            variation = _c_(544845, _n_(544843, "float", lambda: float), _n_(544844, "var1", lambda: var1))
            _l_(544846)
        elif _n_(544847, "element", lambda: element) == _n_(544848, "element2", lambda: element2):
            _l_(544853)

            variation = _c_(544851, _n_(544849, "float", lambda: float), _n_(544850, "var2", lambda: var2))
            _l_(544852)
_c_(544859, _n_(544857, "collect_data", lambda: collect_data), _n_(544858, "text", lambda: text))
_l_(544860)