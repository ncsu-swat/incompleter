# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/21100117/encountering-typeerror-with-csv-writer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(678053)

except ImportError:
    pass
try:
    import csv
    _l_(678055)

except ImportError:
    pass
try:
    import tempfile
    _l_(678057)

except ImportError:
    pass

def importFromCSV(filepath):
    _l_(678099)

    _c_(678064, _n_(678058, "print", lambda: print), "Reading data from",_c_(678063, _a_(678061, _a_(678060, _n_(678059, "os", lambda: os), "path"), "basename"), _n_(678062, "filepath", lambda: filepath)))
    _l_(678065)
    datalist = []
    _l_(678066)
    with _c_(678069, _n_(678067, "open", lambda: open), _n_(678068, "filepath", lambda: filepath)) as csvfile:
        _l_(678096)

        file_dialect = _c_(678077, _a_(678073, _c_(678072, _a_(678071, _n_(678070, "csv", lambda: csv), "Sniffer")), "sniff"), _c_(678076, _a_(678075, _n_(678074, "csvfile", lambda: csvfile), "readline")),[',',';',':','\t','.'])
        _l_(678078)
        _c_(678081, _a_(678080, _n_(678079, "csvfile", lambda: csvfile), "seek"), 0)
        _l_(678082)
        filereader = _c_(678087, _a_(678084, _n_(678083, "csv", lambda: csv), "reader"), _n_(678085, "csvfile", lambda: csvfile),dialect = _n_(678086, "file_dialect", lambda: file_dialect))
        _l_(678088)
        for row in _n_(678089, "filereader", lambda: filereader):
            _l_(678095)

            _c_(678093, _a_(678091, _n_(678090, "datalist", lambda: datalist), "append"), _n_(678092, "row", lambda: row))
            _l_(678094)
    aux = _n_(678097, "datalist", lambda: datalist)
    _l_(678098)
    return aux

def SplitToTemp(datalist, target_dir):
    _l_(678144)

    tmpnamelist = []
    _l_(678100)
    templist = []
    _l_(678101)
    for item in _n_(678102, "datalist", lambda: datalist):
        _l_(678141)

        if _n_(678103, "item", lambda: item)[0] != '':
            _l_(678140)

            _c_(678107, _a_(678105, _n_(678104, "templist", lambda: templist), "append"), _n_(678106, "item", lambda: item))
            _l_(678108)
        else:
            del item
            _l_(678109)
            f = _c_(678113, _a_(678111, _n_(678110, "tempfile", lambda: tempfile), "NamedTemporaryFile"), delete = False, dir = _n_(678112, "target_dir", lambda: target_dir))
            _l_(678114)
            _c_(678119, _a_(678116, _n_(678115, "tmpnamelist", lambda: tmpnamelist), "append"), _a_(678118, _n_(678117, "f", lambda: f), "name"))
            _l_(678120)
            dw = _c_(678126, _a_(678122, _n_(678121, "csv", lambda: csv), "writer"), _n_(678123, "f", lambda: f), delimiter = ',', quotechar = '|', quoting = _a_(678125, _n_(678124, "csv", lambda: csv), "QUOTE_MINIMAL"))
            _l_(678127)
            for row in _n_(678128, "templist", lambda: templist):
                _l_(678134)

                _c_(678132, _a_(678130, _n_(678129, "dw", lambda: dw), "writerow"), _n_(678131, "row", lambda: row))
                _l_(678133)
            _c_(678137, _a_(678136, _n_(678135, "f", lambda: f), "close"))
            _l_(678138)
            templist = []
            _l_(678139)
    aux = _n_(678142, "tmpnamelist", lambda: tmpnamelist)
    _l_(678143)
    return aux

###############################################################################
pathname = _c_(678148, _a_(678147, _a_(678146, _n_(678145, "os", lambda: os), "path"), "normpath"), 'C:/Python33/myprograms/myclassandfx/BenchLink/blrtest.csv')
_l_(678149)
tempdir = _c_(678159, _a_(678151, _n_(678150, "tempfile", lambda: tempfile), "mkdtemp"), dir = _c_(678158, _a_(678154, _a_(678153, _n_(678152, "os", lambda: os), "path"), "normpath"), 'c:/users/'+_c_(678157, _a_(678156, _n_(678155, "os", lambda: os), "getlogin"))+'/desktop'))
_l_(678160)

filedata = _c_(678163, _n_(678161, "import_from_csv", lambda: import_from_csv), _n_(678162, "pathname", lambda: pathname))
_l_(678164)
tempnames = _c_(678168, _n_(678165, "SplitToTemp", lambda: SplitToTemp), _n_(678166, "filedata", lambda: filedata), _n_(678167, "tempdir", lambda: tempdir))
_l_(678169)