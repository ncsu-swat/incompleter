# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39069353/filenotfounderror-pointing-to-the-wrong-drive-letter-using-pythons-df2gspread
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from df2gspread import df2gspread as d2g
    _l_(449019)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(449021)

except ImportError:
    pass

df = _c_(449023, _n_(449022, "live_data", lambda: live_data))
_l_(449024)
spreadsheet = 'my_spreadsheet_key'
_l_(449025)
wks_name = 'my_sheet_name'
_l_(449026)
_c_(449032, _a_(449028, _n_(449027, "d2g", lambda: d2g), "upload"), _n_(449029, "df", lambda: df), _n_(449030, "spreadsheet", lambda: spreadsheet), _n_(449031, "wks_name", lambda: wks_name))
_l_(449033)