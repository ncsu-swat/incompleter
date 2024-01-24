# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36329269/python-legend-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fig = _c_(382733, _a_(382732, _n_(382731, "plt", lambda: plt), "figure"))
_l_(382734)
ax = _c_(382737, _a_(382736, _n_(382735, "plt", lambda: plt), "gca"))
_l_(382738)
barplt = _c_(382743, _a_(382740, _n_(382739, "plt", lambda: plt), "bar"), _n_(382741, "bins", lambda: bins),_n_(382742, "frq", lambda: frq),align='center',label='Dgr')
_l_(382744)
normplt = _c_(382749, _a_(382746, _n_(382745, "plt", lambda: plt), "plot"), _n_(382747, "bins_n", lambda: bins_n),_n_(382748, "frq_n", lambda: frq_n),'--r', label='Norm');
_l_(382750)
_c_(382759, _a_(382752, _n_(382751, "ax", lambda: ax), "set_xlim"), [_c_(382755, _n_(382753, "min", lambda: min), _n_(382754, "bins", lambda: bins))-1, _c_(382758, _n_(382756, "max", lambda: max), _n_(382757, "bins", lambda: bins))+1])
_l_(382760)
_c_(382766, _a_(382762, _n_(382761, "ax", lambda: ax), "set_ylim"), [0, _c_(382765, _n_(382763, "max", lambda: max), _n_(382764, "frq", lambda: frq))])
_l_(382767)
_c_(382770, _a_(382769, _n_(382768, "plt", lambda: plt), "xlabel"), 'Dgr')
_l_(382771)
_c_(382774, _a_(382773, _n_(382772, "plt", lambda: plt), "ylabel"), 'Frequency')
_l_(382775)
_c_(382778, _a_(382777, _n_(382776, "plt", lambda: plt), "show"))
_l_(382779)
_c_(382784, _a_(382781, _n_(382780, "plt", lambda: plt), "legend"), handles=[_n_(382782, "barplt", lambda: barplt),_n_(382783, "normplt", lambda: normplt)])
_l_(382785)