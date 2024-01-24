# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42980584/attribute-error-when-using-firls-method-of-scipy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scipy.signal as signal
    _l_(565419)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(565421)

except ImportError:
    pass
fig, axs = _c_(565424, _a_(565423, _n_(565422, "plt", lambda: plt), "subplots"), 2)
_l_(565425)
nyq = 5.  # Hz
_l_(565426)  # Hz
desired = (0, 0, 1, 1, 0, 0)
_l_(565427)
for bi, bands in _c_(565429, _n_(565428, "enumerate", lambda: enumerate), ((0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 4.5, 5))):
    _l_(565521)

    fir_firls = _c_(565435, _a_(565431, _n_(565430, "signal", lambda: signal), "firls"), 73, _n_(565432, "bands", lambda: bands), _n_(565433, "desired", lambda: desired), nyq=_n_(565434, "nyq", lambda: nyq))
    _l_(565436)
    fir_remez = _c_(565442, _a_(565438, _n_(565437, "signal", lambda: signal), "remez"), 73, _n_(565439, "bands", lambda: bands), _n_(565440, "desired", lambda: desired)[::2], Hz=2 * _n_(565441, "nyq", lambda: nyq))
    _l_(565443)
    fir_firwin2 = _c_(565449, _a_(565445, _n_(565444, "signal", lambda: signal), "firwin2"), 73, _n_(565446, "bands", lambda: bands), _n_(565447, "desired", lambda: desired), nyq=_n_(565448, "nyq", lambda: nyq))
    _l_(565450)
    hs = _c_(565452, _n_(565451, "list", lambda: list))
    _l_(565453)
    ax = _n_(565454, "axs", lambda: axs)[_n_(565455, "bi", lambda: bi)]
    _l_(565456)
    for fir in (_n_(565457, "fir_firls", lambda: fir_firls), _n_(565458, "fir_remez", lambda: fir_remez), _n_(565459, "fir_firwin2", lambda: fir_firwin2)):
        _l_(565480)

        freq, response = _c_(565463, _a_(565461, _n_(565460, "signal", lambda: signal), "freqz"), _n_(565462, "fir", lambda: fir))
        _l_(565464)
        _c_(565478, _a_(565466, _n_(565465, "hs", lambda: hs), "append"), _c_(565477, _a_(565468, _n_(565467, "ax", lambda: ax), "semilogy"), _n_(565469, "nyq", lambda: nyq)*_n_(565470, "freq", lambda: freq)/_a_(565472, _n_(565471, "np", lambda: np), "pi"), _c_(565476, _a_(565474, _n_(565473, "np", lambda: np), "abs"), _n_(565475, "response", lambda: response)))[0])
        _l_(565479)
    for band, gains in _c_(565490, _n_(565481, "zip", lambda: zip), _c_(565485, _n_(565482, "zip", lambda: zip), _n_(565483, "bands", lambda: bands)[::2], _n_(565484, "bands", lambda: bands)[1::2]), _c_(565489, _n_(565486, "zip", lambda: zip), _n_(565487, "desired", lambda: desired)[::2],      _n_(565488, "desired", lambda: desired)[1::2])):
        _l_(565500)

        _c_(565498, _a_(565492, _n_(565491, "ax", lambda: ax), "semilogy"), _n_(565493, "band", lambda: band), _c_(565497, _a_(565495, _n_(565494, "np", lambda: np), "maximum"), _n_(565496, "gains", lambda: gains), 1e-7), 'k--', linewidth=2)
        _l_(565499)
    if _n_(565501, "bi", lambda: bi) == 0:
        _l_(565511)

        _c_(565505, _a_(565503, _n_(565502, "ax", lambda: ax), "legend"), _n_(565504, "hs", lambda: hs), ('firls', 'remez', 'firwin2'), loc='lower center',    frameon=False)
        _l_(565506)
    else:
        _c_(565509, _a_(565508, _n_(565507, "ax", lambda: ax), "set_xlabel"), 'Frequency (Hz)')
        _l_(565510)
    _c_(565514, _a_(565513, _n_(565512, "ax", lambda: ax), "grid"), True)
    _l_(565515)
    _c_(565519, _a_(565517, _n_(565516, "ax", lambda: ax), "set"), title='Band-pass %d-%d Hz' % _n_(565518, "bands", lambda: bands)[2:4], ylabel='Magnitude')
    _l_(565520)
_c_(565524, _a_(565523, _n_(565522, "fig", lambda: fig), "tight_layout"))
_l_(565525)
_c_(565528, _a_(565527, _n_(565526, "plt", lambda: plt), "show"))
_l_(565529)