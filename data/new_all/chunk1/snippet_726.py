# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40535615/python-typeerror-with-for-logic-iterating-data-values
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(393963)

except ImportError:
    pass
try:
    import csv
    _l_(393965)

except ImportError:
    pass

with _c_(393967, _n_(393966, "open", lambda: open), 'C:\\folder\\dev\\TagAlarms.txt',"r") as file:
    _l_(393973)

    data = _c_(393971, _a_(393969, _n_(393968, "json", lambda: json), "load"), _n_(393970, "file", lambda: file))
    _l_(393972)

with _c_(393975, _n_(393974, "open", lambda: open), 'C:\\folder\\dev\\TagAlarms.csv',"w",newline='') as file:
    _l_(393995)

    csv_file = _c_(393979, _a_(393977, _n_(393976, "csv", lambda: csv), "writer"), _n_(393978, "file", lambda: file))
    _l_(393980)
    for dev in _n_(393981, "data", lambda: data)["devs"]:
        _l_(393994)

        for tag in _n_(393982, "dev", lambda: dev)["tags"]:
            _l_(393993)

            for alarm in _n_(393983, "tag", lambda: tag)["alarmst"]:
                _l_(393992)

                _c_(393990, _a_(393985, _n_(393984, "csv_file", lambda: csv_file), "writerow"), _n_(393986, "alarm", lambda: alarm)['dateStatus'],[_n_(393987, "alarm", lambda: alarm)['dateStart'], _n_(393988, "alarm", lambda: alarm)['status'], _n_(393989, "alarm", lambda: alarm)['type']])
                _l_(393991)