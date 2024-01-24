# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72319342/attributeerror-module-cirq-has-no-attribute-gridqubit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cirq
    _l_(455519)

except ImportError:
    pass

# Pick a qubit.
qubit = _c_(455522, _a_(455521, _n_(455520, "cirq", lambda: cirq), "GridQubit"), 0, 0)
_l_(455523)

# Create a circuit
circuit = _c_(455534, _a_(455525, _n_(455524, "cirq", lambda: cirq), "Circuit"), _c_(455529, _a_(455527, _n_(455526, "cirq", lambda: cirq), "X"), _n_(455528, "qubit", lambda: qubit))**0.5,  # Square root of NOT.
    _c_(455533, _a_(455531, _n_(455530, "cirq", lambda: cirq), "measure"), _n_(455532, "qubit", lambda: qubit), key='m')  # Measurement.
)
_l_(455535)
_c_(455537, _n_(455536, "print", lambda: print), "Circuit:")
_l_(455538)
_c_(455541, _n_(455539, "print", lambda: print), _n_(455540, "circuit", lambda: circuit))
_l_(455542)

# Simulate the circuit several times.
simulator = _c_(455545, _a_(455544, _n_(455543, "cirq", lambda: cirq), "Simulator"))
_l_(455546)
result = _c_(455550, _a_(455548, _n_(455547, "simulator", lambda: simulator), "run"), _n_(455549, "circuit", lambda: circuit), repetitions=20)
_l_(455551)
_c_(455553, _n_(455552, "print", lambda: print), "Results:")
_l_(455554)
_c_(455557, _n_(455555, "print", lambda: print), _n_(455556, "result", lambda: result))
_l_(455558)