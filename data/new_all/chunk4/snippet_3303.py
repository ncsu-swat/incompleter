# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75961048/attributeerror-request-object-has-no-attribute-from-client-config-error
# Import necessary libraries
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(606135)

except ImportError:
    pass
try:
    import google.auth
    _l_(606137)

except ImportError:
    pass
try:
    from google.auth.transport.requests import Request
    _l_(606139)

except ImportError:
    pass
try:
    from google.oauth2.credentials import Credentials
    _l_(606141)

except ImportError:
    pass
try:
    from googleapiclient.errors import HttpError
    _l_(606143)

except ImportError:
    pass
try:
    from googleapiclient.discovery import build
    _l_(606145)

except ImportError:
    pass
try:
    from googleapiclient.http import MediaFileUpload, MediaIoBaseUpload
    _l_(606147)

except ImportError:
    pass
try:
    import requests
    _l_(606149)

except ImportError:
    pass
try:
    import io
    _l_(606151)

except ImportError:
    pass

# Define the OAuth 2.0 credentials
client_id = 'PUT YOUR CLIENT ID HERE'
_l_(606152)
project_id = 'PUT YOUR PROJECT ID HERE'
_l_(606153)
auth_uri = 'PUT YOUR AUTH URI HERE'
_l_(606154)
token_uri = 'PUT YOUR TOKEN URI HERE'
_l_(606155)
auth_provider_x509_cert_url = 'PUT YOUR AUTH PROVIDER X509 CERT URL HERE'
_l_(606156)
client_secret = 'PUT YOUR CLIENT SECRET HERE'
_l_(606157)
redirect_uris = ['PUT YOUR REDIRECT URIS HERE']
_l_(606158)
refresh_token = 'PUT YOUR REFRESH TOKEN HERE'
_l_(606159)

# Authenticate the user
creds = None
_l_(606160)
if _c_(606164, _a_(606163, _a_(606162, _n_(606161, "os", lambda: os), "path"), "exists"), 'token.json'):
    _l_(606169)

    creds = _c_(606167, _a_(606166, _n_(606165, "Credentials", lambda: Credentials), "from_authorized_user_file"), 'token.json', ['https://www.googleapis.com/auth/drive'])
    _l_(606168)

if not _n_(606170, "creds", lambda: creds) or not _a_(606172, _n_(606171, "creds", lambda: creds), "valid"):
    _l_(606214)

    if _n_(606173, "creds", lambda: creds) and _a_(606175, _n_(606174, "creds", lambda: creds), "expired") and _a_(606177, _n_(606176, "creds", lambda: creds), "refresh_token"):
        _l_(606203)

        _c_(606182, _a_(606179, _n_(606178, "creds", lambda: creds), "refresh"), _c_(606181, _n_(606180, "Request", lambda: Request)))
        _l_(606183)
    else:
        flow = _c_(606197, _a_(606189, _c_(606188, _a_(606187, _a_(606186, _a_(606185, _a_(606184, google, "auth"), "transport"), "requests"), "Request")), "from_client_config"), {
            'client_id': _n_(606190, "client_id", lambda: client_id),
            'client_secret': _n_(606191, "client_secret", lambda: client_secret),
            'redirect_uris': _n_(606192, "redirect_uris", lambda: redirect_uris),
            'project_id': _n_(606193, "project_id", lambda: project_id),
            'auth_uri': _n_(606194, "auth_uri", lambda: auth_uri),
            'token_uri': _n_(606195, "token_uri", lambda: token_uri),
            'auth_provider_x509_cert_url': _n_(606196, "auth_provider_x509_cert_url", lambda: auth_provider_x509_cert_url)
        }, ['https://www.googleapis.com/auth/drive'])
        _l_(606198)
        creds = _c_(606201, _a_(606200, _n_(606199, "flow", lambda: flow), "run_local_server"), port=0)
        _l_(606202)
    with _c_(606205, _n_(606204, "open", lambda: open), 'token.json', 'w') as token:
        _l_(606213)

        _c_(606211, _a_(606207, _n_(606206, "token", lambda: token), "write"), _c_(606210, _a_(606209, _n_(606208, "creds", lambda: creds), "to_json")))
        _l_(606212)

# Build the YouTube API client
youtube = _c_(606217, _n_(606215, "build", lambda: build), 'youtube', 'v3', credentials=_n_(606216, "creds", lambda: creds))
_l_(606218)

# Define the file ID and the name of the video
file_id = 'PUT YOUR GOOGLE DRIVE FILE ID HERE'
_l_(606219)
video_title = 'PUT YOUR VIDEO TITLE HERE'
_l_(606220)

# Get the video file from Google Drive
link = 'https://drive.google.com/uc?id=' + _n_(606221, "file_id", lambda: file_id)
_l_(606222)
response = _c_(606226, _a_(606224, _n_(606223, "requests", lambda: requests), "get"), _n_(606225, "link", lambda: link))
_l_(606227)
bytes_io = _c_(606232, _a_(606229, _n_(606228, "io", lambda: io), "BytesIO"), _a_(606231, _n_(606230, "response", lambda: response), "content"))
_l_(606233)

# Create a media upload object for the video file
media = _c_(606236, _n_(606234, "MediaIoBaseUpload", lambda: MediaIoBaseUpload), _n_(606235, "bytes_io", lambda: bytes_io), chunksize=-1, resumable=True)
_l_(606237)

# Define the parameters for the video insert request
body = {
    'snippet': {
        'title': _n_(606238, "video_title", lambda: video_title),
        'description': 'PUT YOUR VIDEO DESCRIPTION HERE',
        'tags': ['PUT', 'YOUR', 'VIDEO', 'TAGS', 'HERE'],
        'categoryId': 'PUT YOUR CATEGORY ID HERE'
    },
    'status': {
        'privacyStatus': 'PUT YOUR VIDEO PRIVACY STATUS HERE'
    }
}
_l_(606239)

# Execute the video insert request and upload the video
try:
    _l_(606270)

    insert_request = _c_(606251, _a_(606243, _c_(606242, _a_(606241, _n_(606240, "youtube", lambda: youtube), "videos")), "insert"), part=_c_(606248, _a_(606244, ',', "join"), _c_(606247, _a_(606246, _n_(606245, "body", lambda: body), "keys"))), body=_n_(606249, "body", lambda: body), media_body=_n_(606250, "media", lambda: media))
    _l_(606252)
    resumable_upload = _c_(606255, _a_(606254, _n_(606253, "insert_request", lambda: insert_request), "execute"))
    _l_(606256)
    _c_(606259, _n_(606257, "print", lambda: print), f'Video uploaded successfully! Video ID: {_n_(606258, "resumable_upload", lambda: resumable_upload)["id"]}')
    _l_(606260)
except _n_(606261, 'HttpError', lambda: HttpError) as error:
    _l_(606269)

    _c_(606267, _n_(606262, 'print', lambda: print), f'An HTTP error {_a_(606265, _a_(606264, _n_(606263, "error", lambda: error), "resp"), "status")} occurred: {_n_(606266, "error", lambda: error)}')
    _l_(606268)