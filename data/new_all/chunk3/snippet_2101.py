# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64002683/how-to-fix-typeerror-tuple-indices-must-be-integers-or-slices-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pulp import *
    _l_(532008)

except ImportError:
    pass
FOODS = ['OATMEAL', 'CHICKEN', 'EGGS', 'MILK']
_l_(532009)
CUSTOMERS = [1,2,3,4,5]
_l_(532010)
FACILITY = ['FAC1', 'FAC2', 'FAC3']
_l_(532011)
dem = {1: 80,      
       2: 270,
       3: 250,
       4: 160,
       5: 180}
_l_(532012)
maxam = {'FAC1': 500,
         'FAC2': 500,
         'FAC3': 500}
_l_(532013)
actcost = {'FAC1': 1000,
           'FAC2': 1000,
           'FAC3': 1000}
_l_(532014)
transp = {'FAC1': {1:4, 2:5, 3:6, 4:8, 5:10},  
          'FAC2': {1:6, 2:4, 3:3, 4:5, 5:8},
          'FAC3': {1:9, 2:7, 3:4, 4:3, 5:4}}
_l_(532015)

prob = _c_(532018, _n_(532016, "LpProblem", lambda: LpProblem), "FacilityLocation", _n_(532017, "LpMinimize", lambda: LpMinimize)) 
_l_(532019) 

use_vars = _c_(532024, _a_(532021, _n_(532020, "LpVariable", lambda: LpVariable), "dicts"), "UseLocation",_n_(532022, "FACILITY", lambda: FACILITY),0,1,_n_(532023, "LpBinary", lambda: LpBinary))  
_l_(532025)  
serv_vars = _c_(532032, _a_(532027, _n_(532026, "LpVariable", lambda: LpVariable), "dicts"), "Service", [(_n_(532028, "i", lambda: i),_n_(532029, "j", lambda: j)) for i in _n_(532030, "CUSTOMERS", lambda: CUSTOMERS) 
                                               for j in _n_(532031, "FACILITY", lambda: FACILITY)],0)
_l_(532033)
foods_vars = _c_(532037, _a_(532035, _n_(532034, "LpVariable", lambda: LpVariable), "dicts"), "food", _n_(532036, "FOODS", lambda: FOODS), 0)
_l_(532038)

prob += _c_(532045, _n_(532039, "lpSum", lambda: lpSum), (_n_(532040, "actcost", lambda: actcost)[_n_(532041, "j", lambda: j)]*_n_(532042, "use_vars", lambda: use_vars)[_n_(532043, "j", lambda: j)] for j in _n_(532044, "FACILITY", lambda: FACILITY))) + _c_(532055, _n_(532046, "lpSum", lambda: lpSum), (_n_(532047, "transp", lambda: transp)[_n_(532048, "j", lambda: j)][_n_(532049, "i", lambda: i)]*_n_(532050, "serv_vars", lambda: serv_vars)[(_n_(532051, "i", lambda: i),_n_(532052, "j", lambda: j))] for j in _n_(532053, "FACILITY", lambda: FACILITY) for i in _n_(532054, "CUSTOMERS", lambda: CUSTOMERS)))
_l_(532056)