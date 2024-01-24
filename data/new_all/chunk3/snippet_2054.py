# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66219990/typeerror-string-indices-must-be-integer-while-retrieving-a-data-from-google-sh
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(522567)
try:
    import json
    _l_(522569)

except ImportError:
    pass
try:
    import os.path
    _l_(522571)

except ImportError:
    pass
try:
    import pymssql
    _l_(522573)

except ImportError:
    pass
try:
    import pickle
    _l_(522575)

except ImportError:
    pass
try:
    import get_sec
    _l_(522577)

except ImportError:
    pass
try:
    from googleapiclient.discovery import build
    _l_(522579)

except ImportError:
    pass
try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    _l_(522581)

except ImportError:
    pass
try:
    from google.auth.transport.requests import Request
    _l_(522583)

except ImportError:
    pass

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
_l_(522584)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "spread_sheet_id"
_l_(522585)
SAMPLE_RANGE_NAME = "sample!A:E"
_l_(522586)
credentials = _c_(522588, _n_(522587, "get_sec", lambda: get_sec), "matrix_metrics")
_l_(522589)
with _c_(522591, _n_(522590, "open", lambda: open), 'credentials.json', 'w') as f:
    _l_(522598)

    _c_(522596, _a_(522593, _n_(522592, "json", lambda: json), "dump"), _n_(522594, "credentials", lambda: credentials), _n_(522595, "f", lambda: f), ensure_ascii=False, indent=4)
    _l_(522597)

f = _c_(522600, _n_(522599, "open", lambda: open), "credentials.json", "r")
_l_(522601)
_c_(522606, _n_(522602, "print", lambda: print), _c_(522605, _a_(522604, _n_(522603, "f", lambda: f), "read")))
_l_(522607)

def main():
    _l_(522685)

    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    _l_(522608)
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if _c_(522611, _a_(522610, _a_(522609, os, "path"), "exists"), "token.pickle"):
        _l_(522620)

        with _c_(522613, _n_(522612, "open", lambda: open), "token.pickle", "rb") as token:
            _l_(522619)

            creds = _c_(522617, _a_(522615, _n_(522614, "pickle", lambda: pickle), "load"), _n_(522616, "token", lambda: token))
            _l_(522618)
    # If there are no (valid) credentials available, let the user log in.
    if not _n_(522621, "creds", lambda: creds) or not _a_(522623, _n_(522622, "creds", lambda: creds), "valid"):
        _l_(522654)

        if _n_(522624, "creds", lambda: creds) and _a_(522626, _n_(522625, "creds", lambda: creds), "expired") and _a_(522628, _n_(522627, "creds", lambda: creds), "refresh_token"):
            _l_(522644)

            _c_(522633, _a_(522630, _n_(522629, "creds", lambda: creds), "refresh"), _c_(522632, _n_(522631, "Request", lambda: Request)))
            _l_(522634)
        else:
            flow = _c_(522638, _a_(522636, _n_(522635, "InstalledAppFlow", lambda: InstalledAppFlow), "from_client_secrets_file"), "credentials.json", _n_(522637, "SCOPES", lambda: SCOPES)
            )
            _l_(522639)
            creds = _c_(522642, _a_(522641, _n_(522640, "flow", lambda: flow), "run_local_server"), port=0)
            _l_(522643)
        # Save the credentials for the next run
        with _c_(522646, _n_(522645, "open", lambda: open), "token.pickle", "wb") as token:
            _l_(522653)

            _c_(522651, _a_(522648, _n_(522647, "pickle", lambda: pickle), "dump"), _n_(522649, "creds", lambda: creds), _n_(522650, "token", lambda: token))
            _l_(522652)

    service = _c_(522657, _n_(522655, "build", lambda: build), "sheets", "v4", credentials=_n_(522656, "creds", lambda: creds))
    _l_(522658)

    # Call the Sheets API
    sheet = _c_(522661, _a_(522660, _n_(522659, "service", lambda: service), "spreadsheets"))
    _l_(522662)
    result = _c_(522671, _a_(522670, _c_(522669, _a_(522666, _c_(522665, _a_(522664, _n_(522663, "sheet", lambda: sheet), "values")), "get"), spreadsheetId=_n_(522667, "SAMPLE_SPREADSHEET_ID", lambda: SAMPLE_SPREADSHEET_ID), range=_n_(522668, "SAMPLE_RANGE_NAME", lambda: SAMPLE_RANGE_NAME)), "execute"))
    _l_(522672)
    values = _c_(522675, _a_(522674, _n_(522673, "result", lambda: result), "get"), "values", [])
    _l_(522676)

    if not _n_(522677, "values", lambda: values):
        _l_(522684)

        _c_(522679, _n_(522678, "print", lambda: print), "No data found.")
        _l_(522680)
    else:
        _c_(522682, _n_(522681, "print", lambda: print), "Major")
        _l_(522683)