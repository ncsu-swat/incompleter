# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60156335/cloud-function-attribute-error-bytes-object-has-no-attribute-get-when-readi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
storage_client = _c_(393323, _a_(393322, _n_(393321, "storage", lambda: storage), "Client"))
_l_(393324)
bucket_name = 'bucket_name'
_l_(393325)
bucket = _c_(393329, _a_(393327, _n_(393326, "storage_client", lambda: storage_client), "get_bucket"), _n_(393328, "bucket_name", lambda: bucket_name))
_l_(393330)
blob = _c_(393333, _a_(393332, _n_(393331, "bucket", lambda: bucket), "get_blob"), 'key.json')
_l_(393334)
json_data_string = _c_(393337, _a_(393336, _n_(393335, "blob", lambda: blob), "download_as_string"))
_l_(393338)

credentials = _c_(393342, _a_(393340, _n_(393339, "ServiceAccountCredentials", lambda: ServiceAccountCredentials), "from_json_keyfile_dict"), _n_(393341, "json_data_string", lambda: json_data_string),
    scopes=['https://www.googleapis.com/auth/analytics',
            'https://www.googleapis.com/auth/analytics.edit'])
_l_(393343)