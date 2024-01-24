# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58987855/im-seeing-typeerror-tuple-object-does-not-support-item-assignment-on-spyde
#import libraries
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(468201)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(468203)

except ImportError:
    pass

def dydt(t,y):
    _l_(468209)

    dfdt = _n_(468204, "y", lambda: y) / ((_n_(468205, "t", lambda: t) + 1) ** 2)
    _l_(468206)
    aux = _n_(468207, "dfdt", lambda: dfdt)
    _l_(468208)
    return aux

def IVPsolver2(dydt_fun, y0, t0, t1, t2, tf, h):
    _l_(468301)

    n = 50 #points
    _l_(468210) #points
    h = (_n_(468211, "tf", lambda: tf)-_n_(468212, "t0", lambda: t0))/(_n_(468213, "n", lambda: n)-1) #step size
    _l_(468214) #step size
    t = _c_(468222, _a_(468216, _n_(468215, "np", lambda: np), "linspace"), _n_(468217, "t0", lambda: t0),_n_(468218, "t1", lambda: t1),_n_(468219, "t2", lambda: t2),_n_(468220, "tf", lambda: tf),_n_(468221, "n", lambda: n))
    _l_(468223)
    y = _c_(468227, _a_(468225, _n_(468224, "np", lambda: np), "zeros"), _n_(468226, "n", lambda: n)) #preallocate zeros
    _l_(468228) #preallocate zeros
    yp = _c_(468232, _a_(468230, _n_(468229, "np", lambda: np), "zeros"), _n_(468231, "n", lambda: n))
    _l_(468233)
    m = _c_(468237, _a_(468235, _n_(468234, "np", lambda: np), "zeros"), _n_(468236, "n", lambda: n))
    _l_(468238)
    mc = _c_(468242, _a_(468240, _n_(468239, "np", lambda: np), "zeros"), _n_(468241, "n", lambda: n))
    _l_(468243)
    _n_(468244, "yp", lambda: yp)[0] = _n_(468245, "y0", lambda: y0) #first yp at y0
    _l_(468246) #first yp at y0
    _n_(468247, "y", lambda: y)[0] = _n_(468248, "y0", lambda: y0) #y is 0
    _l_(468249) #y is 0
    _n_(468250, "t", lambda: t)[0] = 0 #t is 0
    _l_(468251) #t is 0
    for i in _c_(468254, _n_(468252, "range", lambda: range), 0,_n_(468253, "n", lambda: n)-1):
        _l_(468297)

        _n_(468255, "m", lambda: m)[_n_(468256, "i", lambda: i)] = _c_(468262, _n_(468257, "dydt_fun", lambda: dydt_fun), _n_(468258, "t", lambda: t)[_n_(468259, "i", lambda: i)-1],_n_(468260, "y", lambda: y)[_n_(468261, "i", lambda: i)-1]) #calculating slope
        _l_(468263) #calculating slope
        _n_(468264, "yp", lambda: yp)[_n_(468265, "i", lambda: i)] = _n_(468266, "y", lambda: y)[_n_(468267, "i", lambda: i)] + _n_(468268, "m", lambda: m)[_n_(468269, "i", lambda: i)]*_n_(468270, "h", lambda: h) #calculating predicted y at slope y
        _l_(468271) #calculating predicted y at slope y
        _n_(468272, "mc", lambda: mc)[_n_(468273, "i", lambda: i)] = _c_(468279, _n_(468274, "dydt_fun", lambda: dydt_fun), _n_(468275, "t", lambda: t)[_n_(468276, "i", lambda: i)+1],_n_(468277, "yp", lambda: yp)[_n_(468278, "i", lambda: i)]) #slope corrector, 2 step
        _l_(468280) #slope corrector, 2 step
        _n_(468281, "t", lambda: t)[_n_(468282, "i", lambda: i)+1] = _n_(468283, "t", lambda: t)[_n_(468284, "i", lambda: i)] + _n_(468285, "h", lambda: h) #t going by stepsize
        _l_(468286) #t going by stepsize
        _n_(468287, "y", lambda: y)[_n_(468288, "i", lambda: i)+1] = _n_(468289, "y", lambda: y)[_n_(468290, "i", lambda: i)] + ((_n_(468291, "m", lambda: m)[_n_(468292, "i", lambda: i)]+_n_(468293, "mc", lambda: mc)[_n_(468294, "i", lambda: i)])/2)*_n_(468295, "h", lambda: h) #corrected y
        _l_(468296) #corrected y
    aux = _n_(468298, "t", lambda: t), _n_(468299, "y", lambda: y)
    _l_(468300)
    return aux

def main():
    _l_(468313)

    x2, y2 = _c_(468304, _n_(468302, "IVPsolver2", lambda: IVPsolver2), _n_(468303, "dydt", lambda: dydt), 1, 0, 0.2, 0.4, 0.6, 0.2)
    _l_(468305)
    _c_(468310, _a_(468307, _n_(468306, "plt", lambda: plt), "plot"), _n_(468308, "x2", lambda: x2),_n_(468309, "y2", lambda: y2), 'o', mfc = 'purple')
    _l_(468311)
    aux = ""
    _l_(468312)

    return aux
_c_(468315, _n_(468314, "main", lambda: main))
_l_(468316)