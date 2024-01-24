# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64775607/typo-in-pymongo-set-update-causes-typeerror-unhashable-type-dict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
find_query = {'_id': _n_(474396, "doc", lambda: doc)['_id']}
_l_(474397)
upd_statement = {'$set:',
                 {'subdivision_name': _n_(474398, "new_name", lambda: new_name)}
                 }
_l_(474399)
_c_(474404, _a_(474401, _n_(474400, "dbCollection", lambda: dbCollection), "update_one"), _n_(474402, "find_query", lambda: find_query), _n_(474403, "upd_statement", lambda: upd_statement), upsert=False)
_l_(474405)