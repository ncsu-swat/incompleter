# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1485841/behaviour-of-increment-and-decrement-operators-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def PreIncrement(name, local={}):
    _l_(1546074)

    #Equivalent to ++name
    if _n_(1546057, "name", lambda: name) in _n_(1546058, "local", lambda: local):
        _l_(1546065)

        _n_(1546059, "local", lambda: local)[_n_(1546060, "name", lambda: name)]+=1
        _l_(1546061)
        aux = _n_(1546062, "local", lambda: local)[_n_(1546063, "name", lambda: name)]
        _l_(1546064)
        return aux
    _c_(1546067, _n_(1546066, "globals", lambda: globals))[_n_(1546068, "name", lambda: name)]+=1
    _l_(1546069)
    aux = _c_(1546071, _n_(1546070, "globals", lambda: globals))[_n_(1546072, "name", lambda: name)]
    _l_(1546073)
    return aux

def PostIncrement(name, local={}):
    _l_(1546092)

    #Equivalent to name++
    if _n_(1546075, "name", lambda: name) in _n_(1546076, "local", lambda: local):
        _l_(1546083)

        _n_(1546077, "local", lambda: local)[_n_(1546078, "name", lambda: name)]+=1
        _l_(1546079)
        aux = _n_(1546080, "local", lambda: local)[_n_(1546081, "name", lambda: name)]-1
        _l_(1546082)
        return aux
    _c_(1546085, _n_(1546084, "globals", lambda: globals))[_n_(1546086, "name", lambda: name)]+=1
    _l_(1546087)
    aux = _c_(1546089, _n_(1546088, "globals", lambda: globals))[_n_(1546090, "name", lambda: name)]-1
    _l_(1546091)
    return aux

x = 1
_l_(1546093)
y = _c_(1546095, _n_(1546094, "PreIncrement", lambda: PreIncrement), 'x') #y and x are both 2
_l_(1546096) #y and x are both 2
a = 1
_l_(1546097)
b = _c_(1546099, _n_(1546098, "PostIncrement", lambda: PostIncrement), 'a') #b is 1 and a is 2
_l_(1546100) #b is 1 and a is 2

x = 1
_l_(1546101)
def test():
    _l_(1546111)

    x = 10
    _l_(1546102)
    y = _c_(1546104, _n_(1546103, "PreIncrement", lambda: PreIncrement), 'x') #y will be 2, local x will be still 10 and global x will be changed to 2
    _l_(1546105) #y will be 2, local x will be still 10 and global x will be changed to 2
    z = _c_(1546109, _n_(1546106, "PreIncrement", lambda: PreIncrement), 'x', _c_(1546108, _n_(1546107, "locals", lambda: locals))) #z will be 11, local x will be 11 and global x will be unaltered
    _l_(1546110) #z will be 11, local x will be 11 and global x will be unaltered
_c_(1546113, _n_(1546112, "test", lambda: test))
_l_(1546114)

x = 1
_l_(1546115)
_c_(1546119, _n_(1546116, "print", lambda: print), _c_(1546118, _n_(1546117, "PreIncrement", lambda: PreIncrement), 'x'))   #print(x+=1) is illegal!
_l_(1546120)   #print(x+=1) is illegal!

x = 1
_l_(1546121)
x+=1
_l_(1546122)
_c_(1546125, _n_(1546123, "print", lambda: print), _n_(1546124, "x", lambda: x))
_l_(1546126)

def PreDecrement(name, local={}):
    _l_(1546144)

    #Equivalent to --name
    if _n_(1546127, "name", lambda: name) in _n_(1546128, "local", lambda: local):
        _l_(1546135)

        _n_(1546129, "local", lambda: local)[_n_(1546130, "name", lambda: name)]-=1
        _l_(1546131)
        aux = _n_(1546132, "local", lambda: local)[_n_(1546133, "name", lambda: name)]
        _l_(1546134)
        return aux
    _c_(1546137, _n_(1546136, "globals", lambda: globals))[_n_(1546138, "name", lambda: name)]-=1
    _l_(1546139)
    aux = _c_(1546141, _n_(1546140, "globals", lambda: globals))[_n_(1546142, "name", lambda: name)]
    _l_(1546143)
    return aux

def PostDecrement(name, local={}):
    _l_(1546162)

    #Equivalent to name--
    if _n_(1546145, "name", lambda: name) in _n_(1546146, "local", lambda: local):
        _l_(1546153)

        _n_(1546147, "local", lambda: local)[_n_(1546148, "name", lambda: name)]-=1
        _l_(1546149)
        aux = _n_(1546150, "local", lambda: local)[_n_(1546151, "name", lambda: name)]+1
        _l_(1546152)
        return aux
    _c_(1546155, _n_(1546154, "globals", lambda: globals))[_n_(1546156, "name", lambda: name)]-=1
    _l_(1546157)
    aux = _c_(1546159, _n_(1546158, "globals", lambda: globals))[_n_(1546160, "name", lambda: name)]+1
    _l_(1546161)
    return aux

