# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2128505/difference-between-filter-and-filter-by-in-sqlalchemy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def filter_by(self, **kwargs):
    _l_(65139)

    aux = _c_(65137, _a_(65132, _n_(65131, "self", lambda: self), "filter"), _c_(65136, _a_(65134, _n_(65133, "sql", lambda: sql), "and_"), **_n_(65135, "kwargs", lambda: kwargs)))
    _l_(65138)
    return aux

_c_(65146, _a_(65145, _c_(65144, _a_(65141, _n_(65140, "session", lambda: session), "query"), _a_(65143, _n_(65142, "db", lambda: db), "users")), "filter_by"), name='Joe', surname='Dodson')
_l_(65147)

_c_(65162, _a_(65153, _c_(65152, _a_(65149, _n_(65148, "session", lambda: session), "query"), _a_(65151, _n_(65150, "db", lambda: db), "users")), "filter"), _c_(65161, _n_(65154, "or_", lambda: or_), _a_(65157, _a_(65156, _n_(65155, "db", lambda: db), "users"), "name")=='Ryan', _a_(65160, _a_(65159, _n_(65158, "db", lambda: db), "users"), "country")=='England'))
_l_(65163)

_c_(65176, _a_(65169, _c_(65168, _a_(65165, _n_(65164, "session", lambda: session), "query"), _a_(65167, _n_(65166, "db", lambda: db), "users")), "filter"), (_a_(65172, _a_(65171, _n_(65170, "db", lambda: db), "users"), "name")=='Ryan') | (_a_(65175, _a_(65174, _n_(65173, "db", lambda: db), "users"), "country")=='England'))
_l_(65177)

_c_(65181, _a_(65180, _a_(65179, _n_(65178, "Users", lambda: Users), "query"), "get"), 123)
_l_(65182)
# And even by a composite PK
_c_(65186, _a_(65185, _a_(65184, _n_(65183, "Users", lambda: Users), "query"), "get"), 123, 321)
_l_(65187)

