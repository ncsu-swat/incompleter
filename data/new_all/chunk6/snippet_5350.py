# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62989992/attribute-error-list-object-has-no-attribute-map
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.sql.types import *
    _l_(359913)

except ImportError:
    pass

schemaString="Address_Type,Address_ID,Address_Line_1,Address_Line_2,Address_Line_3,City,County,Zip,State,Country,Dflt_Address_Ind,Row_Insert_TS,Row_Update_TS,SYS_CHANGE_VERSION,SYS_CHANGE_OPERATION"
_l_(359914)

fields=_c_(359925, _a_(359918, _c_(359917, _a_(359916, _n_(359915, "schemaString", lambda: schemaString), "split"), ","), "map"), lambda fieldName: _c_(359924, _n_(359919, "StructField", lambda: StructField), _n_(359920, "fieldName", lambda: fieldName), _c_(359922, _n_(359921, "StringType", lambda: StringType)), nullable = _n_(359923, "true", lambda: true)))
_l_(359926)

schema = _c_(359929, _n_(359927, "StructType", lambda: StructType), _n_(359928, "fields", lambda: fields))
_l_(359930)