# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65592003/how-to-fix-typeerror-cant-pickle-module-objects-during-multiprocessing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def process(x):
    _l_(390925)

    my_file = _a_(390923, _a_(390922, _n_(390921, "x", lambda: x), "resources")['DICOM'], "files")[0] 
    _l_(390924) 

def another_method():
    _l_(390941)

    ...                
    _l_(390926)                
    pool = _c_(390931, _n_(390927, "Pool", lambda: Pool), _c_(390930, _a_(390929, _n_(390928, "os", lambda: os), "cpu_count")))
    _l_(390932)
    _c_(390939, _a_(390934, _n_(390933, "pool", lambda: pool), "map"), _n_(390935, "process", lambda: process), [_n_(390936, "scans", lambda: scans)[_n_(390937, "sc", lambda: sc)] for sc in _n_(390938, "scans", lambda: scans)])
    _l_(390940)

_c_(390943, _n_(390942, "another_method", lambda: another_method))  
_l_(390944)  