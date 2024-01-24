# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55695479/why-cant-i-sort-a-list-of-dicts-in-3-x-why-do-i-get-typeerror-not-suppor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
server_list = []
_l_(379527)

for server in _n_(379528, "res", lambda: res)["aggregations"]["hostname"]["buckets"]:
    _l_(379553)

    temp_obj = []
    _l_(379529)
    _c_(379534, _a_(379531, _n_(379530, "temp_obj", lambda: temp_obj), "append"), {"name":_a_(379533, _n_(379532, "server", lambda: server), "key")})        
    _l_(379535)        
    _c_(379541, _a_(379537, _n_(379536, "temp_obj", lambda: temp_obj), "append"), {"stat": _a_(379540, _n_(379538, "server", lambda: server)["last_log"]["hits"]["hits"][0]["_source"][_n_(379539, "system", lambda: system)], "stat")})
    _l_(379542)
    _c_(379546, _a_(379544, _n_(379543, "server_list", lambda: server_list), "append"), _n_(379545, "temp_obj", lambda: temp_obj))
    _l_(379547)
    _c_(379551, _a_(379549, _n_(379548, "server_list", lambda: server_list), "sort"), key=lambda x: _n_(379550, "x", lambda: x)[0], reverse=False)
    _l_(379552)