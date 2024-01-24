# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75026218/python-pytest-mock-the-class-method-typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from python_tools.pytest_samples.load_data import slow_load
    _l_(434768)

except ImportError:
    pass


def test_slow_load():
    _l_(434772)

    assert "Data" in _c_(434770, _n_(434769, "slow_load", lambda: slow_load))
    _l_(434771)


def test_slow_load(mocker):
    _l_(434791)

    assert "Data" in _c_(434774, _n_(434773, "slow_load", lambda: slow_load))
    _l_(434775)

    expected = 'mock load'
    _l_(434776)

    def mock_load():
        _l_(434778)

        aux = 'mock load'
        _l_(434777)
        return aux

    _c_(434783, _a_(434780, _n_(434779, "mocker", lambda: mocker), "patch"), "python_tools.pytest_samples.load_data.DataSet.load_data", _c_(434782, _n_(434781, "mock_load", lambda: mock_load)))
    _l_(434784)
    actual = _c_(434786, _n_(434785, "slow_load", lambda: slow_load))
    _l_(434787)
    assert _n_(434788, "actual", lambda: actual) == _n_(434789, "expected", lambda: expected)
    _l_(434790)