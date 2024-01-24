# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56919286/function-call-with-np-ndarray-say-typeerror-missing-1-required-positional-argu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def rotate_rpy(posvec: _n_(430654, "Vector", lambda: Vector), rotvec: _n_(430655, "Vector", lambda: Vector)) -> _n_(430656, "Vector", lambda: Vector) :
  _l_(430677)

  aux = _c_(430675, _a_(430658, _n_(430657, "np", lambda: np), "dot"), _c_(430671, _a_(430660, _n_(430659, "np", lambda: np), "dot"), _c_(430667, _a_(430662, _n_(430661, "np", lambda: np), "dot"), _n_(430663, "posvec", lambda: posvec), _c_(430666, _n_(430664, "rotate_rpy", lambda: rotate_rpy), _n_(430665, "rotvec", lambda: rotvec)[0]) ), _c_(430670, _n_(430668, "rotate_pitch", lambda: rotate_pitch), _n_(430669, "rotvec", lambda: rotvec)[1]) ), _c_(430674, _n_(430672, "rotate_yaw", lambda: rotate_yaw), _n_(430673, "rotvec", lambda: rotvec)[2]))
  _l_(430676)
  return aux

newpose = _c_(430681, _n_(430678, "rotate_rpy", lambda: rotate_rpy), _n_(430679, "mypose", lambda: mypose), _n_(430680, "rotateang", lambda: rotateang))#enbug
_l_(430682)#enbug