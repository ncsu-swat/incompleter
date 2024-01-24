# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58019067/filenotfounderror-when-using-os-rename-but-not-when-calling-up-print-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os, csv
    _l_(531733)

except ImportError:
    pass

_c_(531736, _a_(531735, _n_(531734, "os", lambda: os), "chdir"), "/Users/.../test11")
_l_(531737)
root = "/Users/.../test11"
_l_(531738)

for file in _c_(531741, _a_(531740, _n_(531739, "os", lambda: os), "listdir")):
    _l_(531758)

    if _c_(531744, _a_(531743, _n_(531742, "file", lambda: file), "endswith"), ".DS_Store"):
        _l_(531757)

        path = _c_(531750, _a_(531747, _a_(531746, _n_(531745, "os", lambda: os), "path"), "join"), _n_(531748, "root", lambda: root), _n_(531749, "file", lambda: file))
        _l_(531751)
        _c_(531755, _a_(531753, _n_(531752, "os", lambda: os), "remove"), _n_(531754, "path", lambda: path))
        _l_(531756)

src = "/Users/.../test11/temp_name" # rename (date/name/index)
_l_(531759) # rename (date/name/index)
csvFilePath = "/Users/.../test11/temp_name/data.csv"
_l_(531760)
with _c_(531763, _n_(531761, "open", lambda: open), _n_(531762, "csvFilePath", lambda: csvFilePath)) as csvFile:
    _l_(531786)

    csvReader = _c_(531767, _a_(531765, _n_(531764, "csv", lambda: csv), "DictReader"), _n_(531766, "csvFile", lambda: csvFile))
    _l_(531768)
    for csvRow in _n_(531769, "csvReader", lambda: csvReader):
        _l_(531785)

        timestamp = _n_(531770, "csvRow", lambda: csvRow)["Timestamp"]
        _l_(531771)
        name = _n_(531772, "csvRow", lambda: csvRow)["First name"]
        _l_(531773)
        for index, folder in _c_(531779, _n_(531774, "enumerate", lambda: enumerate), _c_(531778, _a_(531776, _n_(531775, "os", lambda: os), "listdir"), _n_(531777, "root", lambda: root)), start=1):
            _l_(531784)

            new_folder_name = f"{_n_(531780, 'timestamp', lambda: timestamp)}_{_n_(531781, 'name', lambda: name)}_{_n_(531782, 'index', lambda: index)}"
            _l_(531783)
_c_(531791, _a_(531788, _n_(531787, "os", lambda: os), "rename"), _n_(531789, "src", lambda: src), _n_(531790, "new_folder_name", lambda: new_folder_name))
_l_(531792)