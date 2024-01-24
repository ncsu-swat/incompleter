# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52342233/python-3-x-python-exec-function-throws-typeerror-for-no-reason
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def parse(input_var):
    _l_(449001)

    input_var = _c_(448976, _a_(448975, _n_(448974, "input_var", lambda: input_var), "split"), "[METHOD]")
    _l_(448977)
    if(_c_(448980, _n_(448978, "len", lambda: len), _n_(448979, "input_var", lambda: input_var))>1):
        _l_(448996)

        _n_(448981, "input_var", lambda: input_var)[0] = _c_(448984, _a_(448983, _n_(448982, "input_var", lambda: input_var)[0], "replace"), "using ","exec(parse(")
        _l_(448985)
        _n_(448986, "input_var", lambda: input_var)[0] = _c_(448989, _a_(448988, _n_(448987, "input_var", lambda: input_var)[0], "replace"), ";","))")
        _l_(448990)
        input_var = _n_(448991, "input_var", lambda: input_var)[0]+_n_(448992, "input_var", lambda: input_var)[1]
        _l_(448993)
    else:
        input_var=_n_(448994, "input_var", lambda: input_var)[0]
        _l_(448995)
    _c_(448999, _n_(448997, "exec", lambda: exec), _n_(448998, "input_var", lambda: input_var))
    _l_(449000)


foo="""
using bar;
[METHOD]
print('Passed foo!')
"""
_l_(449002)

bar = """
print('Passed bar!')
"""
_l_(449003)

_c_(449006, _n_(449004, "parse", lambda: parse), _n_(449005, "foo", lambda: foo))
_l_(449007)