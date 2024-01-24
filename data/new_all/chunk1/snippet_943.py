# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71682915/pyspark-typeerror-unionbyname-got-an-unexpected-keyword-argument-allowmissi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df =_c_(404204, _a_(404201, _n_(404200, "spark", lambda: spark), "createDataFrame"), _n_(404202, "data", lambda: data),_n_(404203, "columns", lambda: columns))
_l_(404205)

df1 = _c_(404208, _a_(404207, _n_(404206, "spark", lambda: spark), "createDataFrame"), [[1, 2, 3]], ["col0", "col1", "col2"])
_l_(404209)
df2 = _c_(404212, _a_(404211, _n_(404210, "spark", lambda: spark), "createDataFrame"), [[4, 5, 6]], ["col1", "col2", "col3"])
_l_(404213)
_c_(404219, _a_(404218, _c_(404217, _a_(404215, _n_(404214, "df1", lambda: df1), "unionByName"), _n_(404216, "df2", lambda: df2), allowMissingColumns=True), "show"))
_l_(404220)