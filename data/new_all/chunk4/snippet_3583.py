# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71909085/attributeerror-nonetype-object-has-no-attribute-find-in-python-collatz-con
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import random
  _l_(646036)

except ImportError:
  pass

x = None
_l_(646037)
y = None
_l_(646038)
nru = None
_l_(646039)
nra = None
_l_(646040)
history = None
_l_(646041)
z = None
_l_(646042)
s = None
_l_(646043)
text1 = None
_l_(646044)
text2 = None
_l_(646045)
inpt = None
_l_(646046)

# Describe this function...
def func1():
  _l_(646058)

  global x, y, nru, nra, history, z, s, text1, text2
  _l_(646047)
  x = _c_(646050, _a_(646049, _n_(646048, "random", lambda: random), "randint"), 1, 100)
  _l_(646051)
  nru = _n_(646052, "x", lambda: x)
  _l_(646053)
  z = 2
  _l_(646054)
  _c_(646056, _n_(646055, "func4", lambda: func4))
  _l_(646057)

# Describe this function...
def func2():
  _l_(646069)

  global x, y, nru, nra, history, z, s, text1, text2
  _l_(646059)
  if _n_(646060, "x", lambda: x) % 2 == 0:
    _l_(646065)

    x = _n_(646061, "x", lambda: x) / 2
    _l_(646062)
  else:
    x = _n_(646063, "x", lambda: x) * 3 + 1
    _l_(646064)
  _c_(646067, _n_(646066, "func3", lambda: func3))
  _l_(646068)

# Describe this function...
def func3():
  _l_(646092)

  global x, y, nru, nra, history, z, s, text1, text2
  _l_(646070)
  if _n_(646071, "x", lambda: x) == 1:
    _l_(646091)

    nra = _n_(646072, "nra", lambda: nra) + 1
    _l_(646073)
    _c_(646075, _n_(646074, "func1", lambda: func1))
    _l_(646076)
  else:
    if not _c_(646080, _a_(646078, _n_(646077, "history", lambda: history), "find"), _n_(646079, "y", lambda: y))+ 1 == 0:
      _l_(646090)

      z = 3
      _l_(646081)
      s = 'pending successful'
      _l_(646082)
      _c_(646084, _n_(646083, "func4", lambda: func4))
      _l_(646085)
    else:
      z = 1
      _l_(646086)
      _c_(646088, _n_(646087, "func4", lambda: func4))
      _l_(646089)

# Describe this function...
def func4():
  _l_(646145)

  global x, y, nru, nra, history, z, s, text1, text2
  _l_(646093)
  if _n_(646094, "z", lambda: z) == 1:
    _l_(646144)

    history = _c_(646101, _a_(646095, '', "join"), [_c_(646098, _n_(646096, "str", lambda: str), _n_(646097, "x2", lambda: x2)) for x2 in [_n_(646099, "history", lambda: history), "'", _n_(646100, "x", lambda: x), "'"]])
    _l_(646102)
    _c_(646104, _n_(646103, "func2", lambda: func2))
    _l_(646105)
  elif _n_(646106, "z", lambda: z) == 2:
    _l_(646143)

    _c_(646118, _n_(646107, "print", lambda: print), _c_(646117, _a_(646108, '', "join"), [_c_(646111, _n_(646109, "str", lambda: str), _n_(646110, "x3", lambda: x3)) for x3 in [_n_(646112, "text1", lambda: text1), _n_(646113, "nru", lambda: nru), _n_(646114, "text2", lambda: text2), _n_(646115, "nra", lambda: nra), _n_(646116, "s", lambda: s)]]))
    _l_(646119)
    _c_(646121, _n_(646120, "func2", lambda: func2))
    _l_(646122)
  elif _n_(646123, "z", lambda: z) == 3:
    _l_(646142)

    nra = _n_(646124, "nra", lambda: nra) + 1
    _l_(646125)
    _c_(646137, _n_(646126, "print", lambda: print), _c_(646136, _a_(646127, '', "join"), [_c_(646130, _n_(646128, "str", lambda: str), _n_(646129, "x4", lambda: x4)) for x4 in [_n_(646131, "text1", lambda: text1), _n_(646132, "nru", lambda: nru), _n_(646133, "text2", lambda: text2), _n_(646134, "nra", lambda: nra), _n_(646135, "s", lambda: s)]]))
    _l_(646138)
    _c_(646140, _n_(646139, "func5", lambda: func5))
    _l_(646141)


# Describe this function...
def func5():
  _l_(646165)

  global x, y, nru, nra, history, z, s, text1, text2
  _l_(646146)
  _c_(646149, _n_(646147, "print", lambda: print), _n_(646148, "history", lambda: history))
  _l_(646150)
  inpt = _c_(646152, _n_(646151, "input", lambda: input), "flaw? y/n")
  _l_(646153)
  if _n_(646154, "inpt", lambda: inpt) == 'y':
    _l_(646164)

    s = 'pending'
    _l_(646155)
    nra = _n_(646156, "nra", lambda: nra) + 1
    _l_(646157)
    _c_(646159, _n_(646158, "func1", lambda: func1))
    _l_(646160)
  elif _n_(646161, "inpt", lambda: inpt) == 'n':
    _l_(646163)

    s = 'success'
    _l_(646162)


x = 0
_l_(646166)
y = 0
_l_(646167)
z = 0
_l_(646168)
s = 'pending'
_l_(646169)
nra = 0
_l_(646170)
nru = 0
_l_(646171)
text1 = 'The number that is running'
_l_(646172)
text2 = 'Number of numbers that ran'
_l_(646173)
text2 = 0
_l_(646174)
inpt = '0'
_l_(646175)
_c_(646177, _n_(646176, "func1", lambda: func1))
_l_(646178)