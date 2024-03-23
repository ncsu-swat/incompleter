# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51152635/typeerror-string-indices-must-be-integers-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(702504, _n_(702503, "open", lambda: open), 'file location','r') as f:
    _l_(702510)

    urls =[_c_(702507, _a_(702506, _n_(702505, "line", lambda: line), "strip")) for line in _n_(702508, "f", lambda: f)]
    _l_(702509)


lookup = [ ]
_l_(702511)
for url in _n_(702512, "urls", lambda: urls):
    _l_(702521)

    _c_(702519, _a_(702514, _n_(702513, "lookup", lambda: lookup), "append"), _c_(702518, _n_(702515, "PubMedLookup", lambda: PubMedLookup), _n_(702516, "url", lambda: url),_n_(702517, "email", lambda: email)))
    _l_(702520)
i = 0
_l_(702522)
while True:
    _l_(702539)

    publication = _c_(702526, _n_(702523, "Publication", lambda: Publication), _n_(702524, "lookup", lambda: lookup)[_n_(702525, "i", lambda: i)])
    _l_(702527)
    _c_(702533, _n_(702528, "print", lambda: print), _c_(702532, _a_(702529, """
JOURNAL:\n{journal}\n
""", "format"), **{
            'journal':_a_(702531, _n_(702530, "publication", lambda: publication), "journal"),
            }))
    _l_(702534)
    i +=1
    _l_(702535)
    if _n_(702536, "i", lambda: i) >3:
        _l_(702538)

        break
        _l_(702537)