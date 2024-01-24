# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71743807/typeerror-reverse-takes-exactly-2-arguments-1-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class StartAssessment(_a_(390599, _n_(390598, "generics", lambda: generics), "GenericAPIView")):
    _l_(390645)

    
    def post(self, request, *args, **kwargs):
        _l_(390644)

        data = _a_(390601, _n_(390600, "request", lambda: request), "data")
        _l_(390602)
        request = _c_(390605, _n_(390603, "build_rp_request", lambda: build_rp_request), _n_(390604, "data", lambda: data))
        _l_(390606)
        response = _c_(390609, _n_(390607, "post_to_app_start_assessment", lambda: post_to_app_start_assessment), _n_(390608, "request", lambda: request))
        _l_(390610)
        path = _c_(390613, _n_(390611, "get_path", lambda: get_path), _n_(390612, "response", lambda: response))
        _l_(390614)
        step = _c_(390617, _n_(390615, "get_step", lambda: get_step), _n_(390616, "response", lambda: response))
        _l_(390618)
        _n_(390619, "data", lambda: data)["path"] = _n_(390620, "path", lambda: path)
        _l_(390621)
        _n_(390622, "data", lambda: data)["step"] = _n_(390623, "step", lambda: step)
        _l_(390624)
        request = _c_(390627, _n_(390625, "build_rp_request", lambda: build_rp_request), _n_(390626, "data", lambda: data))
        _l_(390628)
        app_response = _c_(390632, _n_(390629, "post_to_app", lambda: post_to_app), _n_(390630, "request", lambda: request), _n_(390631, "path", lambda: path))
        _l_(390633)
        message = _c_(390636, _n_(390634, "format_message", lambda: format_message), _n_(390635, "app_response", lambda: app_response))
        _l_(390637)
        aux = _c_(390642, _n_(390638, "Response", lambda: Response), _n_(390639, "message", lambda: message), status=_a_(390641, _n_(390640, "status", lambda: status), "HTTP_200_OK"))
        _l_(390643)
        return aux