# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54575314/typeerror-sequence-item-0-expected-str-instance-nonetype-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(685466)

except ImportError:
    pass
try:
    from sklearn import preprocessing
    _l_(685468)

except ImportError:
    pass

input_labels=['red','black','red','green','black','yellow','white']
_l_(685469)
encoder=_c_(685472, _a_(685471, _n_(685470, "preprocessing", lambda: preprocessing), "LabelEncoder"))
_l_(685473)
_c_(685477, _a_(685475, _n_(685474, "encoder", lambda: encoder), "fit"), _n_(685476, "input_labels", lambda: input_labels))
_l_(685478)

_c_(685480, _n_(685479, "print", lambda: print), "\nLabel Mapping:")
_l_(685481)
for i,item in _c_(685485, _n_(685482, "enumerate", lambda: enumerate), _a_(685484, _n_(685483, "encoder", lambda: encoder), "classes_")):
    _l_(685491)

    _c_(685489, _n_(685486, "print", lambda: print), _n_(685487, "item", lambda: item), '--->',_n_(685488, "i", lambda: i))
    _l_(685490)

_c_(685503, _n_(685492, "print", lambda: print), "\nLabel Mapping:",_c_(685502, _a_(685493, '', "join"), (_c_(685497, _n_(685494, "print", lambda: print), _n_(685495, "item", lambda: item), '--->',_n_(685496, "i", lambda: i)) for i,item in 
_c_(685501, _n_(685498, "enumerate", lambda: enumerate), _a_(685500, _n_(685499, "encoder", lambda: encoder), "classes_")))))
_l_(685504)