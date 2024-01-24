# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/19285014/python-name-error-name-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main():
    _l_(382815)

    D = {} #create empty dictionary
    _l_(382786) #create empty dictionary
    for x in _c_(382788, _n_(382787, "open", lambda: open), 'wvtc_data.txt'):
        _l_(382814)

        key, name, email, record = _c_(382793, _a_(382792, _c_(382791, _a_(382790, _n_(382789, "x", lambda: x), "strip")), "split"), ':')
        _l_(382794)
        key = _c_(382797, _n_(382795, "int", lambda: int), _n_(382796, "key", lambda: key)) #convert key from string to integer
        _l_(382798) #convert key from string to integer
        _n_(382799, "D", lambda: D)[_n_(382800, "key", lambda: key)] = {} #initialize key value with empty dictionary
        _l_(382801) #initialize key value with empty dictionary
        _n_(382802, "D", lambda: D)[_n_(382803, "key", lambda: key)]['name'] = _n_(382804, "name", lambda: name)
        _l_(382805)
        _n_(382806, "D", lambda: D)[_n_(382807, "key", lambda: key)]['email'] = _n_(382808, "email", lambda: email)
        _l_(382809)
        _n_(382810, "D", lambda: D)[_n_(382811, "key", lambda: key)]['record'] = _n_(382812, "record", lambda: record)
        _l_(382813)

_c_(382818, _n_(382816, "print", lambda: print), _n_(382817, "D", lambda: D)[106]['name'])
_l_(382819)
_c_(382822, _n_(382820, "print", lambda: print), _n_(382821, "D", lambda: D)[110]['email'])
_l_(382823)
_c_(382825, _n_(382824, "main", lambda: main))
_l_(382826)