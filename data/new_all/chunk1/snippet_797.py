# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40513144/open-geotiff-with-gdal-produces-attributeerror-exit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(401216, _a_(401214, _n_(401213, "gdal", lambda: gdal), "Open"), _n_(401215, "filename", lambda: filename)) as gtiff:
    _l_(401221)

    prj = _c_(401219, _a_(401218, _n_(401217, "gtiff", lambda: gtiff), "GetProjection"))
    _l_(401220)