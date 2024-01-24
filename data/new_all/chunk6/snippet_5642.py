# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56811628/typeerror-generate-input-missing-1-required-positional-argument-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(372535)

except ImportError:
    pass
try:
    from mph.program import Program
    _l_(372537)

except ImportError:
    pass
try:
    from fuzzbang.alphanumericfuzzer import AlphaNumericFuzzer
    _l_(372539)

except ImportError:
    pass

def generate_input(n):
    _l_(372548)

    """
    Returns an alphanumeric string with a length no greater than n.
    """
    fuzzer = _c_(372542, _n_(372540, "AlphaNumericFuzzer", lambda: AlphaNumericFuzzer), 0, _n_(372541, "n", lambda: n))
    _l_(372543)
    aux = _c_(372546, _a_(372545, _n_(372544, "fuzzer", lambda: fuzzer), "generate"))
    _l_(372547)

    return aux

if _n_(372549, "__name__", lambda: __name__) == '__main__':
    _l_(372619)

    # usage
    if _c_(372553, _n_(372550, "len", lambda: len), _a_(372552, _n_(372551, "sys", lambda: sys), "argv")) != 3:
        _l_(372560)

        _c_(372555, _n_(372554, "print", lambda: print), "usage: python3 fuzztut.py num_cases max_length")
        _l_(372556)
        aux = 1
        _l_(372559)
        exit(aux)

    # command-line arguments    
    num_cases = _c_(372564, _n_(372561, "int", lambda: int), _a_(372563, _n_(372562, "sys", lambda: sys), "argv")[1]) # number of test cases to run
    _l_(372565) # number of test cases to run
    max_length = _c_(372569, _n_(372566, "int", lambda: int), _a_(372568, _n_(372567, "sys", lambda: sys), "argv")[2]) # maximum length of each string
    _l_(372570) # maximum length of each string

    results = [] # list for storing the result of each test
    _l_(372571) # list for storing the result of each test

    # main loop
    for i in _c_(372574, _n_(372572, "range", lambda: range), _n_(372573, "num_cases", lambda: num_cases)):
        _l_(372597)

        input = _c_(372576, _n_(372575, "generate_input", lambda: generate_input)) # generate input string
        _l_(372577) # generate input string
        return_value = _c_(372580, _n_(372578, "run", lambda: run), _n_(372579, "input", lambda: input)) # run name with our input
        _l_(372581) # run name with our input

        # save test results to our global results list
        test_result = {}
        _l_(372582)
        _n_(372583, "test_result", lambda: test_result)["num"] = _n_(372584, "i", lambda: i)
        _l_(372585)
        _n_(372586, "test_result", lambda: test_result)["input"] = _n_(372587, "input", lambda: input)
        _l_(372588)
        _n_(372589, "test_result", lambda: test_result)["output"] = _n_(372590, "return_value", lambda: return_value)
        _l_(372591)
        _c_(372595, _a_(372593, _n_(372592, "results", lambda: results), "append"), _n_(372594, "test_result", lambda: test_result))
        _l_(372596)

    # print summary
    for test in _n_(372598, "results", lambda: results):
        _l_(372618)

        _c_(372603, _n_(372599, "print", lambda: print), _c_(372602, _a_(372600, "Case #{:d}:", "format"), _n_(372601, "test", lambda: test)["num"]))
        _l_(372604)
        _c_(372607, _n_(372605, "print", lambda: print), "    IN: " + _n_(372606, "test", lambda: test)["input"])
        _l_(372608)
        _c_(372613, _n_(372609, "print", lambda: print), _c_(372612, _a_(372610, "    OUT: {:4d}", "format"), _n_(372611, "test", lambda: test)["output"]))
        _l_(372614)
        _c_(372616, _n_(372615, "print", lambda: print), "\n")
        _l_(372617)