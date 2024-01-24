# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34905187/compression-strings-list-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import zlib
    _l_(348273)

except ImportError:
    pass
sentence = _c_(348275, _n_(348274, "input", lambda: input), "Enter the text you want to compress: ")
_l_(348276)
listSentence = _c_(348279, _a_(348278, _n_(348277, "sentence", lambda: sentence), "split"), " ")
_l_(348280)
d = {}
_l_(348281)
i = 0
_l_(348282)
values = []
_l_(348283)
for i, word in _c_(348288, _n_(348284, "enumerate", lambda: enumerate), _c_(348287, _a_(348286, _n_(348285, "sentence", lambda: sentence), "split"), " ")):
    _l_(348299)

    if not _n_(348289, "word", lambda: word) in _n_(348290, "d", lambda: d):
        _l_(348295)

        _n_(348291, "d", lambda: d)[_n_(348292, "word", lambda: word)] = (_n_(348293, "i", lambda: i)+1)
        _l_(348294)
    values += [_n_(348296, "d", lambda: d)[_n_(348297, "word", lambda: word)]]
    _l_(348298)
coms = _c_(348305, _a_(348301, _n_(348300, "zlib", lambda: zlib), "compress"), _c_(348304, _a_(348303, _n_(348302, "sentence", lambda: sentence), "encode"), 'utf-8'))
_l_(348306)
comv = _c_(348312, _a_(348308, _n_(348307, "zlib", lambda: zlib), "compress"), _c_(348311, _a_(348310, _n_(348309, "values", lambda: values), "encode"), 'utf-8'))
_l_(348313)
with _c_(348315, _n_(348314, "open", lambda: open), "listofwords.txt", "wb") as myfile:
    _l_(348326)

    _c_(348319, _a_(348317, _n_(348316, "myfile", lambda: myfile), "write"), _n_(348318, "coms", lambda: coms))
    _l_(348320)
    _c_(348324, _a_(348322, _n_(348321, "myfile", lambda: myfile), "write"), _n_(348323, "comv", lambda: comv))
    _l_(348325)