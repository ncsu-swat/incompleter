# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40513144/open-geotiff-with-gdal-produces-attributeerror-exit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from osgeo import gdal
    _l_(405451)

except ImportError:
    pass
gtiff = _c_(405455, _a_(405453, _n_(405452, "gdal", lambda: gdal), "Open"), _n_(405454, "filename", lambda: filename))
_l_(405456)
prj = _c_(405459, _a_(405458, _n_(405457, "gtiff", lambda: gtiff), "GetProjection"))
_l_(405460)
# do some work