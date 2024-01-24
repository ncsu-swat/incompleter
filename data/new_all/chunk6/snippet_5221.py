# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69706223/how-to-solve-this-typeerror-in-lambda-functions
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def even_odd_lambda(list_object):
    _l_(365055)

  
    #odd_ctr = list(filter(lambda x: (x%2 != 0) , list_1))
    #even_ctr = list(filter(lambda x: (x%2 == 0) , list_1))
    
    odd_ctr = _c_(365041, _n_(365034, "len", lambda: len), _c_(365040, _n_(365035, "list", lambda: list), _c_(365039, _n_(365036, "filter", lambda: filter), lambda x: (_n_(365037, "x", lambda: x)%2 != 0) , _n_(365038, "list_object", lambda: list_object))))
    _l_(365042)
    even_ctr = _c_(365050, _n_(365043, "len", lambda: len), _c_(365049, _n_(365044, "list", lambda: list), _c_(365048, _n_(365045, "filter", lambda: filter), lambda x: (_n_(365046, "x", lambda: x)%2 == 0) , _n_(365047, "list_object", lambda: list_object))))
    _l_(365051)
    aux = [_n_(365052, "odd_ctr", lambda: odd_ctr), _n_(365053, "even_ctr", lambda: even_ctr)] 
    _l_(365054) 

    return aux 


if _n_(365056, "__name__", lambda: __name__) == '__main__':
    _l_(365074)

  
    a=_c_(365060, _a_(365059, _c_(365058, _n_(365057, "input", lambda: input), "Add list elements seperated by space "), "split"), ' ')
    _l_(365061)

    
    
    output = _c_(365064, _n_(365062, "even_odd_lambda", lambda: even_odd_lambda), _n_(365063, "a", lambda: a))
    _l_(365065)
    _c_(365068, _n_(365066, "print", lambda: print), "\nNumber of even numbers in the above array: ", _n_(365067, "output", lambda: output)[1])
    _l_(365069)
    _c_(365072, _n_(365070, "print", lambda: print), "\nNumber of odd numbers in the above array: ", _n_(365071, "output", lambda: output)[0])  
    _l_(365073)  