# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51684913/typeerror-int-object-is-not-iterable-using-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(469737)

except ImportError:
    pass
try:
    import csv
    _l_(469739)

except ImportError:
    pass

with _c_(469741, _n_(469740, "open", lambda: open), 'leap_data.json') as f:
    _l_(469747)

    data = _c_(469745, _a_(469743, _n_(469742, "json", lambda: json), "load"), _n_(469744, "f", lambda: f))
    _l_(469746)
#print(data)
cnt=0
_l_(469748)
final_list={}
_l_(469749)

for k,v in _c_(469752, _a_(469751, _n_(469750, "data", lambda: data), "items")):
    _l_(469796)

    for m,n in _c_(469755, _a_(469754, _n_(469753, "v", lambda: v), "items")):
        _l_(469795)

        #print n
        cnt=_n_(469756, "cnt", lambda: cnt)+1
        _l_(469757)
        #print cnt
        if _n_(469758, "cnt", lambda: cnt)==6:
            _l_(469794)

            #print n
            for data1 in _n_(469759, "n", lambda: n):
                _l_(469777)

                for a,b in _c_(469762, _a_(469761, _n_(469760, "data1", lambda: data1), "items")):
                    _l_(469767)

                    _n_(469763, "final_list", lambda: final_list)[_n_(469764, "a", lambda: a)]=_n_(469765, "b", lambda: b)    
                    _l_(469766)    
                with _c_(469769, _n_(469768, "open", lambda: open), 'output4.json', 'a') as outfile:
                    _l_(469776)

                    _c_(469774, _a_(469771, _n_(469770, "json", lambda: json), "dump"), _n_(469772, "final_list", lambda: final_list),_n_(469773, "outfile", lambda: outfile))
                    _l_(469775)

            my_list = "["+_c_(469783, _a_(469782, _c_(469781, _a_(469780, _c_(469779, _n_(469778, "open", lambda: open), 'output4.json'), "read")), "replace"), "}{","},{")+"]"
            _l_(469784)
            data_1 = _c_(469788, _a_(469786, _n_(469785, "json", lambda: json), "loads"), _n_(469787, "my_list", lambda: my_list))
            _l_(469789)
            _c_(469792, _n_(469790, "print", lambda: print), _n_(469791, "data_1", lambda: data_1))
            _l_(469793)


with _c_(469798, _n_(469797, "open", lambda: open), r'samp.csv', 'w+') as csvfile:
    _l_(469820)

    output = _c_(469802, _a_(469800, _n_(469799, "csv", lambda: csv), "writer"), _n_(469801, "csvfile", lambda: csvfile))
    _l_(469803)
    _c_(469809, _a_(469805, _n_(469804, "output", lambda: output), "writerow"), _c_(469808, _a_(469807, _n_(469806, "data_1", lambda: data_1)[0], "keys")))
    _l_(469810)
    for row in _n_(469811, "data_1", lambda: data_1):
        _l_(469819)

        _c_(469817, _a_(469813, _n_(469812, "output", lambda: output), "writerow"), _c_(469816, _a_(469815, _n_(469814, "row", lambda: row), "values")))
        _l_(469818)