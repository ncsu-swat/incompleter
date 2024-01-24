# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65199374/typeerror-a-bytes-like-object-is-required-not-str-when-trying-to-write-in-cs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(438377, _n_(438376, "open", lambda: open), 'C:/Users/path_to_csv_file/fold1_1.csv', 'wb') as csvfile:
    _l_(438409)

    spamwriter = _c_(438383, _a_(438379, _n_(438378, "csv", lambda: csv), "writer"), _n_(438380, "csvfile", lambda: csvfile), delimiter=',', quotechar='|', quoting=_a_(438382, _n_(438381, "csv", lambda: csv), "QUOTE_MINIMAL"))
    _l_(438384)
    for row, timeseq in _c_(438388, _n_(438385, "zip", lambda: zip), _n_(438386, "fold1", lambda: fold1), _n_(438387, "fold1_t", lambda: fold1_t)):
        _l_(438408)

        for s, t in _c_(438392, _n_(438389, "zip", lambda: zip), _n_(438390, "row", lambda: row), _n_(438391, "timeseq", lambda: timeseq)):
            _l_(438407)

            bytes_var = _c_(438395, _a_(438394, _n_(438393, "s", lambda: s), "encode"), 'utf-8') +_c_(438400, _a_(438399, _c_(438398, _a_(438396, '#{}', "format"), _n_(438397, "t", lambda: t)), "encode"), 'utf-8') 
            _l_(438401) 
            _c_(438405, _a_(438403, _n_(438402, "spamwriter", lambda: spamwriter), "writerow"), _n_(438404, "bytes_var", lambda: bytes_var))
            _l_(438406)