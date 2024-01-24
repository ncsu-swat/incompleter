# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61665661/how-to-solve-attribute-error-cursor-object-has-no-attribute-nocursortimeout
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from pymongo import MongoClient as Connection
  _l_(419077)

except ImportError:
  pass
try:
  from datetime import datetime
  _l_(419079)

except ImportError:
  pass

conn = _c_(419083, _n_(419080, "Connection", lambda: Connection), _c_(419082, _n_(419081, "get_uri", lambda: get_uri)))
_l_(419084)
with _n_(419085, "conn", lambda: conn) as conn:
  _l_(419095)

  collection = _n_(419086, "conn", lambda: conn)['db_name']['my_collection']
  _l_(419087)
  documents_cursor = _c_(419093, _a_(419092, _c_(419091, _a_(419089, _n_(419088, "collection", lambda: collection), "find"), _n_(419090, "query", lambda: query)), "noCursorTimeout")) # same with .maxTimeMS()
  _l_(419094) # same with .maxTimeMS()