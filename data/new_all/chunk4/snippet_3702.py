# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69669751/typeerror-bool-object-is-not-subscriptable-with-while-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while _c_(631325, _n_(631323, "CheckBlockOrder", lambda: CheckBlockOrder), _n_(631324, "dictCon", lambda: dictCon))[1] is not True:
  _l_(631350)

  pair=_c_(631328, _n_(631326, "CheckBlockOrder", lambda: CheckBlockOrder), _n_(631327, "dictCon", lambda: dictCon))[0]
  _l_(631329)
  df_shuffle = _n_(631330, "dictCon", lambda: dictCon)[_n_(631331, "pair", lambda: pair)[0]]
  _l_(631332)
  df_shuffle = _c_(631342, _a_(631341, _a_(631334, _n_(631333, "df_shuffle", lambda: df_shuffle), "iloc")[_c_(631340, _a_(631337, _a_(631336, _n_(631335, "np", lambda: np), "random"), "permutation"), _a_(631339, _n_(631338, "df_shuffle", lambda: df_shuffle), "index"))], "reset_index"), drop=True)
  _l_(631343)
  _c_(631348, _a_(631345, _n_(631344, "dictCon", lambda: dictCon), "update"), {_n_(631346, "pair", lambda: pair)[0]:_n_(631347, "df_shuffle", lambda: df_shuffle)})
  _l_(631349)