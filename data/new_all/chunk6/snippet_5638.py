# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56811628/typeerror-generate-input-missing-1-required-positional-argument-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(358452)

except ImportError:
    pass
try:
    from mph.program import Program
    _l_(358454)

except ImportError:
    pass
try:
    from fuzzbang.alphanumericfuzzer import AlphaNumericFuzzer
    _l_(358456)

except ImportError:
    pass

def generate_input(n):
    _l_(358465)

    """
    Returns an alphanumeric string with a length no greater than n.
    """
    fuzzer = _c_(358459, _n_(358457, "AlphaNumericFuzzer", lambda: AlphaNumericFuzzer), 0, _n_(358458, "n", lambda: n))
    _l_(358460)
    aux = _c_(358463, _a_(358462, _n_(358461, "fuzzer", lambda: fuzzer), "generate"))
    _l_(358464)

    return aux

if _n_(358466, "__name__", lambda: __name__) == '__main__':
    _l_(358536)

    # usage
    if _c_(358470, _n_(358467, "len", lambda: len), _a_(358469, _n_(358468, "sys", lambda: sys), "argv")) != 3:
        _l_(358477)

        _c_(358472, _n_(358471, "print", lambda: print), "usage: python3 fuzztut.py num_cases max_length")
        _l_(358473)
        aux = 1
        _l_(358476)
        exit(aux)

    # command-line arguments    
    num_cases = _c_(358481, _n_(358478, "int", lambda: int), _a_(358480, _n_(358479, "sys", lambda: sys), "argv")[1]) # number of test cases to run
    _l_(358482) # number of test cases to run
    max_length = _c_(358486, _n_(358483, "int", lambda: int), _a_(358485, _n_(358484, "sys", lambda: sys), "argv")[2]) # maximum length of each string
    _l_(358487) # maximum length of each string

    results = [] # list for storing the result of each test
    _l_(358488) # list for storing the result of each test

    # main loop
    for i in _c_(358491, _n_(358489, "range", lambda: range), _n_(358490, "num_cases", lambda: num_cases)):
        _l_(358514)

        input = _c_(358493, _n_(358492, "generate_input", lambda: generate_input)) # generate input string
        _l_(358494) # generate input string
        return_value = _c_(358497, _n_(358495, "run", lambda: run), _n_(358496, "input", lambda: input)) # run name with our input
        _l_(358498) # run name with our input

        # save test results to our global results list
        test_result = {}
        _l_(358499)
        _n_(358500, "test_result", lambda: test_result)["num"] = _n_(358501, "i", lambda: i)
        _l_(358502)
        _n_(358503, "test_result", lambda: test_result)["input"] = _n_(358504, "input", lambda: input)
        _l_(358505)
        _n_(358506, "test_result", lambda: test_result)["output"] = _n_(358507, "return_value", lambda: return_value)
        _l_(358508)
        _c_(358512, _a_(358510, _n_(358509, "results", lambda: results), "append"), _n_(358511, "test_result", lambda: test_result))
        _l_(358513)

    # print summary
    for test in _n_(358515, "results", lambda: results):
        _l_(358535)

        _c_(358520, _n_(358516, "print", lambda: print), _c_(358519, _a_(358517, "Case #{:d}:", "format"), _n_(358518, "test", lambda: test)["num"]))
        _l_(358521)
        _c_(358524, _n_(358522, "print", lambda: print), "    IN: " + _n_(358523, "test", lambda: test)["input"])
        _l_(358525)
        _c_(358530, _n_(358526, "print", lambda: print), _c_(358529, _a_(358527, "    OUT: {:4d}", "format"), _n_(358528, "test", lambda: test)["output"]))
        _l_(358531)
        _c_(358533, _n_(358532, "print", lambda: print), "\n")
        _l_(358534)