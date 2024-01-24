# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65641396/how-to-solve-the-python-error-nameerror-name-x-is-not-defined
#!/bin/python3 
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def clear_line():
    _l_(367806)

    _c_(367804, _n_(367803, "print", lambda: print), "\n")
    _l_(367805)

def id_check(id,gender):
    _l_(367839)

                    
    id = _c_(367808, _n_(367807, "input", lambda: input), " Do you have an id? : ")    
    _l_(367809)    


    if (_n_(367810, "id", lambda: id) == "yes" ) or (_n_(367811, "id", lambda: id) == "Yes") or (_n_(367812, "id", lambda: id) == "y"):
        _l_(367831)

        
        id = True   
        _l_(367813)   
    
    elif (_n_(367814, "id", lambda: id) == "no" ) or (_n_(367815, "id", lambda: id) == "No") or (_n_(367816, "id", lambda: id) == "n"):
        _l_(367830)

        
        _c_(367818, _n_(367817, "print", lambda: print), "I need your id")
        _l_(367819)
    else:
        _c_(367821, _n_(367820, "print", lambda: print), "Please respound with yes or no "), 
        _l_(367822) 
        _c_(367824, _n_(367823, "clear_line", lambda: clear_line))
        _l_(367825)
        _c_(367828, _n_(367826, "id_check", lambda: id_check), _n_(367827, "id", lambda: id))
        _l_(367829)

    gender = _c_(367833, _n_(367832, "input", lambda: input), " What is you gender ? ")
    _l_(367834)
    _c_(367837, _n_(367835, "print", lambda: print), _n_(367836, "gender", lambda: gender))
    _l_(367838)

_c_(367843, _n_(367840, "id_check", lambda: id_check), _n_(367841, "id", lambda: id),_n_(367842, "gender", lambda: gender)) 
_l_(367844) 