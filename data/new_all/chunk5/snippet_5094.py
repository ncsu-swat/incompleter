# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71704542/got-error-as-typeerror-list-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for line in _a_(677857, _n_(677856, "sys", lambda: sys), "stdin"):
    _l_(677932)

    myList= _c_(677862, _n_(677858, "list", lambda: list), _c_(677861, _a_(677860, _n_(677859, "line", lambda: line), "split"), "|"))
    _l_(677863)
    temp=_c_(677869, _n_(677864, "list", lambda: list), _c_(677868, _a_(677867, _c_(677866, _n_(677865, "myList", lambda: myList), 0), "split"), " "))
    _l_(677870)
    list1=()
    _l_(677871)
    list2=()
    _l_(677872)
    newList=()
    _l_(677873)
    for ele in _n_(677874, "temp", lambda: temp):
        _l_(677884)

        if _c_(677877, _a_(677876, _n_(677875, "ele", lambda: ele), "strip")):
            _l_(677883)

            _c_(677881, _a_(677879, _n_(677878, "list1", lambda: list1), "append"), _n_(677880, "ele", lambda: ele))
            _l_(677882)
    temp=_c_(677890, _n_(677885, "list", lambda: list), _c_(677889, _a_(677888, _c_(677887, _n_(677886, "mylist", lambda: mylist), 1), "split"), " "))
    _l_(677891)
    for ele in _n_(677892, "temp", lambda: temp):
        _l_(677904)

        if _c_(677895, _a_(677894, _n_(677893, "ele", lambda: ele), "strip")):
            _l_(677903)

            _c_(677901, _a_(677897, _n_(677896, "list2", lambda: list2), "append"), _c_(677900, _a_(677899, _n_(677898, "ele", lambda: ele), "strip")))
            _l_(677902)
    count=0
    _l_(677905)
    for count in _c_(677910, _n_(677906, "range", lambda: range), _c_(677909, _n_(677907, "len", lambda: len), _n_(677908, "list1", lambda: list1))):
        _l_(677927)

        _c_(677923, _a_(677912, _n_(677911, "newList", lambda: newList), "append"), _c_(677917, _n_(677913, "int", lambda: int), _c_(677916, _n_(677914, "list1", lambda: list1), _n_(677915, "count", lambda: count)))*_c_(677922, _n_(677918, "int", lambda: int), _c_(677921, _n_(677919, "list2", lambda: list2), _n_(677920, "count", lambda: count))))
        _l_(677924)
        count=_n_(677925, "count", lambda: count)+1
        _l_(677926)
    _c_(677930, _n_(677928, "print", lambda: print), _n_(677929, "newList", lambda: newList))
    _l_(677931)