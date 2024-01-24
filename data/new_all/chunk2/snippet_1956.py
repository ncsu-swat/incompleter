# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75704771/google-drive-api-attributeerror-credentials-object-has-no-attribute-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os.path
    _l_(431465)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(431467)

except ImportError:
    pass
try:
    from google.auth.transport.requests import Request
    _l_(431469)

except ImportError:
    pass
try:
    from google.oauth2.credentials import Credentials
    _l_(431471)

except ImportError:
    pass
try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    _l_(431473)

except ImportError:
    pass
try:
    from googleapiclient.discovery import build
    _l_(431475)

except ImportError:
    pass
try:
    from googleapiclient.errors import HttpError
    _l_(431477)

except ImportError:
    pass
try:
    from googleapiclient.http import MediaFileUpload
    _l_(431479)

except ImportError:
    pass


SCOPES = ["https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive",
          "https://www.googleapis.com/auth/drive.metadata", "https://www.googleapis.com/auth/drive.readonly",
          "https://www.googleapis.com/auth/drive.metadata.readonly"]
_l_(431480)

drive_folder = "google_drive"
_l_(431481)

def get_token(cred_path):
    _l_(431549)

    cred_path = _c_(431484, _n_(431482, "Path", lambda: Path), _n_(431483, "cred_path", lambda: cred_path))
    _l_(431485)
    cred = None
    _l_(431486)
    token_file_path = _c_(431492, _n_(431487, "Path", lambda: Path), _c_(431490, _a_(431489, _n_(431488, "Path", lambda: Path), "cwd")), _n_(431491, "drive_folder", lambda: drive_folder), "token.json")
    _l_(431493)

    if _c_(431496, _a_(431495, _n_(431494, "token_file_path", lambda: token_file_path), "exists")):
        _l_(431505)

        cred = _c_(431503, _a_(431498, _n_(431497, "Credentials", lambda: Credentials), "from_authorized_user_file"), _c_(431501, _n_(431499, "str", lambda: str), _n_(431500, "token_file_path", lambda: token_file_path)), _n_(431502, "SCOPES", lambda: SCOPES))
        _l_(431504)

    if not _n_(431506, "cred", lambda: cred) or not _a_(431508, _n_(431507, "cred", lambda: cred), "valid"):
        _l_(431546)

        if _n_(431509, "cred", lambda: cred) and _a_(431511, _n_(431510, "cred", lambda: cred), "expired") and _a_(431513, _n_(431512, "cred", lambda: cred), "refresh_token"):
            _l_(431532)

            _c_(431518, _a_(431515, _n_(431514, "cred", lambda: cred), "refresh"), _c_(431517, _n_(431516, "Request", lambda: Request)))
            _l_(431519)
        else:
            flow = _c_(431526, _a_(431521, _n_(431520, "InstalledAppFlow", lambda: InstalledAppFlow), "from_client_secrets_file"), _c_(431524, _n_(431522, "str", lambda: str), _n_(431523, "cred_path", lambda: cred_path)), _n_(431525, "SCOPES", lambda: SCOPES)
            )
            _l_(431527)
            cred = _c_(431530, _a_(431529, _n_(431528, "flow", lambda: flow), "run_local_server"), port=0)
            _l_(431531)
        with _c_(431535, _n_(431533, "open", lambda: open), _n_(431534, "token_file_path", lambda: token_file_path), 'w') as file:
            _l_(431543)

            _c_(431541, _a_(431537, _n_(431536, "file", lambda: file), "write"), _c_(431540, _a_(431539, _n_(431538, "cred", lambda: cred), "to_json")))
            _l_(431542)
        aux = _n_(431544, "cred", lambda: cred)
        _l_(431545)
        return aux
    aux = _n_(431547, "cred", lambda: cred)
    _l_(431548)

    return aux

def upload_zip(zip_created_path, credential_path):
    _l_(431596)

    cred = _c_(431552, _n_(431550, "get_token", lambda: get_token), _n_(431551, "credential_path", lambda: credential_path))
    _l_(431553)
    zip_name = _c_(431557, _a_(431555, _a_(431554, os, "path"), "basename"), _n_(431556, "zip_created_path", lambda: zip_created_path))
    _l_(431558)
    try:
        _l_(431595)

        service = _c_(431561, _n_(431559, "build", lambda: build), "drive", 'v3', _n_(431560, "cred", lambda: cred))
        _l_(431562)

        file_metadata = {"name": _n_(431563, "zip_name", lambda: zip_name), "mimeType": "application/zip"}
        _l_(431564)
        media = _c_(431567, _n_(431565, "MediaFileUpload", lambda: MediaFileUpload), _n_(431566, "zip_created_path", lambda: zip_created_path), mimetype="application/zip", resumable=True)
        _l_(431568)

        file = _c_(431577, _a_(431576, _c_(431575, _a_(431572, _c_(431571, _a_(431570, _n_(431569, "service", lambda: service), "files")), "create"), body=_n_(431573, "file_metadata", lambda: file_metadata), media_body=_n_(431574, "media", lambda: media),
                                      fields='id'), "execute"))
        _l_(431578)
        _c_(431582, _a_(431580, _n_(431579, "os", lambda: os), "remove"), _n_(431581, "zip_created_path", lambda: zip_created_path))
        _l_(431583)
        aux = _c_(431586, _a_(431585, _n_(431584, "file", lambda: file), "get"), 'id')
        _l_(431587)
        return aux

    except _n_(431588, "HttpError", lambda: HttpError) as error:
        _l_(431594)

        _c_(431591, _n_(431589, "print", lambda: print), F'An error occurred: {_n_(431590, "error", lambda: error)}')
        _l_(431592)
        aux = ""
        _l_(431593)
        return aux