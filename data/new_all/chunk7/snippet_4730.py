# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51152635/typeerror-string-indices-must-be-integers-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(676404, _n_(676403, "open", lambda: open), 'file location','r') as f:
    _l_(676410)

    urls =[_c_(676407, _a_(676406, _n_(676405, "line", lambda: line), "strip")) for line in _n_(676408, "f", lambda: f)]
    _l_(676409)


lookup = [ ]
_l_(676411)
for url in _n_(676412, "urls", lambda: urls):
    _l_(676421)

    _c_(676419, _a_(676414, _n_(676413, "lookup", lambda: lookup), "append"), _c_(676418, _n_(676415, "PubMedLookup", lambda: PubMedLookup), _n_(676416, "url", lambda: url),_n_(676417, "email", lambda: email)))
    _l_(676420)
i = 0
_l_(676422)
while True:
    _l_(676439)

    publication = _c_(676426, _n_(676423, "Publication", lambda: Publication), _n_(676424, "lookup", lambda: lookup)[_n_(676425, "i", lambda: i)])
    _l_(676427)
    _c_(676433, _n_(676428, "print", lambda: print), _c_(676432, _a_(676429, """
JOURNAL:\n{journal}\n
""", "format"), **{
            'journal':_a_(676431, _n_(676430, "publication", lambda: publication), "journal"),
            }))
    _l_(676434)
    i +=1
    _l_(676435)
    if _n_(676436, "i", lambda: i) >3:
        _l_(676438)

        break
        _l_(676437)