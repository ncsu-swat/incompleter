# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74798015/typeerror-structtype-can-not-accept-object-1-1-2021-10000-am-in-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.sql.functions import to_timestamp
    _l_(566129)

except ImportError:
    pass
try:
    from pyspark.sql.types import StringType, StructType, StructField
    _l_(566131)

except ImportError:
    pass

schema = _c_(566137, _n_(566132, "StructType", lambda: StructType), [
    _c_(566136, _n_(566133, "StructField", lambda: StructField), "timestamp_str", _c_(566135, _n_(566134, "StringType", lambda: StringType)), True)
])
_l_(566138)

data = [("1/1/2021 1:00:00 AM")]
_l_(566139)
df = _c_(566144, _a_(566141, _n_(566140, "spark", lambda: spark), "createDataFrame"), _n_(566142, "data", lambda: data), schema=_n_(566143, "schema", lambda: schema))
_l_(566145)

df = _c_(566150, _a_(566147, _n_(566146, "df", lambda: df), "withColumn"), "timestamp", _c_(566149, _n_(566148, "to_timestamp", lambda: to_timestamp), "timestamp_str", "MM/dd/yyyy hh:mm:ss a"))
_l_(566151)