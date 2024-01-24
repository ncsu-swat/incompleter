# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60360550/sqlalchemy-multiple-nested-queries-with-filters-from-one-table-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
poste_eu = _c_(650479, _a_(650478, _c_(650477, _a_(650472, _c_(650471, _a_(650438, _a_(650437, _n_(650436, "db", lambda: db), "session"), "query"), _c_(650470, _a_(650469, _c_(650468, _a_(650445, (_a_(650440, _n_(650439, "Sale", lambda: Sale), "id"), _a_(650442, _n_(650441, "Sale", lambda: Sale), "poste"), _a_(650444, _n_(650443, "Sale", lambda: Sale), "pays")), "filter"), _c_(650467, _n_(650446, "or_", lambda: or_), _a_(650448, _n_(650447, "Sale", lambda: Sale), "pays")=='United Kingdom', _a_(650450, _n_(650449, "Sale", lambda: Sale), "pays")=='France', _a_(650452, _n_(650451, "Sale", lambda: Sale), "pays")=='Germany',\
           _a_(650454, _n_(650453, "Sale", lambda: Sale), "pays")=='The Netherlands', _a_(650456, _n_(650455, "Sale", lambda: Sale), "pays")=='Italy', _a_(650458, _n_(650457, "Sale", lambda: Sale), "pays")=='Slovakia', _a_(650460, _n_(650459, "Sale", lambda: Sale), "pays")=='Ireland',\
           _a_(650462, _n_(650461, "Sale", lambda: Sale), "pays")=='Malta', _a_(650464, _n_(650463, "Sale", lambda: Sale), "pays")=='Belgium', _a_(650466, _n_(650465, "Sale", lambda: Sale), "pays")=='Spain')), "label"), 'poste_eu')
    ), "group_by"), _c_(650476, _a_(650475, _a_(650474, _n_(650473, "Sale", lambda: Sale), "id"), "asc"))), "subquery"))
_l_(650480)