# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61384965/attributeerror-str-object-has-no-attribute-name-pyspark
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.sql import SparkSession
    _l_(408210)

except ImportError:
    pass
try:
    import logging
    _l_(408212)

except ImportError:
    pass
try:
    from pyspark.sql.types import *
    _l_(408214)

except ImportError:
    pass
try:
    from pyspark.sql.functions import to_timestamp
    _l_(408216)

except ImportError:
    pass
try:
    from pyspark.sql.functions import udf
    _l_(408218)

except ImportError:
    pass
try:
    from pyspark.sql.functions import lit
    _l_(408220)

except ImportError:
    pass
try:
    from pyspark.sql.functions import year, month, dayofmonth
    _l_(408222)

except ImportError:
    pass
try:
    from pyspark.context import SparkContext
    _l_(408224)

except ImportError:
    pass
try:
    from pyspark.sql import SQLContext
    _l_(408226)

except ImportError:
    pass
try:
    import argparse
    _l_(408228)

except ImportError:
    pass

_c_(408233, _a_(408230, _n_(408229, "logging", lambda: logging), "basicConfig"), level=_a_(408232, _n_(408231, "logging", lambda: logging), "INFO"),filename = 'parquet.log')
_l_(408234)
logger = _c_(408238, _a_(408236, _n_(408235, "logging", lambda: logging), "getLogger"), _n_(408237, "__name__", lambda: __name__))
_l_(408239)

parser = _c_(408242, _a_(408241, _n_(408240, "argparse", lambda: argparse), "ArgumentParser"))
_l_(408243)
_c_(408246, _a_(408245, _n_(408244, "parser", lambda: parser), "add_argument"), '--schema_py', '--list', nargs='+', required=True, dest='schema_py', help='Scheam def')
_l_(408247)

args = _c_(408250, _a_(408249, _n_(408248, "parser", lambda: parser), "parse_args"))
_l_(408251)

schemaField = _a_(408253, _n_(408252, "args", lambda: args), "schema_py")
_l_(408254)
_c_(408259, _n_(408255, "print", lambda: print), _c_(408258, _n_(408256, "type", lambda: type), _n_(408257, "schemaField", lambda: schemaField)))   #It will print <class 'list'>
_l_(408260)   #It will print <class 'list'>

schema = _c_(408263, _n_(408261, "StructType", lambda: StructType), _n_(408262, "schemaField", lambda: schemaField)) # On this line facing issue
_l_(408264) # On this line facing issue
_c_(408269, _n_(408265, "print", lambda: print), _c_(408268, _n_(408266, "type", lambda: type), _n_(408267, "schema", lambda: schema)))
_l_(408270)