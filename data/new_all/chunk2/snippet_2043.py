# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67249213/why-is-ipython-returning-nameerror-while-decorating-interact
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(475783, "interact", lambda: interact)
def show_crank(angle = _c_(475788, _n_(475784, "slider", lambda: slider), 0,2*_n_(475785, "pi", lambda: pi),_n_(475786, "pi", lambda: pi)/20,_n_(475787, "pi", lambda: pi)/10,label='angle')):
    _l_(475816)

    center = (0,0)
    _l_(475789)
    endpnt = (_c_(475792, _n_(475790, "cos", lambda: cos), _n_(475791, "angle", lambda: angle)),_c_(475795, _n_(475793, "sin", lambda: sin), _n_(475794, "angle", lambda: angle)))
    _l_(475796)
    pltcnt = _c_(475799, _n_(475797, "point", lambda: point), _n_(475798, "center", lambda: center), size = 50)
    _l_(475800)
    pltend = _c_(475803, _n_(475801, "point", lambda: point), _n_(475802, "endpnt", lambda: endpnt), size = 50)
    _l_(475804)
    crank = _c_(475808, _n_(475805, "line", lambda: line), [_n_(475806, "center", lambda: center),_n_(475807, "endpnt", lambda: endpnt)])
    _l_(475809)
    _c_(475814, _a_(475813, (_n_(475810, "pltcnt", lambda: pltcnt) + _n_(475811, "crank", lambda: crank) + _n_(475812, "pltend", lambda: pltend)), "show"), xmin=-1,xmax=1,ymin=-1,ymax=1)
    _l_(475815)