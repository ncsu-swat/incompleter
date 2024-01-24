# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75507313/try-exception-typeerror-not-loading-properly
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
entrada=_c_(623189, _n_(623188, "input", lambda: input), "escribe un valor para calcular su raiz: ")
_l_(623190)
raiz_cuadrada=_n_(623191, "entrada", lambda: entrada) ** 0.5
_l_(623192)
try:
    _l_(623211)

    if _n_(623193, "entrada", lambda: entrada)>=0:
        _l_(623203)

        _c_(623196, _n_(623194, "print", lambda: print), _n_(623195, "raiz_cuadrada", lambda: raiz_cuadrada))
        _l_(623197)
    else:
        _c_(623199, _n_(623198, "print", lambda: print), "no se puede calcular la raiz cuadrada de un numero negativo")
        _l_(623200)
        raise _n_(623201, "ValueError", lambda: ValueError)
        _l_(623202)
except _n_(623204, "TypeError", lambda: TypeError):
    _l_(623210)

    #This print below should be showed always as the input is a string always I think
    _c_(623206, _n_(623205, "print", lambda: print), "el valor proporcionado no es un número")
    _l_(623207)
    raise _n_(623208, "TypeError", lambda: TypeError)
    _l_(623209)