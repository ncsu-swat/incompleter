# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74135982/python-calling-mutiple-my-own-functions-nameerror-not-defined-on-passing-ou
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pymongo
    _l_(343550)

except ImportError:
    pass
try:
    import datetime
    _l_(343552)

except ImportError:
    pass
try:
    import json
    _l_(343554)

except ImportError:
    pass
def init_db(ip, db, coll):
    _l_(343569)

    myclient = _c_(343558, _a_(343556, _n_(343555, "pymongo", lambda: pymongo), "MongoClient"), 'mongodb://' + _n_(343557, "ip", lambda: ip) + '/')
    _l_(343559)
    mydb = _n_(343560, "myclient", lambda: myclient)[_n_(343561, "db", lambda: db)]
    _l_(343562)
    mycol = _n_(343563, "mydb", lambda: mydb)[_n_(343564, "coll", lambda: coll)]
    _l_(343565)
    aux = _n_(343566, "mydb", lambda: mydb), _n_(343567, "mycol", lambda: mycol)
    _l_(343568)

    return aux


def change_db_data(myquery_json, newvalues_json, one_or_many_bool):
    _l_(343586)

    
    if _n_(343570, "one_or_many_bool", lambda: one_or_many_bool) == True:
        _l_(343583)

        x = _c_(343575, _a_(343572, _n_(343571, "mycol", lambda: mycol), "update_many"), _n_(343573, "myquery_json", lambda: myquery_json), _n_(343574, "newvalues_json", lambda: newvalues_json))
        _l_(343576)
    else:
        x = _c_(343581, _a_(343578, _n_(343577, "mycol", lambda: mycol), "update_one"), _n_(343579, "myquery_json", lambda: myquery_json), _n_(343580, "newvalues_json", lambda: newvalues_json))
        _l_(343582)
    aux = _n_(343584, "x", lambda: x)
    _l_(343585)
    return aux