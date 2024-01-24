# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39767292/unhashable-type-error-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
text = _c_(568018, _a_(568015, _n_(568014, "pd", lambda: pd), "read_sql"), _n_(568016, "select_string", lambda: select_string), _n_(568017, "con", lambda: con))
_l_(568019)
ftext = _c_(568023, _a_(568022, _a_(568021, _n_(568020, "text", lambda: text)['SomeText'], "str"), "split"))
_l_(568024)
country_codes = _c_(568027, _a_(568026, _n_(568025, "pd", lambda: pd), "read_csv"), 'wikipedia-iso-country-codes.csv')
_l_(568028)
ccs = _c_(568031, _n_(568029, "set", lambda: set), _n_(568030, "country_codes", lambda: country_codes)['English short name lower case'])
_l_(568032)
for country in _n_(568033, "ftext", lambda: ftext):
    _l_(568041)

    if _n_(568034, "country", lambda: country) in _n_(568035, "ccs", lambda: ccs):
        _l_(568040)

        _c_(568038, _n_(568036, "print", lambda: print), _n_(568037, "country", lambda: country)+'  is in the text')
        _l_(568039)