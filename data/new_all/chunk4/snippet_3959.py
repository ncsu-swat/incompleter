# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64841890/dataframe-to-google-spreadsheet-typeerror-dataframe-objects-are-mutable-th
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(600716)

except ImportError:
    pass
try:
    from oauth2client.service_account import ServiceAccountCredentials
    _l_(600718)

except ImportError:
    pass
try:
    import numpy as np
    _l_(600720)

except ImportError:
    pass
try:
    import gspread
    _l_(600722)

except ImportError:
    pass
try:
    from googleapiclient import discovery
    _l_(600724)

except ImportError:
    pass

data = [['Alex',10],['Bob',12],['Clarke',13]]
_l_(600725)
df = _c_(600729, _a_(600727, _n_(600726, "pd", lambda: pd), "DataFrame"), _n_(600728, "data", lambda: data),columns=['Name','Age'])
_l_(600730)
_c_(600733, _n_(600731, "print", lambda: print), _n_(600732, "df", lambda: df))
_l_(600734)

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
_l_(600735)
credentials = _c_(600739, _a_(600737, _n_(600736, "ServiceAccountCredentials", lambda: ServiceAccountCredentials), "from_json_keyfile_name"), 'cred.json', _n_(600738, "scope", lambda: scope))
_l_(600740)
client = _c_(600744, _a_(600742, _n_(600741, "gspread", lambda: gspread), "authorize"), _n_(600743, "credentials", lambda: credentials))
_l_(600745)
sheet = _a_(600749, _c_(600748, _a_(600747, _n_(600746, "client", lambda: client), "open"), 'SpreadsheetName'), "sheet1")
_l_(600750)

sheets_service = _c_(600754, _a_(600752, _n_(600751, "discovery", lambda: discovery), "build"), 'sheets','v4',credentials=_n_(600753, "credentials", lambda: credentials))
_l_(600755)
sheets = _c_(600758, _a_(600757, _n_(600756, "sheets_service", lambda: sheets_service), "spreadsheets"))
_l_(600759)
spreadsheet_id = '************************'
_l_(600760)


def df_to_sheet(df):
    _l_(600782)

    df_columns = [_c_(600765, _a_(600762, _n_(600761, "np", lambda: np), "array"), _a_(600764, _n_(600763, "df", lambda: df), "columns"))]
    _l_(600766)
    df_values = _c_(600770, _a_(600769, _a_(600768, _n_(600767, "df", lambda: df), "values"), "tolist"))
    _l_(600771)
    df_to_sheet = _c_(600778, _a_(600777, _c_(600776, _a_(600773, _n_(600772, "np", lambda: np), "concatenate"), (_n_(600774, "df_columns", lambda: df_columns), _n_(600775, "df_values", lambda: df_values))), "tolist"))
    _l_(600779)
    aux = _n_(600780, "df_to_sheet", lambda: df_to_sheet)
    _l_(600781)
    return aux

data = [
    {
        "title": "Unique URL",
        "df": _c_(600785, _a_(600784, _n_(600783, "pd", lambda: pd), "DataFrame"), {})
    }
]
_l_(600786)
update_body = {
        "valueInputOption": "RAW",
        "data": _c_(600800, _n_(600787, "list", lambda: list), _c_(600799, _n_(600788, "map", lambda: map), lambda d: {"range": _c_(600791, _a_(600790, _n_(600789, "d", lambda: d), "get"), "title"), "values": _c_(600797, _n_(600792, "df_to_sheet", lambda: df_to_sheet), _c_(600796, _a_(600794, _n_(600793, "d", lambda: d), "get"), _n_(600795, "df", lambda: df)))}, _n_(600798, "data", lambda: data)))
    }
_l_(600801)
_c_(600810, _a_(600809, _c_(600808, _a_(600805, _c_(600804, _a_(600803, _n_(600802, "sheets", lambda: sheets), "values")), "batchUpdate"), spreadsheetId=_n_(600806, "spreadsheet_id", lambda: spreadsheet_id), body=_n_(600807, "update_body", lambda: update_body)), "execute"))
_l_(600811)