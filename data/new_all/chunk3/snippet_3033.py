# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52701261/qiskit-nameerror-name-q0-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from qiskit import*
    _l_(550867)

except ImportError:
    pass
try:
    from qiskit.tools.visualization import*
    _l_(550869)

except ImportError:
    pass

list = [_n_(550870, "q0", lambda: q0),_n_(550871, "q1", lambda: q1),_n_(550872, "q2", lambda: q2)]
_l_(550873)
def ccz(qci,q0,q1,q2):
    _l_(550891)

    _c_(550877, _a_(550875, _n_(550874, "qci", lambda: qci), "h"), _n_(550876, "q2", lambda: q2))
    _l_(550878)
    _c_(550884, _a_(550880, _n_(550879, "qci", lambda: qci), "ccx"), _n_(550881, "q0", lambda: q0),_n_(550882, "q1", lambda: q1),_n_(550883, "q2", lambda: q2))
    _l_(550885)
    _c_(550889, _a_(550887, _n_(550886, "qci", lambda: qci), "h"), _n_(550888, "q2", lambda: q2))
    _l_(550890)
def grover(qci,q0,q1,q2):
    _l_(550934)

    _c_(550897, _n_(550892, "ccz", lambda: ccz), _n_(550893, "qci", lambda: qci),_n_(550894, "q0", lambda: q0),_n_(550895, "q1", lambda: q1),_n_(550896, "q2", lambda: q2))
    _l_(550898)
    for i in _c_(550901, _n_(550899, "range", lambda: range), _n_(550900, "list", lambda: list)):
        _l_(550912)

        _c_(550905, _a_(550903, _n_(550902, "qci", lambda: qci), "h"), _n_(550904, "i", lambda: i))
        _l_(550906)
        _c_(550910, _a_(550908, _n_(550907, "qci", lambda: qci), "x"), _n_(550909, "i", lambda: i))
        _l_(550911)
    _c_(550918, _n_(550913, "ccz", lambda: ccz), _n_(550914, "qci", lambda: qci),_n_(550915, "q0", lambda: q0),_n_(550916, "q1", lambda: q1),_n_(550917, "q2", lambda: q2))
    _l_(550919)
    for i in _c_(550922, _n_(550920, "range", lambda: range), _n_(550921, "list", lambda: list)):
        _l_(550933)

        _c_(550926, _a_(550924, _n_(550923, "qci", lambda: qci), "x"), _n_(550925, "i", lambda: i))
        _l_(550927)
        _c_(550931, _a_(550929, _n_(550928, "qci", lambda: qci), "h"), _n_(550930, "i", lambda: i))
        _l_(550932)

bn = 3
_l_(550935)
q = _c_(550938, _n_(550936, "QuantumRegister", lambda: QuantumRegister), _n_(550937, "bn", lambda: bn))
_l_(550939)
c = _c_(550942, _n_(550940, "ClassicalRegister", lambda: ClassicalRegister), _n_(550941, "bn", lambda: bn))
_l_(550943)
qc = _c_(550947, _n_(550944, "QuantumCircuit", lambda: QuantumCircuit), _n_(550945, "q", lambda: q),_n_(550946, "c", lambda: c))
_l_(550948)
for i in _c_(550951, _n_(550949, "range", lambda: range), _n_(550950, "bn", lambda: bn)):
    _l_(550958)

    _c_(550956, _a_(550953, _n_(550952, "qc", lambda: qc), "h"), _n_(550954, "q", lambda: q)[_n_(550955, "i", lambda: i)])
    _l_(550957)
_c_(550964, _n_(550959, "grover", lambda: grover), _n_(550960, "qc", lambda: qc),_n_(550961, "q", lambda: q)[0],_n_(550962, "q", lambda: q)[1],_n_(550963, "q", lambda: q)[2])
_l_(550965)
for i in _c_(550968, _n_(550966, "range", lambda: range), _n_(550967, "bn", lambda: bn)):
    _l_(550978)

    _c_(550976, _a_(550970, _n_(550969, "qc", lambda: qc), "measure"), _n_(550971, "q", lambda: q)[_n_(550972, "bn", lambda: bn)-_n_(550973, "i", lambda: i)-1],_n_(550974, "c", lambda: c)[_n_(550975, "i", lambda: i)])
    _l_(550977)
r = _c_(550983, _a_(550982, _c_(550981, _n_(550979, "execute", lambda: execute), _n_(550980, "qc", lambda: qc),"local_qasm_simulator"), "result"))
_l_(550984)
rc = _c_(550987, _a_(550986, _n_(550985, "r", lambda: r), "get_counts"))
_l_(550988)
_c_(550991, _n_(550989, "print", lambda: print), _n_(550990, "rc", lambda: rc))
_l_(550992)
_c_(550995, _n_(550993, "plot_histogram", lambda: plot_histogram), _n_(550994, "rc", lambda: rc)) 
_l_(550996) 