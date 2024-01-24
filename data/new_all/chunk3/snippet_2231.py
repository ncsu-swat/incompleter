# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55937881/how-to-fix-typeerror-introduced-by-switching-from-python-2-7-10-to-python-3-7
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import subprocess
  _l_(569704)

except ImportError:
  pass

def getLength(filename):
  _l_(569721)

  result = _c_(569712, _a_(569706, _n_(569705, "subprocess", lambda: subprocess), "Popen"), ["ffprobe", _n_(569707, "filename", lambda: filename)],
    stdout = _a_(569709, _n_(569708, "subprocess", lambda: subprocess), "PIPE"), stderr = _a_(569711, _n_(569710, "subprocess", lambda: subprocess), "STDOUT"))
  _l_(569713)
  aux = [_n_(569714, "x", lambda: x) for x in _c_(569718, _a_(569717, _a_(569716, _n_(569715, "result", lambda: result), "stdout"), "readlines")) if "Duration" in _n_(569719, "x", lambda: x)]
  _l_(569720)
  return aux

_c_(569725, _n_(569722, "print", lambda: print), _c_(569724, _n_(569723, "getLength", lambda: getLength), 'bell.mp4'))
_l_(569726)