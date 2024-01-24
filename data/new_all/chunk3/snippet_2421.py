# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43220123/google-calendar-api-filenotfounderror
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(556384)
try:
    from apiclient.discovery import build
    _l_(556386)

except ImportError:
    pass
try:
    from httplib2 import Http
    _l_(556388)

except ImportError:
    pass
try:
    from oauth2client import file, client, tools
    _l_(556390)

except ImportError:
    pass

try:
    _l_(556403)

    import argparse
    _l_(556391)
    flags = _c_(556398, _a_(556397, _c_(556396, _a_(556393, _n_(556392, "argparse", lambda: argparse), "ArgumentParser"), parents=[_a_(556395, _n_(556394, "tools", lambda: tools), "argparser")]), "parse_args"))
    _l_(556399)
except _n_(556400, "ImportError", lambda: ImportError):
    _l_(556402)

    flags = None
    _l_(556401)

SCOPES = 'https://www.googleapis.com/auth/calendar'
_l_(556404)
store = _c_(556407, _a_(556406, _n_(556405, "file", lambda: file), "Storage"), 'storage.json')
_l_(556408)
creds = _c_(556411, _a_(556410, _n_(556409, "store", lambda: store), "get"))
_l_(556412)
if not _n_(556413, "creds", lambda: creds) or _a_(556415, _n_(556414, "creds", lambda: creds), "invalid"):
    _l_(556434)

    flow = _c_(556419, _a_(556417, _n_(556416, "client", lambda: client), "flow_from_clientsecrets"), 'client_secret.json', _n_(556418, "SCOPES", lambda: SCOPES))
    _l_(556420)
    creds = _c_(556426, _a_(556422, _n_(556421, "tools", lambda: tools), "run_flow"), _n_(556423, "flow", lambda: flow), _n_(556424, "store", lambda: store), _n_(556425, "flags", lambda: flags)) \
            if _n_(556427, "flags", lambda: flags) else _c_(556432, _a_(556429, _n_(556428, "tools", lambda: tools), "run"), _n_(556430, "flow", lambda: flow), _n_(556431, "store", lambda: store))
    _l_(556433)
CAL = _c_(556441, _n_(556435, "build", lambda: build), 'calendar', 'v3', http=_c_(556440, _a_(556437, _n_(556436, "creds", lambda: creds), "authorize"), _c_(556439, _n_(556438, "Http", lambda: Http))))
_l_(556442)

GMT_OFF = '-07:00'      # PDT/MST/GMT-7
_l_(556443)      # PDT/MST/GMT-7
EVENT = {
    'summary': 'Dinner with friends',
    'start':  {'dateTime': '2015-09-15T19:00:00%s' % _n_(556444, "GMT_OFF", lambda: GMT_OFF)},
    'end':    {'dateTime': '2015-09-15T22:00:00%s' % _n_(556445, "GMT_OFF", lambda: GMT_OFF)},
    'attendees': [
        {'email': 'friend1@example.com'},
        {'email': 'friend2@example.com'},
    ],
}
_l_(556446)

e = _c_(556454, _a_(556453, _c_(556452, _a_(556450, _c_(556449, _a_(556448, _n_(556447, "CAL", lambda: CAL), "events")), "insert"), calendarId='primary',
        sendNotifications=True, body=_n_(556451, "EVENT", lambda: EVENT)), "execute"))
_l_(556455)

_c_(556462, _n_(556456, "print", lambda: print), '''*** %r event added:
    Start: %s
    End:   %s''' % (_c_(556459, _a_(556458, _n_(556457, "e", lambda: e)['summary'], "encode"), 'utf-8'),
        _n_(556460, "e", lambda: e)['start']['dateTime'], _n_(556461, "e", lambda: e)['end']['dateTime']))
_l_(556463)