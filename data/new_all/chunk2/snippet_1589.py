# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74549909/bentoml-localhost-server-returns-with-typeerror-runnermethod-object-is-not-ca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(453316)

except ImportError:
    pass
try:
    from sys import argv
    _l_(453318)

except ImportError:
    pass
try:
    import numpy as np
    _l_(453320)

except ImportError:
    pass
try:
    import requests
    _l_(453322)

except ImportError:
    pass

SERVICE_URL = "http://localhost:3000/predict"
_l_(453323)

def make_request_to_bento_service(service_url: _n_(453324, "str", lambda: str), input_array: _a_(453326, _n_(453325, "np", lambda: np), "ndarray")) -> _n_(453327, "str", lambda: str):
    _l_(453344)

    serialized_input_data = _c_(453333, _a_(453329, _n_(453328, "json", lambda: json), "dumps"), _c_(453332, _a_(453331, _n_(453330, "input_array", lambda: input_array), "tolist")))
    _l_(453334)
    response = _c_(453339, _a_(453336, _n_(453335, "requests", lambda: requests), "post"), _n_(453337, "service_url", lambda: service_url),
        data=_n_(453338, "serialized_input_data", lambda: serialized_input_data),
        headers={"Content-Type": "application/json"}
        )
    _l_(453340)
    aux = _a_(453342, _n_(453341, "response", lambda: response), "text")
    _l_(453343)
    return aux

def main():
    _l_(453366)

    # Read the data from argv as an np.ndarray
    input_data = _c_(453351, _a_(453346, _n_(453345, "np", lambda: np), "array"), [_c_(453349, _n_(453347, "float", lambda: float), _n_(453348, "x", lambda: x)) for x in _n_(453350, "argv", lambda: argv)[1:]])
    _l_(453352)
    _c_(453355, _n_(453353, "print", lambda: print), _n_(453354, "input_data", lambda: input_data))
    _l_(453356)
    prediction = _c_(453360, _n_(453357, "make_request_to_bento_service", lambda: make_request_to_bento_service), _n_(453358, "SERVICE_URL", lambda: SERVICE_URL), _n_(453359, "input_data", lambda: input_data))
    _l_(453361)
    _c_(453364, _n_(453362, "print", lambda: print), _n_(453363, "prediction", lambda: prediction))
    _l_(453365)

if _n_(453367, "__name__", lambda: __name__) == "__main__":
    _l_(453371)

    _c_(453369, _n_(453368, "main", lambda: main))
    _l_(453370)