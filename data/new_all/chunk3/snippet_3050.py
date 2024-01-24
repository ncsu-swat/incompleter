# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51610133/typeerror-a-float-is-required-pyspark
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_window = _c_(536616, _a_(536615, _c_(536614, _a_(536613, _n_(536612, "Window", lambda: Window), "partitionBy")), "orderBy"), "time")  
_l_(536617)  
gps_d=_c_(536634, _a_(536619, _n_(536618, "gps_data", lambda: gps_data), "withColumn"), "dist", _c_(536633, _a_(536632, _c_(536631, _n_(536620, "dist", lambda: dist), "longitude", "latitude",
        _c_(536625, _a_(536623, _c_(536622, _n_(536621, "lag", lambda: lag), "longitude", 1), "over"), _n_(536624, "my_window", lambda: my_window)), _c_(536630, _a_(536628, _c_(536627, _n_(536626, "lag", lambda: lag), "latitude", 1), "over"), _n_(536629, "my_window", lambda: my_window))
    ), "alias"), "dist"))
_l_(536635)