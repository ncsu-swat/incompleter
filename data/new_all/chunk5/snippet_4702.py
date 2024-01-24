# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51991264/typeerror-edges-takes-no-keyword-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(696671)

except ImportError:
    pass
try:
    from collections import defaultdict
    _l_(696673)

except ImportError:
    pass
try:
    from typing import Dict, Any
    _l_(696675)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(696677)

except ImportError:
    pass
try:
    from IPython.utils import data
    _l_(696679)

except ImportError:
    pass
try:
    from networkit import *
    _l_(696681)

except ImportError:
    pass
try:
    import numpy as np
    _l_(696683)

except ImportError:
    pass
try:
    import networkx as nx
    _l_(696685)

except ImportError:
    pass
try:
    from networkit.graphio import GraphConverter
    _l_(696687)

except ImportError:
    pass
try:
    from numpy import genfromtxt
    _l_(696689)

except ImportError:
    pass
try:
    import metis as mt
    _l_(696691)

except ImportError:
    pass
try:
    from networkx.utils import make_str
    _l_(696693)

except ImportError:
    pass
try:
    from _NetworKit import Graph
    _l_(696695)

except ImportError:
    pass

df1 = _c_(696698, _a_(696697, _n_(696696, "pd", lambda: pd), "read_csv"), 'person_knows_person_0_0.csv', sep='|', index_col=False )
_l_(696699)
df2 = _c_(696703, _a_(696701, _n_(696700, "pd", lambda: pd), "DataFrame"), _n_(696702, "df1", lambda: df1) )
_l_(696704)
src_list = _c_(696708, _a_(696707, _a_(696706, _n_(696705, "df2", lambda: df2)[':START_ID(Person)'], "values"), "tolist"))
_l_(696709)
tgt_list = _c_(696713, _a_(696712, _a_(696711, _n_(696710, "df2", lambda: df2)[':END_ID(Person)'], "values"), "tolist"))
_l_(696714)

_c_(696717, _n_(696715, "print", lambda: print), _n_(696716, "src_list", lambda: src_list)[1] )
_l_(696718)
_c_(696721, _n_(696719, "print", lambda: print), _n_(696720, "tgt_list", lambda: tgt_list)[1] )
_l_(696722)
f = _c_(696724, _n_(696723, "open", lambda: open), 'sample_ex.csv', 'w' )
_l_(696725)
for (src, tgt) in _c_(696729, _n_(696726, "zip", lambda: zip), _n_(696727, "src_list", lambda: src_list), _n_(696728, "tgt_list", lambda: tgt_list) ):
    _l_(696740)

    _c_(696738, _a_(696731, _n_(696730, "f", lambda: f), "write"), _c_(696734, _n_(696732, "str", lambda: str), _n_(696733, "src", lambda: src) ) + ',' + _c_(696737, _n_(696735, "str", lambda: str), _n_(696736, "tgt", lambda: tgt) ) + '\n' )
    _l_(696739)
_c_(696743, _a_(696742, _n_(696741, "f", lambda: f), "close"))
_l_(696744)
reader = _c_(696747, _a_(696746, _n_(696745, "graphio", lambda: graphio), "EdgeListReader"), ',', 1, continuous=False )
_l_(696748)
G = _c_(696751, _a_(696750, _n_(696749, "reader", lambda: reader), "read"), 'sample_ex.csv' )
_l_(696752)
_c_(696755, _n_(696753, "print", lambda: print), _n_(696754, "G", lambda: G) )
_l_(696756)
_c_(696762, _a_(696758, _n_(696757, "graphio", lambda: graphio), "writeGraph"), _n_(696759, "G", lambda: G), 'newgraph.graph', _a_(696761, _n_(696760, "Format", lambda: Format), "METIS") )
_l_(696763)
metisgraph = _c_(696768, _a_(696765, _n_(696764, "graphio", lambda: graphio), "readGraph"), "newgraph.graph", _a_(696767, _n_(696766, "Format", lambda: Format), "METIS") )
_l_(696769)
_c_(696772, _n_(696770, "print", lambda: print), _n_(696771, "metisgraph", lambda: metisgraph) )
_l_(696773)
_c_(696776, _a_(696775, _n_(696774, "G", lambda: G), "indexEdges"))
_l_(696777)
_c_(696782, _n_(696778, "print", lambda: print), "Original size: ", _c_(696781, _a_(696780, _n_(696779, "G", lambda: G), "size")) )
_l_(696783)

sparsificationAlgorithm = _c_(696786, _a_(696785, _n_(696784, "sparsification", lambda: sparsification), "LocalDegreeSparsifier"))
_l_(696787)
S = _c_(696791, _a_(696789, _n_(696788, "sparsificationAlgorithm", lambda: sparsificationAlgorithm), "getSparsifiedGraph"), _n_(696790, "G", lambda: G), 0.5 )
_l_(696792)
_c_(696797, _n_(696793, "print", lambda: print), "Sparsified size: ", _c_(696796, _a_(696795, _n_(696794, "S", lambda: S), "size")) )
_l_(696798)


_c_(696802, _a_(696800, _n_(696799, "nx", lambda: nx), "write_edgelist"), _n_(696801, "S", lambda: S), 'sparsified_graph.edgelist', ',')
_l_(696803)