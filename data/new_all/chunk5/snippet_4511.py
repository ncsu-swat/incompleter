# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56440957/how-do-i-fix-typeerror-unhashable-type-rqm-cell-auto-generated-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import python_jsonschema_objects as pjs
    _l_(686825)

except ImportError:
    pass
schema = {}
_l_(686826)
_n_(686827, "schema", lambda: schema)['Rqm'] = 'rqm.json'
_l_(686828)
builder = _c_(686832, _a_(686830, _n_(686829, "pjs", lambda: pjs), "ObjectBuilder"), _n_(686831, "schema", lambda: schema)['Rqm'])
_l_(686833)
ns = _c_(686836, _a_(686835, _n_(686834, "builder", lambda: builder), "build_classes"))
_l_(686837)
Cell = _a_(686839, _n_(686838, "ns", lambda: ns), "RqmCell")
_l_(686840)
CellSet = _a_(686842, _n_(686841, "ns", lambda: ns), "RqmCellset")
_l_(686843)
cellSet = None
_l_(686844)
GSMCell = _c_(686846, _n_(686845, "Cell", lambda: Cell), rat='GSM', bandwidth='BW_1_4_MHZ')
_l_(686847)
cellSet = _c_(686850, _n_(686848, "CellSet", lambda: CellSet), cellsToDeploy=[_n_(686849, "GSMCell", lambda: GSMCell)])
_l_(686851)