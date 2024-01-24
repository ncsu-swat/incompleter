# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73028953/reading-file-from-a-different-project-gcloud-file-not-found-error-even-though-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from google.cloud import bigquery
    _l_(611079)

except ImportError:
    pass
try:
    from analytics import Clients, ClientType
    _l_(611081)

except ImportError:
    pass
try:
    from datetime import datetime, date, timedelta
    _l_(611083)

except ImportError:
    pass
try:
    from pytz import timezone
    _l_(611085)

except ImportError:
    pass
try:
    from typing import List
    _l_(611087)

except ImportError:
    pass
try:
    from pyarrow import json as pyj
    _l_(611089)

except ImportError:
    pass
try:
    import pyarrow.parquet as pq
    _l_(611091)

except ImportError:
    pass
try:
    import newlinejson as nlj
    _l_(611093)

except ImportError:
    pass

bigquery_client = _c_(611098, _a_(611095, _n_(611094, "Clients", lambda: Clients), "get_client"), _a_(611097, _n_(611096, "ClientType", lambda: ClientType), "STORAGE"), name='w')
_l_(611099)
write_client = _c_(611104, _a_(611101, _n_(611100, "Clients", lambda: Clients), "get_client"), _a_(611103, _n_(611102, "ClientType", lambda: ClientType), "BIGQUERY"), name='w')
_l_(611105)
k_client = _c_(611110, _a_(611107, _n_(611106, "Clients", lambda: Clients), "get_client"), _a_(611109, _n_(611108, "ClientType", lambda: ClientType), "BIGQUERY"), name='w')
_l_(611111)

bucket ='update'
_l_(611112)


file_name_prefix = "al_"
_l_(611113)
target_table = _c_(611116, _a_(611115, _n_(611114, "k_client", lambda: k_client), "get_table"), "w.junk.json_table1")
_l_(611117)

def get_dates() -> _n_(611118, "List", lambda: List)[_n_(611119, "str", lambda: str)]:
    _l_(611143)

    """
    Return dates for which log files have to be checked
    """
    end = _c_(611132, _a_(611121, _n_(611120, "date", lambda: date), "fromisoformat"), _c_(611131, _n_(611122, "str", lambda: str), _c_(611130, _a_(611124, _n_(611123, "datetime", lambda: datetime), "date"), _c_(611129, _a_(611126, _n_(611125, "datetime", lambda: datetime), "now"), _c_(611128, _n_(611127, "timezone", lambda: timezone), "EST")))))
    _l_(611133)
    aux = [_c_(611138, _n_(611134, "str", lambda: str), _n_(611135, "end", lambda: end) - _c_(611137, _n_(611136, "timedelta", lambda: timedelta), days=1)), _c_(611141, _n_(611139, "str", lambda: str), _n_(611140, "end", lambda: end))]
    _l_(611142)
    return aux

def get_bucket_files(bucket, file_name_prefix):
    _l_(611157)

    # if full_path:
    path = "gs://{}/{}"
    _l_(611144)
    aux = [
        _c_(611150, _a_(611146, _n_(611145, "path", lambda: path), "format"), _n_(611147, "bucket", lambda: bucket), _a_(611149, _n_(611148, "b", lambda: b), "name"))
        for b in _c_(611155, _a_(611152, _n_(611151, "bigquery_client", lambda: bigquery_client), "list_blobs"), _n_(611153, "bucket", lambda: bucket), prefix=_n_(611154, "file_name_prefix", lambda: file_name_prefix))
    ]
    _l_(611156)
    #path = "https://storage.googleapis.com/{}/{}"
    return aux

def get_latest_file() -> _n_(611158, "str", lambda: str):
    _l_(611190)

    """
        Get all files for the current prefix between start and end date
        """
    files = []
    _l_(611159)
    files_json = []
    _l_(611160)

    for d in _c_(611162, _n_(611161, "get_dates", lambda: get_dates)):
        _l_(611189)

        prefix = _n_(611163, "file_name_prefix", lambda: file_name_prefix) + _n_(611164, "d", lambda: d)[4:] + "-" + _n_(611165, "d", lambda: d)[:4]
        _l_(611166)

        files += _c_(611170, _n_(611167, "get_bucket_files", lambda: get_bucket_files), _n_(611168, "bucket", lambda: bucket), _n_(611169, "file_name_prefix", lambda: file_name_prefix))
        _l_(611171)
        for k in _n_(611172, "files", lambda: files):
            _l_(611184)

            filename = _c_(611175, _a_(611174, _n_(611173, "k", lambda: k), "split"), '/')[-1]
            _l_(611176)
            if 'json' in _n_(611177, "filename", lambda: filename):
                _l_(611183)

                _c_(611181, _a_(611179, _n_(611178, "files_json", lambda: files_json), "append"), _n_(611180, "k", lambda: k))
                _l_(611182)
        aux = _c_(611187, _n_(611185, "max", lambda: max), _n_(611186, "files_json", lambda: files_json))
        _l_(611188)
        return aux

def pipeline():
    _l_(611210)

    job_config = _c_(611196, _a_(611192, _n_(611191, "bigquery", lambda: bigquery), "LoadJobConfig"), autodetect=True,
        source_format=_a_(611195, _a_(611194, _n_(611193, "bigquery", lambda: bigquery), "SourceFormat"), "NEWLINE_DELIMITED_JSON"),
    )
    _l_(611197)
    f = _c_(611199, _n_(611198, "get_latest_file", lambda: get_latest_file))
    _l_(611200)
    _c_(611203, _n_(611201, "print", lambda: print), _n_(611202, "f", lambda: f))
    _l_(611204)
    table = _c_(611208, _a_(611206, _n_(611205, "pyj", lambda: pyj), "read_json"), _n_(611207, "f", lambda: f))
    _l_(611209)
#     k_client.load_table_from_uri(
#         f, target_table, job_config=job_config
#     ).result()


_c_(611212, _n_(611211, "pipeline", lambda: pipeline))
_l_(611213)