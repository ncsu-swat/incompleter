# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45113377/typeerror-when-calling-spark-mllib-logisticregressionwithlbfgs-train
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
trainingData = _c_(608968, _a_(608962, _a_(608961, _n_(608960, "sXYdf", lambda: sXYdf), "rdd"), "map"), lambda x: _c_(608967, _a_(608964, _n_(608963, "reg", lambda: reg), "LabeledPoint"), _n_(608965, "x", lambda: x)[0]-1,_n_(608966, "x", lambda: x)[1:]))
_l_(608969)
_c_(608972, _a_(608971, _n_(608970, "trainingData", lambda: trainingData), "take"), 2)
_l_(608973)