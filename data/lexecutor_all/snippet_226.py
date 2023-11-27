# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/9733638/how-to-post-json-data-with-python-requests
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def POST_request():
    _l_(1538259)

    with _c_(1538245, _n_(1538244, "open", lambda: open), "FILE PATH", "r") as data:
        _l_(1538250)

        JSON_Body = _c_(1538248, _a_(1538247, _n_(1538246, "data", lambda: data), "read"))
        _l_(1538249)
    response = _c_(1538254, _a_(1538252, _n_(1538251, "requests", lambda: requests), "post"), url="URL", data=_n_(1538253, "JSON_Body", lambda: JSON_Body))
    _l_(1538255)
    assert _a_(1538257, _n_(1538256, "response", lambda: response), "status_code") == 200
    _l_(1538258)

