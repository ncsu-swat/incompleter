# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68987451/attributeerror-str-object-has-no-attribute-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(359469)

except ImportError:
    pass
try:
    from googleapiclient import discovery
    _l_(359471)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(359473)

except ImportError:
    pass

credential = 'reference/config.json'
_l_(359474)
api_name = 'sheets'
_l_(359475)
api_version = 'v4'
_l_(359476)
scope = ['https://www.googleapis.com/auth/spreadsheets']
_l_(359477)

service = _c_(359481, _a_(359479, _n_(359478, "discovery", lambda: discovery), "build"), 'sheets','v4',credentials=_n_(359480, "credential", lambda: credential))
_l_(359482)

sheet_id = [_n_(359483, "sheet_id", lambda: sheet_id)]
_l_(359484)
ranges = 'Sheet1!D5:J36'
_l_(359485)

sheet = _c_(359488, _a_(359487, _n_(359486, "service", lambda: service), "spreadsheets"))
_l_(359489)
request = _c_(359496, _a_(359493, _c_(359492, _a_(359491, _n_(359490, "sheet", lambda: sheet), "values")), "get"), spreadsheetId=_n_(359494, "sheet_id", lambda: sheet_id), range=_n_(359495, "ranges", lambda: ranges), majorDimension='ROWS')
_l_(359497)
response = _c_(359500, _a_(359499, _n_(359498, "request", lambda: request), "execute"))
_l_(359501)