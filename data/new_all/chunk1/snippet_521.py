# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55035784/typeerror-can-only-perform-ops-with-scalar-values
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
tables = _c_(386122, _a_(386121, _n_(386120, "pd", lambda: pd), "read_html"), 'https://www.iasplus.com/en/resources/ifrs-topics/use-of-ifrs', header = None)
_l_(386123)

df = _n_(386124, "tables", lambda: tables)[2]
_l_(386125)

_n_(386126, "df", lambda: df).columns = _c_(386130, _a_(386129, _a_(386128, _n_(386127, "df", lambda: df), "columns"), "get_level_values"), 0)  + ":" + _c_(386134, _a_(386133, _a_(386132, _n_(386131, "df", lambda: df), "columns"), "get_level_values"), 1)
_l_(386135)

_c_(386139, _a_(386137, _n_(386136, "sns", lambda: sns), "countplot"), "Domestic unlisted companies:Use of IFRSs by unlisted companies", data=_n_(386138, "df", lambda: df))
_l_(386140)