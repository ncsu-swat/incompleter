# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65199374/typeerror-a-bytes-like-object-is-required-not-str-when-trying-to-write-in-cs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(458028, _n_(458027, "open", lambda: open), 'C:/path_to_csv_file/fold1_1.csv', 'wb') as csvfile:
    _l_(458057)

    spamwriter = _c_(458034, _a_(458030, _n_(458029, "csv", lambda: csv), "writer"), _n_(458031, "csvfile", lambda: csvfile), delimiter=',', quotechar='|', quoting=_a_(458033, _n_(458032, "csv", lambda: csv), "QUOTE_MINIMAL"))
    _l_(458035)
    for row, timeseq in _c_(458039, _n_(458036, "izip", lambda: izip), _n_(458037, "fold1", lambda: fold1), _n_(458038, "fold1_t", lambda: fold1_t)):
        _l_(458056)

        _c_(458054, _a_(458041, _n_(458040, "spamwriter", lambda: spamwriter), "writerow"), [_c_(458046, _a_(458045, _c_(458044, _n_(458042, "unicode", lambda: unicode), _n_(458043, "s", lambda: s)), "encode"), "utf-8") +_c_(458049, _a_(458047, '#{}', "format"), _n_(458048, "t", lambda: t)) for s, t in _c_(458053, _n_(458050, "izip", lambda: izip), _n_(458051, "row", lambda: row), _n_(458052, "timeseq", lambda: timeseq))])
        _l_(458055)