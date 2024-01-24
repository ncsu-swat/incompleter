# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74735553/osmnx-attributeerror-dataframe-object-has-no-attribute-crs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
G = _c_(600561, _a_(600560, _n_(600559, "ox", lambda: ox), "graph_from_bbox"), 37.79, 37.78, -122.41, -122.43, network_type='drive')
_l_(600562)
G_projected = _c_(600566, _a_(600564, _n_(600563, "ox", lambda: ox), "project_graph"), _n_(600565, "G", lambda: G))
_l_(600567)
_c_(600571, _a_(600569, _n_(600568, "ox", lambda: ox), "plot_graph"), _n_(600570, "G_projected", lambda: G_projected))
_l_(600572)