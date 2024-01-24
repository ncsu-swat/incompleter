# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52954676/pandas-scatter-plot-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(464383)

except ImportError:
    pass
try:
    import geopandas
    _l_(464385)

except ImportError:
    pass

shapefile = _c_(464389, _a_(464388, _a_(464387, _n_(464386, "geopandas", lambda: geopandas), "GeoDataFrame"), "from_file"), 'file.shp')
_l_(464390)

fig, ax = _c_(464393, _a_(464392, _n_(464391, "plt", lambda: plt), "subplots"), 1)
_l_(464394)

base = _c_(464398, _a_(464396, _n_(464395, "shapefile", lambda: shapefile), "plot"), ax=_n_(464397, "ax", lambda: ax))
_l_(464399)

_c_(464406, _a_(464402, _a_(464401, _n_(464400, "df", lambda: df), "plot"), "scatter"), 'Long', 'Lat',  c=_n_(464403, "df", lambda: df)['colC'], s=_n_(464404, "df", lambda: df)['colD'], alpha=0.7, ax=_n_(464405, "base", lambda: base), colormap='viridis')
_l_(464407)