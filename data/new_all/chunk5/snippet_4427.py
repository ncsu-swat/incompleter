# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57786570/typeerror-list-indices-must-be-integers-or-slices-not-str-using-python-3-7
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from operator import itemgetter
    _l_(673885)

except ImportError:
    pass
balance = 1000
_l_(673886)
name = "Charles De."
_l_(673887)
acc_no = "1235621234"
_l_(673888)

_c_(673895, _n_(673889, "print", lambda: print), "Name: ",_n_(673890, "name", lambda: name),   "Account: ", _n_(673891, "acc_no", lambda: acc_no), "Original Balance: ", "$" + 
_c_(673894, _n_(673892, "str", lambda: str), _n_(673893, "balance", lambda: balance)))
_l_(673896)
charges_list = []
_l_(673897)
charges_dict = []
_l_(673898)
for charge_string in _c_(673900, _n_(673899, "open", lambda: open), "market.txt"):
    _l_(673907)

    charge_info_list = _c_(673905, _a_(673904, _c_(673903, _a_(673902, _n_(673901, "charge_string", lambda: charge_string), "strip")), "split"), ',')
    _l_(673906)

charge_info = _c_(673909, _n_(673908, "dict", lambda: dict))
_l_(673910)
_n_(673911, "charge_info", lambda: charge_info)['vendor'] = _n_(673912, "charge_info_list", lambda: charge_info_list)[0]
_l_(673913)
_n_(673914, "charge_info", lambda: charge_info)['date'] = _n_(673915, "charge_info_list", lambda: charge_info_list)[1]
_l_(673916)
_n_(673917, "charge_info", lambda: charge_info)['charge'] = _n_(673918, "charge_info_list", lambda: charge_info_list)[2]
_l_(673919)

_c_(673923, _a_(673921, _n_(673920, "charges_list", lambda: charges_list), "append"), _n_(673922, "charge_info", lambda: charge_info))
_l_(673924)

if _n_(673925, "charge_info", lambda: charge_info)['vendor'] not in _n_(673926, "charges_dict", lambda: charges_dict):
    _l_(673932)

    _n_(673927, "charges_dict", lambda: charges_dict)[_n_(673928, "charge_info", lambda: charge_info)['vendor']] = _c_(673930, _n_(673929, "list", lambda: list))
    _l_(673931)

_c_(673937, _a_(673935, _n_(673933, "charges_dict", lambda: charges_dict)[_n_(673934, "charge_info", lambda: charge_info)['vendor']], "append"), _n_(673936, "charge_info", lambda: charge_info))
_l_(673938)
charges_sorted_by_date = _c_(673943, _n_(673939, "sorted", lambda: sorted), _n_(673940, "charges_list", lambda: charges_list), key=_c_(673942, _n_(673941, "itemgetter", lambda: itemgetter), 'date'))
_l_(673944)