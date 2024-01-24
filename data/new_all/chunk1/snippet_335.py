# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75825362/attributeerror-encode-when-returning-streamingresponse-in-fastapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fastapi import APIRouter, FastAPI, Header
    _l_(376899)

except ImportError:
    pass
try:
    from src.chat.completions import chat_stream
    _l_(376901)

except ImportError:
    pass
try:
    from fastapi.responses import StreamingResponse
    _l_(376903)

except ImportError:
    pass

router = _c_(376905, _n_(376904, "APIRouter", lambda: APIRouter))
_l_(376906)

@_c_(376910, _a_(376908, _n_(376907, "router", lambda: router), "get"), "/v1/completions",response_class=_n_(376909, "StreamingResponse", lambda: StreamingResponse))
def stream_chat(q: _n_(376911, "str", lambda: str), authorization: _n_(376912, "str", lambda: str) = _c_(376914, _n_(376913, "Header", lambda: Header), None)):
    _l_(376931)

    auth_mode, auth_token = _c_(376917, _a_(376916, _n_(376915, "authorization", lambda: authorization), "split"), ' ')
    _l_(376918)
    if _n_(376919, "auth_token", lambda: auth_token) is None:
        _l_(376921)

        aux = "Authorization token is missing"
        _l_(376920)
        return aux
    answer = _c_(376925, _n_(376922, "chat_stream", lambda: chat_stream), _n_(376923, "q", lambda: q), _n_(376924, "auth_token", lambda: auth_token))
    _l_(376926)
    aux = _c_(376929, _n_(376927, "StreamingResponse", lambda: StreamingResponse), _n_(376928, "answer", lambda: answer), media_type="text/event-stream")
    _l_(376930)
    return aux