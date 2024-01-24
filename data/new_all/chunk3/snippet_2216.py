# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57447483/pandas-dataframe-fails-with-attributeerror-nonetype-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file_list = _c_(529478, _a_(529477, _n_(529476, "glob", lambda: glob), "glob"), "*.json")
_l_(529479)

allFilesDict = {_n_(529480, "v", lambda: v):_n_(529481, "k", lambda: k) for v, k in _c_(529484, _n_(529482, "enumerate", lambda: enumerate), _n_(529483, "file_list", lambda: file_list), 1)}
_l_(529485)

data = []
_l_(529486)

for k,v in _c_(529489, _a_(529488, _n_(529487, "allFilesDict", lambda: allFilesDict), "items")):
    _l_(529504)

    if 1 <= _n_(529490, "k", lambda: k) <= 400000:
        _l_(529503)

        with _c_(529493, _n_(529491, "open", lambda: open), _n_(529492, "v", lambda: v), 'r') as d:
            _l_(529502)

            _c_(529500, _a_(529495, _n_(529494, "data", lambda: data), "append"), _c_(529499, _a_(529497, _n_(529496, "json", lambda: json), "load"), _n_(529498, "d", lambda: d)))
            _l_(529501)

df = _c_(529508, _a_(529506, _n_(529505, "pd", lambda: pd), "DataFrame"), _n_(529507, "data", lambda: data))
_l_(529509)

_c_(529512, _a_(529511, _n_(529510, "df", lambda: df), "to_json"), r'/home/user1/merge/output_1.json', orient='records')
_l_(529513)