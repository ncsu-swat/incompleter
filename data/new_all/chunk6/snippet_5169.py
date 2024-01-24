# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68987451/attributeerror-str-object-has-no-attribute-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(371951)

except ImportError:
    pass
try:
    from googleapiclient import discovery
    _l_(371953)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(371955)

except ImportError:
    pass

credential = 'reference/config.json'
_l_(371956)
api_name = 'sheets'
_l_(371957)
api_version = 'v4'
_l_(371958)
scope = ['https://www.googleapis.com/auth/spreadsheets']
_l_(371959)

service = _c_(371963, _a_(371961, _n_(371960, "discovery", lambda: discovery), "build"), 'sheets','v4',credentials=_n_(371962, "credential", lambda: credential))
_l_(371964)

sheet_id = [_n_(371965, "sheet_id", lambda: sheet_id)]
_l_(371966)
ranges = 'Sheet1!D5:J36'
_l_(371967)

sheet = _c_(371970, _a_(371969, _n_(371968, "service", lambda: service), "spreadsheets"))
_l_(371971)
request = _c_(371978, _a_(371975, _c_(371974, _a_(371973, _n_(371972, "sheet", lambda: sheet), "values")), "get"), spreadsheetId=_n_(371976, "sheet_id", lambda: sheet_id), range=_n_(371977, "ranges", lambda: ranges), majorDimension='ROWS')
_l_(371979)
response = _c_(371982, _a_(371981, _n_(371980, "request", lambda: request), "execute"))
_l_(371983)