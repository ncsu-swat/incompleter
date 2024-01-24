# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76399931/attributeerror-cant-pickle-local-object-flask-init-locals-lambda
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(597105)

except ImportError:
    pass
try:
    import ProcessBuilder as pb
    _l_(597107)

except ImportError:
    pass
try:
    import ServiceLogger as sl
    _l_(597109)

except ImportError:
    pass
try:
    import SystemRecovery as sr
    _l_(597111)

except ImportError:
    pass
try:
    from flask import Flask, Response
    _l_(597113)

except ImportError:
    pass
try:
    from waitress import serve
    _l_(597115)

except ImportError:
    pass
try:
    from flask_cors import CORS
    _l_(597117)

except ImportError:
    pass


class EndpointAction(_n_(597118, "object", lambda: object)):
    _l_(597140)


    def __init__(self, action):
        _l_(597131)

        _n_(597119, "self", lambda: self).action = _n_(597120, "action", lambda: action)
        _l_(597121)
        _n_(597122, "self", lambda: self).logger = _c_(597125, _a_(597124, _n_(597123, "sl", lambda: sl), "ServiceLogger"))
        _l_(597126)
        _n_(597127, "self", lambda: self).response = _c_(597129, _n_(597128, "Response", lambda: Response), status=200, headers={})
        _l_(597130)

    def __call__(self, *args):
        _l_(597139)

        _c_(597134, _a_(597133, _n_(597132, "self", lambda: self), "action"))
        _l_(597135)
        aux = _a_(597137, _n_(597136, "self", lambda: self), "response")
        _l_(597138)
        return aux


class ApiServer:
    _l_(597217)


    def __init__(self):
        _l_(597186)

        _n_(597141, "self", lambda: self).server = None
        _l_(597142)
        _n_(597143, "self", lambda: self).debug = _a_(597147, _c_(597146, _a_(597145, _n_(597144, "sr", lambda: sr), "Recovery")), "debug")
        _l_(597148)
        _n_(597149, "self", lambda: self).port = _a_(597153, _c_(597152, _a_(597151, _n_(597150, "sr", lambda: sr), "Recovery")), "api_port")
        _l_(597154)
        _n_(597155, "self", lambda: self).host = '127.0.0.1'
        _l_(597156)
        _n_(597157, "self", lambda: self).logger = _c_(597160, _a_(597159, _n_(597158, "sl", lambda: sl), "ServiceLogger"))
        _l_(597161)
        _n_(597162, "self", lambda: self).app = _c_(597165, _n_(597163, "Flask", lambda: Flask), _n_(597164, "__name__", lambda: __name__))
        _l_(597166)
        _c_(597170, _n_(597167, "CORS", lambda: CORS), _a_(597169, _n_(597168, "self", lambda: self), "app"), resources={r"/api/*": {"origins": "*"}})
        _l_(597171)
        _c_(597174, _a_(597173, _n_(597172, "self", lambda: self), "register_endpoints"))
        _l_(597175)
        _n_(597176, "self", lambda: self).server = _c_(597184, _a_(597180, _c_(597179, _a_(597178, _n_(597177, "pb", lambda: pb), "ProcessBuilder")), "create_process"), _a_(597182, _n_(597181, "self", lambda: self), "run"), [_n_(597183, "self", lambda: self)])
        _l_(597185)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        _l_(597197)

        _c_(597195, _a_(597189, _a_(597188, _n_(597187, "self", lambda: self), "app"), "add_url_rule"), _n_(597190, "endpoint", lambda: endpoint), _n_(597191, "endpoint_name", lambda: endpoint_name), _c_(597194, _n_(597192, "EndpointAction", lambda: EndpointAction), _n_(597193, "handler", lambda: handler)))
        _l_(597196)

    def register_endpoints(self):
        _l_(597199)

        aux = None
        _l_(597198)
        return aux

    def start(self):
        _l_(597205)

        _c_(597203, _a_(597202, _a_(597201, _n_(597200, "self", lambda: self), "server"), "start"))
        _l_(597204)

    def run(self):
        _l_(597209)

        _c_(597207, _n_(597206, "print", lambda: print), "heyy")
        _l_(597208)

    def terminate(self):
        _l_(597216)

        _c_(597213, _a_(597212, _a_(597211, _n_(597210, "self", lambda: self), "server"), "kill"))
        _l_(597214)
        aux = None
        _l_(597215)
        return aux


a = _c_(597219, _n_(597218, "ApiServer", lambda: ApiServer))
_l_(597220)
_c_(597223, _a_(597222, _n_(597221, "a", lambda: a), "start"))
_l_(597224)
_c_(597226, _n_(597225, "print", lambda: print), "heyy")
_l_(597227)
_c_(597230, _a_(597229, _n_(597228, "a", lambda: a), "terminate"))
_l_(597231)
_c_(597233, _n_(597232, "print", lambda: print), "thread killed")
_l_(597234)