# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69611598/attributeerror-logisticregressiontrainingsummary-object-has-no-attribute-are
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyspark.sql import SparkSession
    _l_(389874)

except ImportError:
    pass
try:
    import pyspark.sql.functions as F
    _l_(389876)

except ImportError:
    pass
try:
    import pyspark.sql.types as T
    _l_(389878)

except ImportError:
    pass

spark = _c_(389882, _a_(389881, _a_(389880, _n_(389879, "SparkSession", lambda: SparkSession), "builder"), "getOrCreate"))
_l_(389883)
    
df=_c_(389887, _a_(389886, _a_(389885, _n_(389884, "spark", lambda: spark), "read"), "csv"), "2018-2010_import.csv",inferSchema=True,header=True)
_l_(389888)
    
train, test = _c_(389891, _a_(389890, _n_(389889, "df", lambda: df), "randomSplit"), [0.7, 0.3], seed=7)
_l_(389892)
    
_c_(389897, _n_(389893, "print", lambda: print), f"Train set length: {_c_(389896, _a_(389895, _n_(389894, 'train', lambda: train), 'count'))} records")
_l_(389898)
_c_(389903, _n_(389899, "print", lambda: print), f"Test set length: {_c_(389902, _a_(389901, _n_(389900, 'test', lambda: test), 'count'))} records")
_l_(389904)

_a_(389906, _n_(389905, "train", lambda: train), "dtypes")
_l_(389907)

catCols = [_n_(389908, "x", lambda: x) for (x, dataType) in _a_(389910, _n_(389909, "train", lambda: train), "dtypes") if _n_(389911, "dataType", lambda: dataType) == "string"]
_l_(389912)
numCols = [
    _n_(389913, "x", lambda: x) for (x, dataType) in _a_(389915, _n_(389914, "train", lambda: train), "dtypes") if ((_n_(389916, "dataType", lambda: dataType) == "double") & (_n_(389917, "x", lambda: x) != "HSCode"))
]
_l_(389918)

_c_(389921, _n_(389919, "print", lambda: print), _n_(389920, "numCols", lambda: numCols))
_l_(389922)
_c_(389925, _n_(389923, "print", lambda: print), _n_(389924, "catCols", lambda: catCols))
_l_(389926)

_c_(389934, _a_(389933, _c_(389932, _a_(389928, _n_(389927, "train", lambda: train), "agg"), _c_(389931, _a_(389930, _n_(389929, "F", lambda: F), "countDistinct"), "Commodity","Country")), "show"))
_l_(389935)

_c_(389942, _a_(389941, _c_(389940, _a_(389939, _c_(389938, _a_(389937, _n_(389936, "train", lambda: train), "groupBy"), "Commodity","Country"), "count")), "show"))
_l_(389943)
try:
    from pyspark.ml.feature import (
        OneHotEncoder,
        StringIndexer,
    )
    _l_(389945)

except ImportError:
    pass

string_indexer = [
    _c_(389949, _n_(389946, "StringIndexer", lambda: StringIndexer), inputCol=_n_(389947, "x", lambda: x), outputCol=_n_(389948, "x", lambda: x) + "_StringIndexer", handleInvalid="skip")
    for x in _n_(389950, "catCols", lambda: catCols)
]
_l_(389951)

one_hot_encoder = [
    _c_(389957, _n_(389952, "OneHotEncoder", lambda: OneHotEncoder), inputCols=[f"{_n_(389953, 'x', lambda: x)}_StringIndexer" for x in _n_(389954, "catCols", lambda: catCols)],
        outputCols=[f"{_n_(389955, 'x', lambda: x)}_OneHotEncoder" for x in _n_(389956, "catCols", lambda: catCols)],
    )
]
_l_(389958)
try:
    from pyspark.ml.feature import VectorAssembler
    _l_(389960)

except ImportError:
    pass

assemblerInput = [_n_(389961, "x", lambda: x) for x in _n_(389962, "numCols", lambda: numCols)]
_l_(389963)
assemblerInput += [f"{_n_(389964, 'x', lambda: x)}_OneHotEncoder" for x in _n_(389965, "catCols", lambda: catCols)]
_l_(389966)

vector_assembler = _c_(389969, _n_(389967, "VectorAssembler", lambda: VectorAssembler), inputCols=_n_(389968, "assemblerInput", lambda: assemblerInput), outputCol="VectorAssembler_features", handleInvalid="skip"
)
_l_(389970)

stages = []
_l_(389971)
stages += _n_(389972, "string_indexer", lambda: string_indexer)
_l_(389973)
stages += _n_(389974, "one_hot_encoder", lambda: one_hot_encoder)
_l_(389975)
stages += [_n_(389976, "vector_assembler", lambda: vector_assembler)]
_l_(389977)
try:
    from pyspark.ml import Pipeline
    _l_(389979)

except ImportError:
    pass

pipeline = _c_(389984, _a_(389982, _c_(389981, _n_(389980, "Pipeline", lambda: Pipeline)), "setStages"), _n_(389983, "stages", lambda: stages))
_l_(389985)
model = _c_(389989, _a_(389987, _n_(389986, "pipeline", lambda: pipeline), "fit"), _n_(389988, "train", lambda: train))
_l_(389990)

pp_df = _c_(389994, _a_(389992, _n_(389991, "model", lambda: model), "transform"), _n_(389993, "test", lambda: test))
_l_(389995)

_c_(390000, _a_(389999, _c_(389998, _a_(389997, _n_(389996, "pp_df", lambda: pp_df), "select"), "HSCode", "Commodity", "value", "Country", "VectorAssembler_features",
), "show"), truncate=False)
_l_(390001)
try:
    from pyspark.ml.classification import LogisticRegression
    _l_(390003)

except ImportError:
    pass

data = _c_(390016, _a_(390005, _n_(390004, "pp_df", lambda: pp_df), "select"), _c_(390010, _a_(390009, _c_(390008, _a_(390007, _n_(390006, "F", lambda: F), "col"), "VectorAssembler_features"), "alias"), "features"),
    _c_(390015, _a_(390014, _c_(390013, _a_(390012, _n_(390011, "F", lambda: F), "col"), "HSCode"), "alias"), "label"),
)
_l_(390017)

model = _c_(390022, _a_(390020, _c_(390019, _n_(390018, "LogisticRegression", lambda: LogisticRegression)), "fit"), _n_(390021, "data", lambda: data))
_l_(390023)

_a_(390025, _n_(390024, "model_summary", lambda: model_summary), "areaUnderROC")
_l_(390026)