# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62989992/attribute-error-list-object-has-no-attribute-map
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.sql.types import *
    _l_(336730)

except ImportError:
    pass

schemaString="Address_Type,Address_ID,Address_Line_1,Address_Line_2,Address_Line_3,City,County,Zip,State,Country,Dflt_Address_Ind,Row_Insert_TS,Row_Update_TS,SYS_CHANGE_VERSION,SYS_CHANGE_OPERATION"
_l_(336731)

fields=_c_(336742, _a_(336735, _c_(336734, _a_(336733, _n_(336732, "schemaString", lambda: schemaString), "split"), ","), "map"), lambda fieldName: _c_(336741, _n_(336736, "StructField", lambda: StructField), _n_(336737, "fieldName", lambda: fieldName), _c_(336739, _n_(336738, "StringType", lambda: StringType)), nullable = _n_(336740, "true", lambda: true)))
_l_(336743)

schema = _c_(336746, _n_(336744, "StructType", lambda: StructType), _n_(336745, "fields", lambda: fields))
_l_(336747)