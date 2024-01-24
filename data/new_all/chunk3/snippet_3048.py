# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51644941/typeerror-csv-reader-object-is-not-subscriptable
#!/usr/bin/python
# -*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(572949)

except ImportError:
    pass

la = _c_(572951, _n_(572950, "open", lambda: open), 'loginscruz.csv', 'r')
_l_(572952)
listaluno = _c_(572956, _a_(572954, _n_(572953, "csv", lambda: csv), "reader"), _n_(572955, "la", lambda: la),delimiter=';')
_l_(572957)

for alunos in _n_(572958, "listaluno", lambda: listaluno)[1:]:
    _l_(572970)


    num = 1
    _l_(572959)

    aluno = _c_(572962, _n_(572960, "str", lambda: str), _n_(572961, "alunos", lambda: alunos)[3])
    _l_(572963)

    if (_n_(572964, "aluno", lambda: aluno) != ''):
        _l_(572969)

        _c_(572967, _n_(572965, "print", lambda: print), _n_(572966, "aluno", lambda: aluno) + " batata")
        _l_(572968)