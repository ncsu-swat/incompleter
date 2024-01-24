# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55616035/typeerror-object-of-type-bytes-is-not-json-serializable-live-streaming-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(647024)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(647026)

except ImportError:
    pass
try:
    from datetime import timedelta
    _l_(647028)

except ImportError:
    pass
try:
    import requests
    _l_(647030)

except ImportError:
    pass
try:
    import json
    _l_(647032)

except ImportError:
    pass
try:
    import time
    _l_(647034)

except ImportError:
    pass
try:
    import random
    _l_(647036)

except ImportError:
    pass

# function for data_generation

def data_generation():
    _l_(647062)

    surr_id = _c_(647039, _a_(647038, _n_(647037, "random", lambda: random), "randint"), 1, 3)
    _l_(647040)
    speed = _c_(647043, _a_(647042, _n_(647041, "random", lambda: random), "randint"), 20, 200)
    _l_(647044)
    date = _c_(647049, _a_(647048, _c_(647047, _a_(647046, _n_(647045, "datetime", lambda: datetime), "today")), "strftime"), "%Y-%m-%d")
    _l_(647050)
    time = _c_(647055, _a_(647054, _c_(647053, _a_(647052, _n_(647051, "datetime", lambda: datetime), "now")), "isoformat"))
    _l_(647056)
    aux = [_n_(647057, "surr_id", lambda: surr_id), _n_(647058, "speed", lambda: speed), _n_(647059, "date", lambda: date), _n_(647060, "time", lambda: time)]
    _l_(647061)

    return aux


if _n_(647063, "__name__", lambda: __name__) == '__main__':
    _l_(647126)


    REST_API_URL = 'api_url'
    _l_(647064)

    while True:
        _l_(647125)

        data_raw = []
        _l_(647065)
        for j in _c_(647067, _n_(647066, "range", lambda: range), 1):
            _l_(647080)

            row = _c_(647069, _n_(647068, "data_generation", lambda: data_generation))
            _l_(647070)
            _c_(647074, _a_(647072, _n_(647071, "data_raw", lambda: data_raw), "append"), _n_(647073, "row", lambda: row))
            _l_(647075)
            _c_(647078, _n_(647076, "print", lambda: print), "Raw data - ", _n_(647077, "data_raw", lambda: data_raw))
            _l_(647079)

        # set the header record
        HEADER = ["surr_id", "speed", "date", "time"]
        _l_(647081)

        data_df = _c_(647086, _a_(647083, _n_(647082, "pd", lambda: pd), "DataFrame"), _n_(647084, "data_raw", lambda: data_raw), columns=_n_(647085, "HEADER", lambda: HEADER))
        _l_(647087)
        data_json = _c_(647092, _n_(647088, "bytes", lambda: bytes), _c_(647091, _a_(647090, _n_(647089, "data_df", lambda: data_df), "to_json"), orient='records'), encoding='utf-8')
        _l_(647093)
        _c_(647096, _n_(647094, "print", lambda: print), "JSON dataset", _n_(647095, "data_json", lambda: data_json))
        _l_(647097)

        # Post the data on the Power BI API
        try:
            _l_(647120)

            req = _c_(647106, _a_(647099, _n_(647098, "requests", lambda: requests), "post"), _n_(647100, "REST_API_URL", lambda: REST_API_URL), data=_c_(647104, _a_(647102, _n_(647101, "json", lambda: json), "dumps"), _n_(647103, "data_json", lambda: data_json)), headers=_n_(647105, "HEADER", lambda: HEADER), timeout=5)
            _l_(647107)
            _c_(647109, _n_(647108, "print", lambda: print), "Data posted in Power BI API")
            _l_(647110)
        except _a_(647113, _a_(647112, _n_(647111, "requests", lambda: requests), "exceptions"), "ConnectionError") as e:
            _l_(647119)

            req = "No response"
            _l_(647114)
            _c_(647117, _n_(647115, "print", lambda: print), _n_(647116, "req", lambda: req))
            _l_(647118)

        _c_(647123, _a_(647122, _n_(647121, "time", lambda: time), "sleep"), 3)
        _l_(647124)