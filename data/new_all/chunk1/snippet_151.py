# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56716818/nameerror-name-mediaiobasedownload-is-not-defined
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(419373)
try:
    import pickle
    _l_(419375)

except ImportError:
    pass
try:
    import os.path
    _l_(419377)

except ImportError:
    pass
try:
    import io
    _l_(419379)

except ImportError:
    pass
try:
    from googleapiclient.discovery import build
    _l_(419381)

except ImportError:
    pass
try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    _l_(419383)

except ImportError:
    pass
try:
    from google.auth.transport.requests import Request
    _l_(419385)

except ImportError:
    pass

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
_l_(419386)

def downloadFile(driveService, fileId):
    _l_(419418)

    request = _c_(419392, _a_(419390, _c_(419389, _a_(419388, _n_(419387, "driveService", lambda: driveService), "files")), "get_media"), fileId=_n_(419391, "fileId", lambda: fileId))
    _l_(419393)
    fh = _c_(419396, _a_(419395, _n_(419394, "io", lambda: io), "BytesIO"))
    _l_(419397)
    #fh = io.FileIO(fileId + '.mp4', 'wb')
    downloader = _c_(419401, _n_(419398, "MediaIoBaseDownload", lambda: MediaIoBaseDownload), _n_(419399, "fh", lambda: fh), _n_(419400, "request", lambda: request))
    _l_(419402)
    done = False
    _l_(419403)
    while _n_(419404, "done", lambda: done) is False:
        _l_(419417)

        status, done = _c_(419407, _a_(419406, _n_(419405, "downloader", lambda: downloader), "next_chunk"))
        _l_(419408)
        _c_(419415, _n_(419409, "print", lambda: print), "Download %d%%." % _c_(419414, _n_(419410, "int", lambda: int), _c_(419413, _a_(419412, _n_(419411, "status", lambda: status), "progress")) * 100))
        _l_(419416)

def main():
    _l_(419504)

    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    _l_(419419)
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if _c_(419422, _a_(419421, _a_(419420, os, "path"), "exists"), 'token.pickle'):
        _l_(419431)

        with _c_(419424, _n_(419423, "open", lambda: open), 'token.pickle', 'rb') as token:
            _l_(419430)

            creds = _c_(419428, _a_(419426, _n_(419425, "pickle", lambda: pickle), "load"), _n_(419427, "token", lambda: token))
            _l_(419429)
    # If there are no (valid) credentials available, let the user log in.
    if not _n_(419432, "creds", lambda: creds) or not _a_(419434, _n_(419433, "creds", lambda: creds), "valid"):
        _l_(419465)

        if _n_(419435, "creds", lambda: creds) and _a_(419437, _n_(419436, "creds", lambda: creds), "expired") and _a_(419439, _n_(419438, "creds", lambda: creds), "refresh_token"):
            _l_(419455)

            _c_(419444, _a_(419441, _n_(419440, "creds", lambda: creds), "refresh"), _c_(419443, _n_(419442, "Request", lambda: Request)))
            _l_(419445)
        else:
            flow = _c_(419449, _a_(419447, _n_(419446, "InstalledAppFlow", lambda: InstalledAppFlow), "from_client_secrets_file"), 'credentials.json', _n_(419448, "SCOPES", lambda: SCOPES))
            _l_(419450)
            creds = _c_(419453, _a_(419452, _n_(419451, "flow", lambda: flow), "run_local_server"))
            _l_(419454)
        # Save the credentials for the next run
        with _c_(419457, _n_(419456, "open", lambda: open), 'token.pickle', 'wb') as token:
            _l_(419464)

            _c_(419462, _a_(419459, _n_(419458, "pickle", lambda: pickle), "dump"), _n_(419460, "creds", lambda: creds), _n_(419461, "token", lambda: token))
            _l_(419463)

    service = _c_(419468, _n_(419466, "build", lambda: build), 'drive', 'v3', credentials=_n_(419467, "creds", lambda: creds))
    _l_(419469)

    # Call the Drive v3 API
    results = _c_(419476, _a_(419475, _c_(419474, _a_(419473, _c_(419472, _a_(419471, _n_(419470, "service", lambda: service), "files")), "list"), q="mimeType != 'application/vnd.google-apps.folder'",
        pageSize=10,
        fields="nextPageToken, files(id, name)"
    ), "execute"))
    _l_(419477)
    items = _c_(419480, _a_(419479, _n_(419478, "results", lambda: results), "get"), 'files', [])
    _l_(419481)

    if not _n_(419482, "items", lambda: items):
        _l_(419503)

        _c_(419484, _n_(419483, "print", lambda: print), 'No files found.')
        _l_(419485)
    else:
        _c_(419487, _n_(419486, "print", lambda: print), 'Files:')
        _l_(419488)
        for item in _n_(419489, "items", lambda: items):
            _l_(419502)

            _c_(419495, _n_(419490, "print", lambda: print), _c_(419494, _a_(419491, u'{0} ({1})', "format"), _n_(419492, "item", lambda: item)['name'], _n_(419493, "item", lambda: item)['id']))
            _l_(419496)
            _c_(419500, _n_(419497, "downloadFile", lambda: downloadFile), _n_(419498, "service", lambda: service), _n_(419499, "item", lambda: item)['id'])
            _l_(419501)

if _n_(419505, "__name__", lambda: __name__) == '__main__':
    _l_(419509)

    _c_(419507, _n_(419506, "main", lambda: main))
    _l_(419508)