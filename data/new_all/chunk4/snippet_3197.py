# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77436795/azure-blob-storage-attributeerror-nonetype-object-has-no-attribute-rstrip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from os import getenv
    _l_(609765)

except ImportError:
    pass
try:
    from azure.storage.blob import BlobServiceClient
    _l_(609767)

except ImportError:
    pass

blob_service_client = _c_(609772, _a_(609769, _n_(609768, "BlobServiceClient", lambda: BlobServiceClient), "from_connection_string"), _c_(609771, _n_(609770, "getenv", lambda: getenv), "AZURE_STORAGE_CONNECTION_STRING"))
_l_(609773)