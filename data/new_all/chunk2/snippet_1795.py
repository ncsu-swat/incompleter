# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55427880/typeerror-unsupported-operand-types-for-map-and-list-with-pyspark
# Transform all features into a vector using VectorAssembler
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
numericCols = ["age", "fnlwgt", "education_num", "capital_gain", "capital_loss", "hours_per_week"]
_l_(468997)
assemblerInputs = _c_(469001, _n_(468998, "map", lambda: map), lambda c: _n_(468999, "c", lambda: c) + "TypeError: unsupported operand type(s) for +: 'map' and 'list'", _n_(469000, "categoricalColumns", lambda: categoricalColumns)) + _n_(469002, "numericCols", lambda: numericCols)
_l_(469003)
assembler = _c_(469006, _n_(469004, "VectorAssembler", lambda: VectorAssembler), inputCols=_n_(469005, "assemblerInputs", lambda: assemblerInputs), outputCol="features")
_l_(469007)
stages += [_n_(469008, "assembler", lambda: assembler)]
_l_(469009)