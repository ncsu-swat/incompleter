# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73733871/typeerror-document-must-be-an-instance-of-dict-bson-son-son-bson-raw-bson-raw
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy.polynomial import Polynomial as poly
    _l_(548868)

except ImportError:
    pass
try:
    import numpy as np
    _l_(548870)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(548872)

except ImportError:
    pass
try:
    import pymongo
    _l_(548874)

except ImportError:
    pass
try:
    import json
    _l_(548876)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(548878)

except ImportError:
    pass

 
df = _c_(548881, _a_(548880, _n_(548879, "pd", lambda: pd), "read_csv"), r'D:\polynomial\points.csv')
_l_(548882)
_c_(548885, _n_(548883, "print", lambda: print), _n_(548884, "df", lambda: df))
_l_(548886)

x= _c_(548892, _a_(548888, _n_(548887, "np", lambda: np), "array"), _c_(548891, _a_(548890, _n_(548889, "df", lambda: df)['Wavelength(A)'], "tolist")))
_l_(548893)
x= _c_(548897, _a_(548895, _n_(548894, "np", lambda: np), "divide"), [299792.458], _n_(548896, "x", lambda: x))
_l_(548898)
y= _c_(548904, _a_(548900, _n_(548899, "np", lambda: np), "array"), _c_(548903, _a_(548902, _n_(548901, "df", lambda: df)['Level(A)'], "tolist")))
_l_(548905)
x_trimmed = _c_(548913, _a_(548907, _n_(548906, "np", lambda: np), "delete"), _n_(548908, "x", lambda: x), _c_(548912, _a_(548910, _n_(548909, "np", lambda: np), "where"), _n_(548911, "y", lambda: y) < 1e-4))
_l_(548914)
y_trimmed = _c_(548922, _a_(548916, _n_(548915, "np", lambda: np), "delete"), _n_(548917, "y", lambda: y), _c_(548921, _a_(548919, _n_(548918, "np", lambda: np), "where"), _n_(548920, "y", lambda: y) < 1e-4))
_l_(548923)
test= _c_(548928, _a_(548925, _n_(548924, "poly", lambda: poly), "fit"), _n_(548926, "x_trimmed", lambda: x_trimmed), _n_(548927, "y_trimmed", lambda: y_trimmed), 10)
_l_(548929)
_c_(548932, _n_(548930, "print", lambda: print), _n_(548931, "test", lambda: test))
_l_(548933)

list1= _a_(548937, _c_(548936, _a_(548935, _n_(548934, "test", lambda: test), "convert")), "coef")
_l_(548938)
_c_(548941, _n_(548939, "print", lambda: print), _n_(548940, "list1", lambda: list1))
_l_(548942)
_c_(548947, _n_(548943, "print", lambda: print), _c_(548946, _n_(548944, "len", lambda: len), _n_(548945, "list1", lambda: list1)))
_l_(548948)
#print (type(list1))
to_list= _c_(548951, _a_(548950, _n_(548949, "list1", lambda: list1), "tolist"))
_l_(548952)
#print(to_list)
#data_format= json.dumps(to_list)
l = _c_(548955, _n_(548953, "len", lambda: len), _n_(548954, "to_list", lambda: to_list))
_l_(548956)
#print (l)
mydict1= []
_l_(548957)
for i in _c_(548960, _n_(548958, "range", lambda: range), _n_(548959, "l", lambda: l)):
    _l_(548972)

    mydict = { "a"+_c_(548963, _n_(548961, "str", lambda: str), _n_(548962, "i", lambda: i)) : _n_(548964, "to_list", lambda: to_list)[_n_(548965, "i", lambda: i)] }
    _l_(548966)
    _c_(548970, _a_(548968, _n_(548967, "mydict1", lambda: mydict1), "append"), _n_(548969, "mydict", lambda: mydict))
    _l_(548971)
_c_(548975, _n_(548973, "print", lambda: print), _n_(548974, "mydict1", lambda: mydict1))
_l_(548976)


myclient = _c_(548979, _a_(548978, _n_(548977, "pymongo", lambda: pymongo), "MongoClient"), "mongodb://localhost:27017/")
_l_(548980)
mydb = _n_(548981, "myclient", lambda: myclient)["mydatabase"]
_l_(548982)
mycol = _n_(548983, "mydb", lambda: mydb)["coefficients"]
_l_(548984)
x = _c_(548988, _a_(548986, _n_(548985, "mycol", lambda: mycol), "insert_one"), _n_(548987, "mydict1", lambda: mydict1))
_l_(548989)