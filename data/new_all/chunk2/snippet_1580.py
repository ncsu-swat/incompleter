# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75026218/python-pytest-mock-the-class-method-typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from python_tools.pytest_samples.slow import DataSet
    _l_(422557)

except ImportError:
    pass


def slow_load():
    _l_(422565)

    dataset = _c_(422559, _n_(422558, "DataSet", lambda: DataSet))
    _l_(422560)
    aux = _c_(422563, _a_(422562, _n_(422561, "dataset", lambda: dataset), "load_data"))
    _l_(422564)
    return aux