# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62989992/attribute-error-list-object-has-no-attribute-map
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.sql.types import *
    _l_(359058)

except ImportError:
    pass

schemaString="Address_Type,Address_ID,Address_Line_1,Address_Line_2,Address_Line_3,City,County,Zip,State,Country,Dflt_Address_Ind,Row_Insert_TS,Row_Update_TS,SYS_CHANGE_VERSION,SYS_CHANGE_OPERATION"
_l_(359059)

fields=_c_(359070, _a_(359063, _c_(359062, _a_(359061, _n_(359060, "schemaString", lambda: schemaString), "split"), ","), "map"), lambda fieldName: _c_(359069, _n_(359064, "StructField", lambda: StructField), _n_(359065, "fieldName", lambda: fieldName), _c_(359067, _n_(359066, "StringType", lambda: StringType)), nullable = _n_(359068, "true", lambda: true)))
_l_(359071)

schema = _c_(359074, _n_(359072, "StructType", lambda: StructType), _n_(359073, "fields", lambda: fields))
_l_(359075)