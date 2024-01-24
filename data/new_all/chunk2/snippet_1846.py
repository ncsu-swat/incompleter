# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50843421/attributeerror-module-json-has-no-attribute-load-python3-6
#!/usr/bin/env python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import json;
        _l_(427792)

except ImportError:
        pass
_c_(427796, _n_(427793, "print", lambda: print), _a_(427795, _n_(427794, "json", lambda: json), "__file__"))
_l_(427797)
try:
        import sys;
        _l_(427799)

except ImportError:
        pass
try:
        from pprint import pprint;
        _l_(427801)

except ImportError:
        pass

with _c_(427803, _n_(427802, "open", lambda: open), 'services.json') as f:
        _l_(427809)

        data=_c_(427807, _a_(427805, _n_(427804, "json", lambda: json), "load"), _n_(427806, "f", lambda: f));
        _l_(427808)

_c_(427812, _n_(427810, "pprint", lambda: pprint), _n_(427811, "data", lambda: data));
_l_(427813)