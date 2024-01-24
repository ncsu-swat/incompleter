# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69669751/typeerror-bool-object-is-not-subscriptable-with-while-loop
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while _c_(588134, _n_(588132, "CheckBlockOrder", lambda: CheckBlockOrder), _n_(588133, "dictCon", lambda: dictCon))[1] is not True:
  _l_(588159)

  pair=_c_(588137, _n_(588135, "CheckBlockOrder", lambda: CheckBlockOrder), _n_(588136, "dictCon", lambda: dictCon))[0]
  _l_(588138)
  df_shuffle = _n_(588139, "dictCon", lambda: dictCon)[_n_(588140, "pair", lambda: pair)[0]]
  _l_(588141)
  df_shuffle = _c_(588151, _a_(588150, _a_(588143, _n_(588142, "df_shuffle", lambda: df_shuffle), "iloc")[_c_(588149, _a_(588146, _a_(588145, _n_(588144, "np", lambda: np), "random"), "permutation"), _a_(588148, _n_(588147, "df_shuffle", lambda: df_shuffle), "index"))], "reset_index"), drop=True)
  _l_(588152)
  _c_(588157, _a_(588154, _n_(588153, "dictCon", lambda: dictCon), "update"), {_n_(588155, "pair", lambda: pair)[0]:_n_(588156, "df_shuffle", lambda: df_shuffle)})
  _l_(588158)