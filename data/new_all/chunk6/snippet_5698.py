# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62576200/filenotfounderror-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(350104, "boolErrorsOnly", lambda: boolErrorsOnly) :
    _l_(350111)

    mfile = "NewPayrollExports\Admin_ErrorsOnly_" + _n_(350105, "m0weekbeg", lambda: m0weekbeg) + "_" + _n_(350106, "m0weekend", lambda: m0weekend) + ".csv"
    _l_(350107)
else:
    mfile = "NewPayrollExports\\Admin_" + _n_(350108, "m0weekbeg", lambda: m0weekbeg) + "_" + _n_(350109, "m0weekend", lambda: m0weekend)+".csv"
    _l_(350110)

#Copy the field list to csv file
with _c_(350114, _n_(350112, "open", lambda: open), _n_(350113, "mfile", lambda: mfile),'r+', newline='') as mhvupload_csv:
    _l_(350125)

    writer = _c_(350118, _a_(350116, _n_(350115, "csv", lambda: csv), "writer"), _n_(350117, "mhvupload_csv", lambda: mhvupload_csv))
    _l_(350119)
    _c_(350123, _a_(350121, _n_(350120, "writer", lambda: writer), "writerow"), _n_(350122, "strFieldList", lambda: strFieldList))
    _l_(350124)