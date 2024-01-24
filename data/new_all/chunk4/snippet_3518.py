# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73028953/reading-file-from-a-different-project-gcloud-file-not-found-error-even-though-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from google.cloud import bigquery
    _l_(600309)

except ImportError:
    pass
try:
    from analytics import Clients, ClientType
    _l_(600311)

except ImportError:
    pass
try:
    from datetime import datetime, date, timedelta
    _l_(600313)

except ImportError:
    pass
try:
    from pytz import timezone
    _l_(600315)

except ImportError:
    pass
try:
    from typing import List
    _l_(600317)

except ImportError:
    pass
try:
    from pyarrow import json as pyj
    _l_(600319)

except ImportError:
    pass
try:
    import pyarrow.parquet as pq
    _l_(600321)

except ImportError:
    pass
try:
    import newlinejson as nlj
    _l_(600323)

except ImportError:
    pass

bigquery_client = _c_(600328, _a_(600325, _n_(600324, "Clients", lambda: Clients), "get_client"), _a_(600327, _n_(600326, "ClientType", lambda: ClientType), "STORAGE"), name='w')
_l_(600329)
write_client = _c_(600334, _a_(600331, _n_(600330, "Clients", lambda: Clients), "get_client"), _a_(600333, _n_(600332, "ClientType", lambda: ClientType), "BIGQUERY"), name='w')
_l_(600335)
k_client = _c_(600340, _a_(600337, _n_(600336, "Clients", lambda: Clients), "get_client"), _a_(600339, _n_(600338, "ClientType", lambda: ClientType), "BIGQUERY"), name='w')
_l_(600341)

bucket ='update'
_l_(600342)


file_name_prefix = "al_"
_l_(600343)
target_table = _c_(600346, _a_(600345, _n_(600344, "k_client", lambda: k_client), "get_table"), "w.junk.json_table1")
_l_(600347)

def get_dates() -> _n_(600348, "List", lambda: List)[_n_(600349, "str", lambda: str)]:
    _l_(600373)

    """
    Return dates for which log files have to be checked
    """
    end = _c_(600362, _a_(600351, _n_(600350, "date", lambda: date), "fromisoformat"), _c_(600361, _n_(600352, "str", lambda: str), _c_(600360, _a_(600354, _n_(600353, "datetime", lambda: datetime), "date"), _c_(600359, _a_(600356, _n_(600355, "datetime", lambda: datetime), "now"), _c_(600358, _n_(600357, "timezone", lambda: timezone), "EST")))))
    _l_(600363)
    aux = [_c_(600368, _n_(600364, "str", lambda: str), _n_(600365, "end", lambda: end) - _c_(600367, _n_(600366, "timedelta", lambda: timedelta), days=1)), _c_(600371, _n_(600369, "str", lambda: str), _n_(600370, "end", lambda: end))]
    _l_(600372)
    return aux

def get_bucket_files(bucket, file_name_prefix):
    _l_(600387)

    # if full_path:
    path = "gs://{}/{}"
    _l_(600374)
    aux = [
        _c_(600380, _a_(600376, _n_(600375, "path", lambda: path), "format"), _n_(600377, "bucket", lambda: bucket), _a_(600379, _n_(600378, "b", lambda: b), "name"))
        for b in _c_(600385, _a_(600382, _n_(600381, "bigquery_client", lambda: bigquery_client), "list_blobs"), _n_(600383, "bucket", lambda: bucket), prefix=_n_(600384, "file_name_prefix", lambda: file_name_prefix))
    ]
    _l_(600386)
    #path = "https://storage.googleapis.com/{}/{}"
    return aux

def get_latest_file() -> _n_(600388, "str", lambda: str):
    _l_(600420)

    """
        Get all files for the current prefix between start and end date
        """
    files = []
    _l_(600389)
    files_json = []
    _l_(600390)

    for d in _c_(600392, _n_(600391, "get_dates", lambda: get_dates)):
        _l_(600419)

        prefix = _n_(600393, "file_name_prefix", lambda: file_name_prefix) + _n_(600394, "d", lambda: d)[4:] + "-" + _n_(600395, "d", lambda: d)[:4]
        _l_(600396)

        files += _c_(600400, _n_(600397, "get_bucket_files", lambda: get_bucket_files), _n_(600398, "bucket", lambda: bucket), _n_(600399, "file_name_prefix", lambda: file_name_prefix))
        _l_(600401)
        for k in _n_(600402, "files", lambda: files):
            _l_(600414)

            filename = _c_(600405, _a_(600404, _n_(600403, "k", lambda: k), "split"), '/')[-1]
            _l_(600406)
            if 'json' in _n_(600407, "filename", lambda: filename):
                _l_(600413)

                _c_(600411, _a_(600409, _n_(600408, "files_json", lambda: files_json), "append"), _n_(600410, "k", lambda: k))
                _l_(600412)
        aux = _c_(600417, _n_(600415, "max", lambda: max), _n_(600416, "files_json", lambda: files_json))
        _l_(600418)
        return aux

def pipeline():
    _l_(600440)

    job_config = _c_(600426, _a_(600422, _n_(600421, "bigquery", lambda: bigquery), "LoadJobConfig"), autodetect=True,
        source_format=_a_(600425, _a_(600424, _n_(600423, "bigquery", lambda: bigquery), "SourceFormat"), "NEWLINE_DELIMITED_JSON"),
    )
    _l_(600427)
    f = _c_(600429, _n_(600428, "get_latest_file", lambda: get_latest_file))
    _l_(600430)
    _c_(600433, _n_(600431, "print", lambda: print), _n_(600432, "f", lambda: f))
    _l_(600434)
    table = _c_(600438, _a_(600436, _n_(600435, "pyj", lambda: pyj), "read_json"), _n_(600437, "f", lambda: f))
    _l_(600439)
#     k_client.load_table_from_uri(
#         f, target_table, job_config=job_config
#     ).result()


_c_(600442, _n_(600441, "pipeline", lambda: pipeline))
_l_(600443)