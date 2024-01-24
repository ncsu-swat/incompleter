# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69994834/attributeerror-aioclientcreator-object-has-no-attribute-register-lazy-block
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
session = _c_(382603, _a_(382602, _n_(382601, "sagemaker", lambda: sagemaker), "Session"))
_l_(382604)
region = _a_(382608, _c_(382607, _a_(382606, _n_(382605, "boto3", lambda: boto3), "Session")), "region_name")
_l_(382609)
role = _c_(382611, _n_(382610, "get_execution_role", lambda: get_execution_role))
_l_(382612)
try:
    import pyarrow.parquet as pq
    _l_(382614)

except ImportError:
    pass
try:
    import s3fs
    _l_(382616)

except ImportError:
    pass
s3 = _c_(382619, _a_(382618, _n_(382617, "s3fs", lambda: s3fs), "S3FileSystem"))
_l_(382620)

bucket = 's3://xx'
_l_(382621)

df = _c_(382630, _a_(382629, _c_(382628, _a_(382627, _c_(382626, _a_(382623, _n_(382622, "pq", lambda: pq), "ParquetDataset"), _n_(382624, "bucket", lambda: bucket), filesystem=_n_(382625, "s3", lambda: s3)), "read_pandas")), "to_pandas"))
_l_(382631)