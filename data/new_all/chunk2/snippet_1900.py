# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41553652/type-error-when-using-sparkit-learns-sparkcountvectorizer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_rdd2 = _c_(466634, _a_(466633, _n_(466632, "sc", lambda: sc), "parallelize"), ['some perfectly reasonable string', 'another perfectly reasonable string'])
_l_(466635)
array_rdd_2 = _c_(466638, _n_(466636, "ArrayRDD", lambda: ArrayRDD), _n_(466637, "my_rdd2", lambda: my_rdd2))
_l_(466639)
tf = _c_(466643, _a_(466641, _n_(466640, "counter", lambda: counter), "fit_transform"), _n_(466642, "array_rdd2", lambda: array_rdd2))
_l_(466644)
_n_(466645, "tf", lambda: tf)
_l_(466646)
# <class 'splearn.rdd.SparseRDD'> from PythonRDD[20] at RDD at PythonRDD.scala:48