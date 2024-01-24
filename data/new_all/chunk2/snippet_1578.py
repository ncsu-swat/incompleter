# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75359017/filenotfounderror-errno-2-no-such-file-or-directory-while-exporting-a-parque
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import mysql.connector
    _l_(446595)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(446597)

except ImportError:
    pass
try:
    from google.cloud import storage
    _l_(446599)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(446601)

except ImportError:
    pass
try:
    import os
    _l_(446603)

except ImportError:
    pass

def extract_data_to_gcs(request):
    _l_(446769)

    connection = _c_(446615, _a_(446605, _a_(446604, mysql, "connector"), "connect"), host=_c_(446608, _a_(446607, _n_(446606, "os", lambda: os), "getenv"), '..'),
        user=_c_(446611, _a_(446610, _n_(446609, "os", lambda: os), "getenv"), '...'),
        password=_c_(446614, _a_(446613, _n_(446612, "os", lambda: os), "getenv"), '...'),
        database='....'
    )
    _l_(446616)

    cursor = _c_(446619, _a_(446618, _n_(446617, "connection", lambda: connection), "cursor"), buffered=True)
    _l_(446620)

    tables = ["table1", "table2", "table3"]
    _l_(446621)
    client = _c_(446624, _a_(446623, _n_(446622, "storage", lambda: storage), "Client"))
    _l_(446625)
    bucket = _c_(446628, _a_(446627, _n_(446626, "client", lambda: client), "bucket"), 'data-lake-archive')
    _l_(446629)

    # Create a timestamp-based folder name
    now = _c_(446632, _a_(446631, _n_(446630, "datetime", lambda: datetime), "now"))
    _l_(446633)
    folder_name = _c_(446636, _a_(446635, _n_(446634, "now", lambda: now), "strftime"), "new_folder_%Y%m%d_%H%M%S")
    _l_(446637)
    folder_path = f"{_n_(446638, 'folder_name', lambda: folder_name)}/"
    _l_(446639)

    # Create the folder in the GCS bucket
    blob = _c_(446643, _a_(446641, _n_(446640, "bucket", lambda: bucket), "blob"), _n_(446642, "folder_path", lambda: folder_path))
    _l_(446644)
    _c_(446647, _a_(446646, _n_(446645, "blob", lambda: blob), "upload_from_string"), "", content_type="application/octet-stream")
    _l_(446648)

    for table in _n_(446649, "tables", lambda: tables):
        _l_(446767)

        _c_(446655, _a_(446651, _n_(446650, "cursor", lambda: cursor), "execute"), _c_(446654, _a_(446652, "SELECT * FROM {}", "format"), _n_(446653, "table", lambda: table)))
        _l_(446656)
        chunks = _c_(446663, _a_(446658, _n_(446657, "pd", lambda: pd), "read_sql_query"), _c_(446661, _a_(446659, "SELECT * FROM {}", "format"), _n_(446660, "table", lambda: table)), _n_(446662, "connection", lambda: connection), chunksize=5000000)
        _l_(446664)
        for i, chunk in _c_(446667, _n_(446665, "enumerate", lambda: enumerate), _n_(446666, "chunks", lambda: chunks)):
            _l_(446704)

            _n_(446668, "chunk", lambda: chunk).columns = [_c_(446671, _n_(446669, "str", lambda: str), _n_(446670, "col", lambda: col)) for col in _a_(446673, _n_(446672, "chunk", lambda: chunk), "columns")]
            _l_(446674)
            ingestion_timestamp = _c_(446679, _a_(446678, _c_(446677, _a_(446676, _n_(446675, "datetime", lambda: datetime), "now")), "strftime"), "%Y-%m-%d %H:%M:%S")
            _l_(446680)
            parquet_file_path = _n_(446681, "folder_path", lambda: folder_path) + f"{_n_(446682, 'table', lambda: table)}-{_n_(446683, 'i', lambda: i)}.parquet"
            _l_(446684)
            timestamp = _c_(446689, _a_(446688, _c_(446687, _a_(446686, _n_(446685, "datetime", lambda: datetime), "now")), "strftime"), "%Y%m%d_%H%M%S")
            _l_(446690)
            # parquet_file_path = folder_path + f'abc.parquet'
            _c_(446693, _n_(446691, "print", lambda: print), f'folder path is {_n_(446692, "folder_path", lambda: folder_path)}')
            _l_(446694)
            _c_(446697, _n_(446695, 'print', lambda: print), f'parquet file path is {_n_(446696, "parquet_file_path", lambda: parquet_file_path)}')
            _l_(446698)
            _c_(446702, _a_(446700, _n_(446699, 'chunk', lambda: chunk), 'to_parquet'), _n_(446701, 'parquet_file_path', lambda: parquet_file_path), engine='fastparquet', compression='snappy')
            _l_(446703)

        _c_(446710, _a_(446706, _n_(446705, 'cursor', lambda: cursor), 'execute'), _c_(446709, _a_(446707, "SELECT table_name, column_name FROM information_schema.key_column_usage WHERE referenced_table_name = '{}'", 'format'), _n_(446708, 'table', lambda: table)))
        _l_(446711)
        referenced_tables = _c_(446714, _a_(446713, _n_(446712, 'cursor', lambda: cursor), 'fetchall'))
        _l_(446715)
        for referenced_table in _n_(446716, 'referenced_tables', lambda: referenced_tables):
            _l_(446766)

            chunks = _c_(446723, _a_(446718, _n_(446717, 'pd', lambda: pd), 'read_sql_query'), _c_(446721, _a_(446719, "SELECT * FROM {}", 'format'), _n_(446720, 'referenced_table', lambda: referenced_table)[0]), _n_(446722, 'connection', lambda: connection), chunksize=5000000)
            _l_(446724)
            for i, chunk in _c_(446727, _n_(446725, 'enumerate', lambda: enumerate), _n_(446726, 'chunks', lambda: chunks)):
                _l_(446765)

                _n_(446728, 'chunk', lambda: chunk).columns = [_c_(446731, _n_(446729, 'str', lambda: str), _n_(446730, 'col', lambda: col)) for col in _a_(446733, _n_(446732, 'chunk', lambda: chunk), 'columns')]
                _l_(446734)
                ingestion_timestamp = _c_(446739, _a_(446738, _c_(446737, _a_(446736, _n_(446735, 'datetime', lambda: datetime), 'now')), 'strftime'), "%Y-%m-%d %H:%M:%S")
                _l_(446740)
                _c_(446747, _a_(446742, _n_(446741, 'chunk', lambda: chunk), 'to_parquet'), f"{_n_(446743, 'folder_path', lambda: folder_path)}{_n_(446744, 'referenced_table', lambda: referenced_table)[0]}-{_n_(446745, 'ingestion_timestamp', lambda: ingestion_timestamp)}-{_n_(446746, 'i', lambda: i)}.parquet", engine='fastparquet', compression='snappy')
                _l_(446748)
                blob = _c_(446755, _a_(446750, _n_(446749, "bucket", lambda: bucket), "blob"), _n_(446751, "folder_path", lambda: folder_path) + f'{_n_(446752, "referenced_table", lambda: referenced_table)[0]}-{_n_(446753, "ingestion_timestamp", lambda: ingestion_timestamp)}-{_n_(446754, "i", lambda: i)}.parquet')
                _l_(446756)
                _c_(446763, _a_(446758, _n_(446757, 'blob', lambda: blob), 'upload_from_filename'), _n_(446759, 'folder_path', lambda: folder_path) + f'{_n_(446760, "referenced_table", lambda: referenced_table)[0]}-{_n_(446761, "ingestion_timestamp", lambda: ingestion_timestamp)}-{_n_(446762, "i", lambda: i)}.parquet')
                _l_(446764)
    aux = 'Data extracted and uploaded to GCS'
    _l_(446768)

    return aux