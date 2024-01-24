# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64265260/python-attributeerror-int-object-has-no-attribute-decode-when-trying-to-ca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(548279)

except ImportError:
    pass
try:
    import networkx as nx
    _l_(548281)

except ImportError:
    pass

gml_path = "XXXX.gml"
_l_(548282)
gml_path = _c_(548285, _a_(548284, _n_(548283, "gml_path", lambda: gml_path), "encode"), "utf-8")
_l_(548286)
G = _c_(548290, _a_(548288, _n_(548287, "nx", lambda: nx), "read_gml"), _n_(548289, "gml_path", lambda: gml_path))
_l_(548291)
X = _c_(548298, _a_(548293, _n_(548292, "np", lambda: np), "array"), _c_(548297, _a_(548295, _n_(548294, "nx", lambda: nx), "to_numpy_matrix"), _n_(548296, "G", lambda: G)))
_l_(548299)
_c_(548305, _n_(548300, "print", lambda: print), _c_(548304, _a_(548302, _n_(548301, "nx", lambda: nx), "is_directed"), _n_(548303, "G", lambda: G)))
_l_(548306)