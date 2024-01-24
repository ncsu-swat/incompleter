# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63502624/i-have-a-query-while-executing-the-below-code-im-getting-type-error-int-obje
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
probs = [0.315, 0.226, 0.289, 0.087, 0.083]
_l_(374637)
paper = [533, 486, 386, 234, 263]
_l_(374638)
demand_paper2= 0
_l_(374639)
for probs, paper in _c_(374643, _n_(374640, "zip", lambda: zip), _n_(374641, "probs", lambda: probs), _n_(374642, "paper", lambda: paper)):
    _l_(374648)

    demand_paper2 = _n_(374644, "demand_paper2", lambda: demand_paper2) + _n_(374645, "probs", lambda: probs) * _n_(374646, "paper", lambda: paper)    
    _l_(374647)    
_c_(374653, _n_(374649, "print", lambda: print), 'Expected demand: ' + _c_(374652, _n_(374650, "str", lambda: str), _n_(374651, "demand_paper2", lambda: demand_paper2)))    
_l_(374654)    
var1 = _c_(374663, _n_(374655, "sum", lambda: sum), [_n_(374656, "prob", lambda: prob) * (_n_(374657, "d", lambda: d)- _n_(374658, "demand_paper2", lambda: demand_paper2))**2 
         for prob, d in _c_(374662, _n_(374659, "zip", lambda: zip), _n_(374660, "probs", lambda: probs), _n_(374661, "demand_paper2", lambda: demand_paper2))])
_l_(374664)
std1 = _n_(374665, "var1", lambda: var1) ** 0.5                                  
_l_(374666)                                  
_c_(374671, _n_(374667, "print", lambda: print), _c_(374670, _a_(374668, 'The standard deviation of demand: {0:0.3f}', "format"), _n_(374669, "std1", lambda: std1)))
_l_(374672)