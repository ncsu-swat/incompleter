# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45763916/when-i-tried-to-get-json-structure-i-got-this-typeerror-list-indices-must-be-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from client import RestClient
    _l_(531572)

except ImportError:
    pass

client = _c_(531574, _n_(531573, "RestClient", lambda: RestClient), "jxxxxxx@xxxx.com", "xxxxxxxyyyyy")
_l_(531575)
completed_tasks_response = _c_(531578, _a_(531577, _n_(531576, "client", lambda: client), "get"), "/v2/srp_tasks_get")
_l_(531579)
if _n_(531580, "completed_tasks_response", lambda: completed_tasks_response)["status"] == "error":
    _l_(531613)

    _c_(531584, _n_(531581, "print", lambda: print), "error. Code: %d Message: %s" % (_n_(531582, "completed_tasks_response", lambda: completed_tasks_response)["error"]["code"], _n_(531583, "completed_tasks_response", lambda: completed_tasks_response)["error"]["message"]))
    _l_(531585)
else:
    results = _n_(531586, "completed_tasks_response", lambda: completed_tasks_response)["results"]
    _l_(531587)
    _c_(531590, _n_(531588, "print", lambda: print), _n_(531589, "results", lambda: results))
    _l_(531591)
    for result_id in _n_(531592, "results", lambda: results):
        _l_(531612)

        result = _n_(531593, "results", lambda: results)[_n_(531594, "result_id", lambda: result_id)]
        _l_(531595)
        srp_response = _c_(531599, _a_(531597, _n_(531596, "client", lambda: client), "get"), "/v2/srp_tasks_get/%d" % (_n_(531598, "result", lambda: result)["142657080"]))
        _l_(531600)
        if _n_(531601, "srp_response", lambda: srp_response)["status"] == "error":
            _l_(531611)

            _c_(531605, _n_(531602, "print", lambda: print), "error. Code: %d Message: %s" % (_n_(531603, "srp_response", lambda: srp_response)["error"]["code"], _n_(531604, "srp_response", lambda: srp_response)["error"]["message"]))
            _l_(531606)
        else:
            _c_(531609, _n_(531607, "print", lambda: print), _n_(531608, "srp_response", lambda: srp_response)["results"])
            _l_(531610)