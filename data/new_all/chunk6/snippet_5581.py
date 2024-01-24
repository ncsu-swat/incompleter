# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74135982/python-calling-mutiple-my-own-functions-nameerror-not-defined-on-passing-ou
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pymongo
    _l_(337384)

except ImportError:
    pass
try:
    import datetime
    _l_(337386)

except ImportError:
    pass
try:
    import json
    _l_(337388)

except ImportError:
    pass
def init_db(ip, db, coll):
    _l_(337403)

    myclient = _c_(337392, _a_(337390, _n_(337389, "pymongo", lambda: pymongo), "MongoClient"), 'mongodb://' + _n_(337391, "ip", lambda: ip) + '/')
    _l_(337393)
    mydb = _n_(337394, "myclient", lambda: myclient)[_n_(337395, "db", lambda: db)]
    _l_(337396)
    mycol = _n_(337397, "mydb", lambda: mydb)[_n_(337398, "coll", lambda: coll)]
    _l_(337399)
    aux = _n_(337400, "mydb", lambda: mydb), _n_(337401, "mycol", lambda: mycol)
    _l_(337402)

    return aux


def change_db_data(myquery_json, newvalues_json, one_or_many_bool):
    _l_(337420)

    
    if _n_(337404, "one_or_many_bool", lambda: one_or_many_bool) == True:
        _l_(337417)

        x = _c_(337409, _a_(337406, _n_(337405, "mycol", lambda: mycol), "update_many"), _n_(337407, "myquery_json", lambda: myquery_json), _n_(337408, "newvalues_json", lambda: newvalues_json))
        _l_(337410)
    else:
        x = _c_(337415, _a_(337412, _n_(337411, "mycol", lambda: mycol), "update_one"), _n_(337413, "myquery_json", lambda: myquery_json), _n_(337414, "newvalues_json", lambda: newvalues_json))
        _l_(337416)
    aux = _n_(337418, "x", lambda: x)
    _l_(337419)
    return aux