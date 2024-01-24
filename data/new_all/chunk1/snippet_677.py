# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58817559/iterating-on-dictionary-throws-typeerror-list-indices-must-be-integers-or-slice
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
num_detections = _c_(386713, _n_(386711, "int", lambda: int), _n_(386712, "detection", lambda: detection)['num_detections'])
_l_(386714)
output_dict = {_n_(386715, "key", lambda: key):_c_(386719, _a_(386718, _n_(386716, "value", lambda: value)[0, :_n_(386717, "num_detections", lambda: num_detections)], "numpy")) 
                for key,value in _c_(386722, _a_(386721, _n_(386720, "detection", lambda: detection), "items"))}
_l_(386723)