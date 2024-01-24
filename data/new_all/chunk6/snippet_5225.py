# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55288202/adding-uuid-type-to-cerberus-leads-to-bad-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(362014, _a_(362013, _n_(362012, "pytest", lambda: pytest), "mark"), "unit")
def test_valid_uuid():
    _l_(362024)

    test_input = "35d6d5a0-6f37-4794-a493-2712eda41c1a"
    _l_(362015)
    actual = _c_(362018, _n_(362016, "UUID", lambda: UUID), _n_(362017, "test_input", lambda: test_input))
    _l_(362019)
    assert _c_(362022, _n_(362020, "str", lambda: str), _n_(362021, "actual", lambda: actual)) == "35d6d5a0-6f37-4794-a493-2712eda41c1a"
    _l_(362023)

@_a_(362027, _a_(362026, _n_(362025, "pytest", lambda: pytest), "mark"), "unit")
def test_invalid_uuid():
    _l_(362038)

    test_input = "Not a Valid UUID"
    _l_(362028)
    with _c_(362032, _a_(362030, _n_(362029, "pytest", lambda: pytest), "raises"), _n_(362031, "ValueError", lambda: ValueError)):
        _l_(362037)

        actual = _c_(362035, _n_(362033, "UUID", lambda: UUID), _n_(362034, "test_input", lambda: test_input)) 
        _l_(362036) 

@_a_(362041, _a_(362040, _n_(362039, "pytest", lambda: pytest), "mark"), "unit")
def test_uuid_type_registration():
    _l_(362060)

    test_schema = {"test_name": {"type": "UUID"}}
    _l_(362042)
    validator = _c_(362045, _n_(362043, "Validator", lambda: Validator), _n_(362044, "test_schema", lambda: test_schema))
    _l_(362046)
    test_record = {"test_name": "35d6d5a0-6f37-4794-a493-2712eda41c1a"}
    _l_(362047)
    result = _c_(362051, _a_(362049, _n_(362048, "validator", lambda: validator), "validate"), _n_(362050, "test_record", lambda: test_record))
    _l_(362052)
    _c_(362056, _n_(362053, "print", lambda: print), _a_(362055, _n_(362054, "validator", lambda: validator), "_errors"))
    _l_(362057)
    assert _n_(362058, "result", lambda: result) == True
    _l_(362059)