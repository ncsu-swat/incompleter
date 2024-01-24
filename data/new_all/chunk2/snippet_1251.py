# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63092814/typeerror-not-supported-between-instances-of-int-and-tuple-python-pand
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def int_checker_projects(columnName):
    _l_(454255)

    intArray = []
    _l_(454231)
    for value in _n_(454232, "projectsFileData", lambda: projectsFileData)[_n_(454233, "columnName", lambda: columnName)]:
        _l_(454252)

        try:
            _l_(454251)

            _c_(454239, _a_(454235, _n_(454234, "intArray", lambda: intArray), "append"), _c_(454238, _n_(454236, "int", lambda: int), _n_(454237, "value", lambda: value)))
            _l_(454240)
        except _n_(454241, "ValueError", lambda: ValueError):
            _l_(454250)

            _c_(454248, _a_(454243, _n_(454242, "sys", lambda: sys), "exit"), _c_(454247, _a_(454244, "ERROR: {0} in the {1} column is not an integer. Terminating Program.", "format"), _n_(454245, "value", lambda: value), _n_(454246, "columnName", lambda: columnName)))
            _l_(454249)
    aux = _n_(454253, "intArray", lambda: intArray)
    _l_(454254)
    return aux

projectIDs = _c_(454257, _n_(454256, "int_checker_projects", lambda: int_checker_projects), 'projectID')
_l_(454258)

for pid in _c_(454261, _n_(454259, "zip", lambda: zip), _n_(454260, "projectIDs", lambda: projectIDs)):
    _l_(454273)

    if _c_(454263, _n_(454262, "pow", lambda: pow), 2, 64) < _n_(454264, "pid", lambda: pid) < 0:
        _l_(454272)

        _c_(454270, _a_(454266, _n_(454265, "sys", lambda: sys), "exit"), _c_(454269, _a_(454267, "ERROR: projectID {0} must be an integer greater than zero and less than 2^64.", "format"), _n_(454268, "pid", lambda: pid)))
        _l_(454271)