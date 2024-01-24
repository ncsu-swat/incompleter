# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55427880/typeerror-unsupported-operand-types-for-map-and-list-with-pyspark
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.ml import Pipeline
    _l_(464935)

except ImportError:
    pass
try:
    from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler
    _l_(464937)

except ImportError:
    pass

categoricalColumns = ["workclass", "education", "marital_status", "occupation", "relationship", "race", "sex", "native_country"]
_l_(464938)
stages = []
_l_(464939)
for categoricalCol in _n_(464940, "categoricalColumns", lambda: categoricalColumns):
    _l_(464954)

    #indexing with StringIndexer
    stringIndexer = _c_(464944, _n_(464941, "StringIndexer", lambda: StringIndexer), inputCol=_n_(464942, "categoricalCol", lambda: categoricalCol),
                                 outputCol=_n_(464943, "categoricalCol", lambda: categoricalCol)+'Index')
    _l_(464945)
    encoder = _c_(464949, _n_(464946, "OneHotEncoder", lambda: OneHotEncoder), inputCol=_n_(464947, "categoricalCol", lambda: categoricalCol)+'Index',
                           outputCol=_n_(464948, "categoricalCol", lambda: categoricalCol)+'classVec')
    _l_(464950)
    #Add stages
    stages += [_n_(464951, "stringIndexer", lambda: stringIndexer), _n_(464952, "encoder", lambda: encoder)]
    _l_(464953)

# Convert label into label indices using the StringIndexer
label_stringIdx = _c_(464956, _n_(464955, "StringIndexer", lambda: StringIndexer), inputCol = "income", outputCol = "label")
_l_(464957)
stages += [_n_(464958, "label_stringIdx", lambda: label_stringIdx)]
_l_(464959)