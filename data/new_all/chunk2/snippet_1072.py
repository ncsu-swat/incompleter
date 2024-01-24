# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46100312/streaming-data-from-amazon-s3-using-smart-open-causing-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import smart_open
    _l_(451805)

except ImportError:
    pass

def stream_data():
    _l_(451821)

    my_bucket = 'monkey-business-dev'
    _l_(451806)
    my_key = 'incoming_monkey_data/banana/banana'
    _l_(451807)
    uri = _c_(451811, _a_(451808, 's3://{}/{}', "format"), _n_(451809, "my_bucket", lambda: my_bucket), _n_(451810, "my_key", lambda: my_key))
    _l_(451812)
    total_lines = 0
    _l_(451813)
    total_records = 0
    _l_(451814)
    for line in _c_(451818, _a_(451816, _n_(451815, "smart_open", lambda: smart_open), "smart_open"), _n_(451817, "uri", lambda: uri)):
        _l_(451820)

        total_records += 1
        _l_(451819)


if _n_(451822, "__name__", lambda: __name__) == '__main__':
    _l_(451826)

    _c_(451824, _n_(451823, "stream_data", lambda: stream_data))
    _l_(451825)