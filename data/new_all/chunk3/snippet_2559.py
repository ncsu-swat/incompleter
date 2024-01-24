# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71639002/supabase-py-typeerror-init-got-an-unexpected-keyword-argument-headers
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from supabase import create_client, Client
    _l_(526254)

except ImportError:
    pass
supabaseUrl = 'REDACTED'
_l_(526255)
supabaseKey = 'REDACTED'
_l_(526256)
supabase = _c_(526260, _n_(526257, "create_client", lambda: create_client), _n_(526258, "supabaseUrl", lambda: supabaseUrl), _n_(526259, "supabaseKey", lambda: supabaseKey))
_l_(526261)
path_data = _c_(526268, _a_(526267, _c_(526266, _a_(526265, _c_(526264, _a_(526263, _n_(526262, "supabase", lambda: supabase), "table"), 'otto'), "select"), '*'), "execute"))
_l_(526269)
_c_(526272, _n_(526270, "print", lambda: print), _n_(526271, "path_data", lambda: path_data))
_l_(526273)