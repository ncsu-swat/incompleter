# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43657351/typeerror-a-bytes-like-object-is-required-not-str-error-getting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(444516)

except ImportError:
    pass

fin = _c_(444518, _n_(444517, "open", lambda: open), 'another_summary_table.csv')
_l_(444519)
words = ["PCB","Switch","Socket","Red-Green LED","Solar Panel","Battery", "Load wire"]
_l_(444520)
found = {}
_l_(444521)

wr = _c_(444526, _a_(444523, _n_(444522, "csv", lambda: csv), "writer"), _c_(444525, _n_(444524, "open", lambda: open), "boop-1.csv", "wb"))
_l_(444527)
fieldnames = ['PartsReplaced']
_l_(444528)
writer = _c_(444533, _a_(444530, _n_(444529, "csv", lambda: csv), "DictWriter"), _n_(444531, "fin", lambda: fin), fieldnames=_n_(444532, "fieldnames", lambda: fieldnames))
_l_(444534)
for line in _n_(444535, "fin", lambda: fin):
    _l_(444557)

    split_line=_c_(444538, _a_(444537, _n_(444536, "line", lambda: line), "split"), ',')
    _l_(444539)
    str1=_n_(444540, "split_line", lambda: split_line)[2] # Whatever columns
    _l_(444541) # Whatever columns
    PartsReplaced=_n_(444542, "split_line", lambda: split_line)[2] # Whatever columns
    _l_(444543) # Whatever columns

    for w in _n_(444544, "words", lambda: words):
        _l_(444556)

        if _n_(444545, "w", lambda: w) in _n_(444546, "str1", lambda: str1):
            _l_(444555)

            _n_(444547, "found", lambda: found)[_n_(444548, "w", lambda: w)]=_c_(444552, _a_(444550, _n_(444549, "found", lambda: found), "get"), _n_(444551, "w", lambda: w),0)+1
            _l_(444553)

            break
            _l_(444554)
_c_(444561, _a_(444559, _n_(444558, "wr", lambda: wr), "writerows"), _n_(444560, "found", lambda: found))
_l_(444562)