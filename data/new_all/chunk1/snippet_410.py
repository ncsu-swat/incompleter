# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64584856/python-exec-with-a-function-chain-producing-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def run_code():
  _l_(388282)

  code = """
def foo():
  print('foo')
  return 1

def bar():
  print('bar calls foo')
  return 1 + foo()

result = bar()
"""
  _l_(388266)

  _c_(388273, _n_(388267, "exec", lambda: exec), _n_(388268, "code", lambda: code), _c_(388270, _n_(388269, "globals", lambda: globals)), _c_(388272, _n_(388271, "locals", lambda: locals)))
  _l_(388274)
  _c_(388280, _n_(388275, "print", lambda: print), _c_(388279, _a_(388276, 'Result: {}', "format"), _c_(388278, _n_(388277, "locals", lambda: locals))['result']))
  _l_(388281)

_c_(388284, _n_(388283, "run_code", lambda: run_code))
_l_(388285)