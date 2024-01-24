# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45292395/error-typeerror-unorderable-types-int-str
    # I used alias to avoid confusion with the mllib library
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyparsing import col
    _l_(674726)

except ImportError:
    pass
try:
    from pyspark.ml.clustering import LDA
    _l_(674728)

except ImportError:
    pass
try:
    from pyspark.ml.feature import HashingTF as MLHashingTF, Tokenizer, HashingTF, IDF, StringIndexer
    _l_(674730)

except ImportError:
    pass
try:
    from pyspark.ml.feature import IDF as MLIDF
    _l_(674732)

except ImportError:
    pass
try:
    from pyspark.python.pyspark.shell import sqlContext, sc
    _l_(674734)

except ImportError:
    pass
try:
    from pyspark.sql.types import DoubleType, StructField, StringType, StructType
    _l_(674736)

except ImportError:
    pass
try:
    from pyspark import SparkContext
    _l_(674738)

except ImportError:
    pass
try:
    from pyspark.sql import SQLContext, Row
    _l_(674740)

except ImportError:
    pass

dbURL = "hdfs://en.wikipedia.org/wiki/Music"
_l_(674741)
file = _c_(674744, _a_(674743, _n_(674742, "sc", lambda: sc), "textFile"), "1.txt")
_l_(674745)
#Define data frame schema
fields = [_c_(674749, _n_(674746, "StructField", lambda: StructField), 'key',_c_(674748, _n_(674747, "StringType", lambda: StringType)),False),_c_(674753, _n_(674750, "StructField", lambda: StructField), 'content',_c_(674752, _n_(674751, "StringType", lambda: StringType)),False)]
_l_(674754)
schema = _c_(674757, _n_(674755, "StructType", lambda: StructType), _n_(674756, "fields", lambda: fields))
_l_(674758)
#Data in format <key>,<listofwords>
file_temp = _c_(674764, _a_(674760, _n_(674759, "file", lambda: file), "map"), lambda l : _c_(674763, _a_(674762, _n_(674761, "l", lambda: l), "split"), ","))
_l_(674765)
file_df = _c_(674770, _a_(674767, _n_(674766, "sqlContext", lambda: sqlContext), "createDataFrame"), _n_(674768, "file_temp", lambda: file_temp), _n_(674769, "schema", lambda: schema))
_l_(674771)
#Extract TF-IDF From https://spark.apache.org/docs/1.5.2/ml-features.html
tokenizer = _c_(674773, _n_(674772, "Tokenizer", lambda: Tokenizer), inputCol='content', outputCol='words')
_l_(674774)
wordsData = _c_(674778, _a_(674776, _n_(674775, "tokenizer", lambda: tokenizer), "transform"), _n_(674777, "file_df", lambda: file_df))
_l_(674779)
hashingTF = _c_(674781, _n_(674780, "HashingTF", lambda: HashingTF), inputCol='words',outputCol='rawFeatures',numFeatures=1000)
_l_(674782)
featurizedData = _c_(674786, _a_(674784, _n_(674783, "hashingTF", lambda: hashingTF), "transform"), _n_(674785, "wordsData", lambda: wordsData))
_l_(674787)
idf = _c_(674789, _n_(674788, "IDF", lambda: IDF), inputCol='rawFeatures',outputCol='features')
_l_(674790)
idfModel = _c_(674794, _a_(674792, _n_(674791, "idf", lambda: idf), "fit"), _n_(674793, "featurizedData", lambda: featurizedData))
_l_(674795)
rescaled_data = _c_(674799, _a_(674797, _n_(674796, "idfModel", lambda: idfModel), "transform"), _n_(674798, "featurizedData", lambda: featurizedData))
_l_(674800)
indexer = _c_(674802, _n_(674801, "StringIndexer", lambda: StringIndexer), inputCol='key',outputCol='KeyIndex')
_l_(674803)
indexed_data = _c_(674818, _a_(674817, _c_(674816, _a_(674815, _c_(674814, _a_(674813, _c_(674812, _a_(674811, _c_(674810, _a_(674808, _c_(674807, _a_(674805, _n_(674804, "indexer", lambda: indexer), "fit"), _n_(674806, "rescaled_data", lambda: rescaled_data)), "transform"), _n_(674809, "rescaled_data", lambda: rescaled_data)), "drop"), 'key'), "drop"), 'content'), "drop"), 'words'), "drop"), 'rawFeatures')
_l_(674819)
corpus = _c_(674830, _a_(674828, _c_(674827, _a_(674821, _n_(674820, "indexed_data", lambda: indexed_data), "select"), _c_(674826, _a_(674825, _c_(674824, _n_(674822, "col", lambda: col), "KeyIndex",_n_(674823, "str", lambda: str)), "cast"), "long"), "features"), "map"), _n_(674829, "list", lambda: list))
_l_(674831)
model = _c_(674835, _a_(674833, _n_(674832, "LDA", lambda: LDA), "train"), _n_(674834, "corpus", lambda: corpus), k=2)
_l_(674836)