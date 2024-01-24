# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70164872/problems-in-the-use-of-sum-typeerror-int-object-is-not-iterable
#ELEMENT 1
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(617811, _a_(617809, _n_(617808, "cursor", lambda: cursor), "execute"), 'SELECT City FROM Nation WHERE X = ?', [_n_(617810, "X", lambda: X)])
_l_(617812)
count_A = _c_(617815, _a_(617814, _n_(617813, "cursor", lambda: cursor), "fetchall")) #Print [(2,), (1,), (2,)]
_l_(617816) #Print [(2,), (1,), (2,)]

sum_A = _c_(617822, _n_(617817, "sum", lambda: sum), (_c_(617820, _n_(617818, "int", lambda: int), _n_(617819, "row", lambda: row)[0]) for row in _n_(617821, "count_A", lambda: count_A))) #print 5
_l_(617823) #print 5
_c_(617826, _n_(617824, "print", lambda: print), _n_(617825, "sum_A", lambda: sum_A))
_l_(617827)
###########################################

#ELEMENT 2
_c_(617831, _a_(617829, _n_(617828, "cursor", lambda: cursor), "execute"), 'SELECT City FROM Nation WHERE Y = ?', [_n_(617830, "Y", lambda: Y)])
_l_(617832)
count_B = _c_(617835, _a_(617834, _n_(617833, "cursor", lambda: cursor), "fetchall")) #Print [(3,), (2,)]
_l_(617836) #Print [(3,), (2,)]

sum_B = _c_(617842, _n_(617837, "sum", lambda: sum), (_c_(617840, _n_(617838, "int", lambda: int), _n_(617839, "row", lambda: row)[0]) for row in _n_(617841, "count_B", lambda: count_B))) #print 5
_l_(617843) #print 5
_c_(617846, _n_(617844, "print", lambda: print), _n_(617845, "sum_B", lambda: sum_B))
_l_(617847)
###########################################

SumA_B = _c_(617851, _n_(617848, "sum", lambda: sum), _n_(617849, "sum_A", lambda: sum_A), _n_(617850, "sum_B", lambda: sum_B)) 
_l_(617852) 
_c_(617855, _n_(617853, "print", lambda: print), _n_(617854, "SumA_B", lambda: SumA_B)) #ERROR: I would like to get result 10
_l_(617856) #ERROR: I would like to get result 10