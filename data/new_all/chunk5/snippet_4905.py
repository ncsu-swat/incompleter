# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41284027/python3-csv-typeerror-valueerror-csv-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
filename = "data.csv"
_l_(685512)
temp_file = _c_(685514, _n_(685513, "NamedTemporaryFile", lambda: NamedTemporaryFile), delete=False)
_l_(685515)

with _c_(685518, _n_(685516, "open", lambda: open), _n_(685517, "filename", lambda: filename), "rb") as csvfile, _n_(685519, "temp_file", lambda: temp_file):
    _l_(685532)

    reader = _c_(685523, _a_(685521, _n_(685520, "csv", lambda: csv), "DictReader"), _n_(685522, "csvfile", lambda: csvfile))
    _l_(685524)
    fieldnames = ["id", "name", "email", "amount", "sent"]
    _l_(685525)
    writer = _c_(685530, _a_(685527, _n_(685526, "csv", lambda: csv), "DictWriter"), _n_(685528, "temp_file", lambda: temp_file), fieldnames=_n_(685529, "fieldnames", lambda: fieldnames))
    _l_(685531)


for row in _n_(685533, "reader", lambda: reader):
    _l_(685545)

    _c_(685536, _n_(685534, "print", lambda: print), _n_(685535, "row", lambda: row))
    _l_(685537)
    _c_(685543, _a_(685539, _n_(685538, "writer", lambda: writer), "writerow"), {
            "id": _n_(685540, "row", lambda: row)["id"],
            "name": _n_(685541, "row", lambda: row)["name"],
            "email": _n_(685542, "row", lambda: row)["email"],
            "amount": "1293.23",
            "sent": ""
        })
    _l_(685544)