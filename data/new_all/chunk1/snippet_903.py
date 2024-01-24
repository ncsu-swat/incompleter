# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46111203/flask-dynamo-connection-issueattributeerror-dynamo-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(399983, _a_(399982, _n_(399981, "app", lambda: app), "route"), '/', methods=['GET'])
def hello_world():
    _l_(399993)

    with _c_(399986, _a_(399985, _n_(399984, "app", lambda: app), "app_context")):
        _l_(399991)

        _c_(399989, _a_(399988, _n_(399987, "dynamo", lambda: dynamo), "create_all"))
        _l_(399990)
    aux = 'table created!'
    _l_(399992)
    return aux