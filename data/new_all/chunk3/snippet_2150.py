# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60983924/attributeerror-mongoalchemy-object-has-no-attribute-insert-mongodb-flask-mo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask.ext.mongoalchemy import MongoAlchemy
    _l_(531888)

except ImportError:
    pass
try:
    from flask import Flask
    _l_(531890)

except ImportError:
    pass

mongododb = _c_(531892, _n_(531891, "MongoAlchemy", lambda: MongoAlchemy))
_l_(531893)

def init_app():
    _l_(531917)

    app = _c_(531896, _n_(531894, "Flask", lambda: Flask), _n_(531895, "__name__", lambda: __name__))
    _l_(531897)
    _a_(531899, _n_(531898, "app", lambda: app), "config")['DEBUG'] = True
    _l_(531900)
    _a_(531902, _n_(531901, "app", lambda: app), "config")['MONGOALCHEMY_SERVER'] = 'localhost'
    _l_(531903)
    _a_(531905, _n_(531904, "app", lambda: app), "config")['MONGOALCHEMY_PORT'] = '27017'
    _l_(531906)
    _a_(531908, _n_(531907, "app", lambda: app), "config")['MONGOALCHEMY_DATABASE'] = 'publicvoicedb'
    _l_(531909)
    _c_(531913, _a_(531911, _n_(531910, "mongododb", lambda: mongododb), "init_app"), _n_(531912, "app", lambda: app))
    _l_(531914)
    aux = _n_(531915, "app", lambda: app)
    _l_(531916)
    return aux

class Location(_a_(531919, _n_(531918, "mongododb", lambda: mongododb), "Document")):
    _l_(531928)

    type= _c_(531922, _a_(531921, _n_(531920, "mongododb", lambda: mongododb), "StringField"))
    _l_(531923)
    cooridantes =_c_(531926, _a_(531925, _n_(531924, "mongododb", lambda: mongododb), "StringField"))
    _l_(531927)


class Essential(_a_(531930, _n_(531929, "mongododb", lambda: mongododb), "Document")):
    _l_(531968)

    subscriberName = _c_(531933, _a_(531932, _n_(531931, "mongododb", lambda: mongododb), "StringField"))
    _l_(531934)
    mobileNumber = _c_(531937, _a_(531936, _n_(531935, "mongododb", lambda: mongododb), "IntField"))
    _l_(531938)
    address = _c_(531941, _a_(531940, _n_(531939, "mongododb", lambda: mongododb), "StringField"))
    _l_(531942)
    pincode = _c_(531945, _a_(531944, _n_(531943, "mongododb", lambda: mongododb), "IntField"))
    _l_(531946)
    location = _c_(531950, _a_(531948, _n_(531947, "mongododb", lambda: mongododb), "DocumentField"), _n_(531949, "Location", lambda: Location))
    _l_(531951)
    category = _c_(531954, _a_(531953, _n_(531952, "mongododb", lambda: mongododb), "StringField"))
    _l_(531955)
    request_date =_c_(531958, _a_(531957, _n_(531956, "mongododb", lambda: mongododb), "StringField"))
    _l_(531959)
    serviceType = _c_(531962, _a_(531961, _n_(531960, "mongododb", lambda: mongododb), "StringField")) 
    _l_(531963) 
    issueDescription = _c_(531966, _a_(531965, _n_(531964, "mongododb", lambda: mongododb), "StringField"))
    _l_(531967)