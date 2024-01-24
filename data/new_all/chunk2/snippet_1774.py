# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56919286/function-call-with-np-ndarray-say-typeerror-missing-1-required-positional-argu
#coding:utf-8

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import numpy as np
  _l_(436274)

except ImportError:
  pass

def rotate_roll (th):
  _l_(436294)

  _rot_vec_roll = {
    { 1.,          0. ,         0.},
    { 0.,   _c_(436278, _a_(436276, _n_(436275, "np", lambda: np), "cos"), _n_(436277, "th", lambda: th)), _c_(436282, _a_(436280, _n_(436279, "np", lambda: np), "sin"), _n_(436281, "th", lambda: th))},
    { 0., - _c_(436286, _a_(436284, _n_(436283, "np", lambda: np), "sin"), _n_(436285, "th", lambda: th)), _c_(436290, _a_(436288, _n_(436287, "np", lambda: np), "cos"), _n_(436289, "th", lambda: th))}
  }
  _l_(436291)
  aux = _n_(436292, "_rot_vec_roll", lambda: _rot_vec_roll)
  _l_(436293)
  return aux

def rotate_pitch (th):
  _l_(436314)

  _rot_vec_pitch = {
    {  _c_(436298, _a_(436296, _n_(436295, "np", lambda: np), "cos"), _n_(436297, "th", lambda: th)),0. , _c_(436302, _a_(436300, _n_(436299, "np", lambda: np), "sin"), _n_(436301, "th", lambda: th))},
    {  0.,        1.,          0.},
    {- _c_(436306, _a_(436304, _n_(436303, "np", lambda: np), "sin"), _n_(436305, "th", lambda: th)),1.,  _c_(436310, _a_(436308, _n_(436307, "np", lambda: np), "cos"), _n_(436309, "th", lambda: th))}
  }
  _l_(436311)
  aux = _n_(436312, "_rot_vec_pitch", lambda: _rot_vec_pitch)
  _l_(436313)
  return aux

def rotate_yaw (th):
  _l_(436334)

  _rot_vec_yaw = {
    {   _c_(436318, _a_(436316, _n_(436315, "np", lambda: np), "cos"), _n_(436317, "th", lambda: th)), _c_(436322, _a_(436320, _n_(436319, "np", lambda: np), "sin"), _n_(436321, "th", lambda: th)), 0.},
    { - _c_(436326, _a_(436324, _n_(436323, "np", lambda: np), "sin"), _n_(436325, "th", lambda: th)), _c_(436330, _a_(436328, _n_(436327, "np", lambda: np), "cos"), _n_(436329, "th", lambda: th)), 0.},
    {           0.,         0., 1.}
  }
  _l_(436331)
  aux = _n_(436332, "_rot_vec_yaw", lambda: _rot_vec_yaw)
  _l_(436333)
  return aux

# R2 = A * R1 
# A = roll_vec * pitch_vec * yaw_vec

Vector = _c_(436339, _a_(436336, _n_(436335, "np", lambda: np), "ndarray"), shape=(1,3), dtype=_a_(436338, _n_(436337, "np", lambda: np), "float"))
_l_(436340)

def rotate_rpy(posvec: _n_(436341, "Vector", lambda: Vector), rotvec: _n_(436342, "Vector", lambda: Vector)) -> _n_(436343, "Vector", lambda: Vector) :
  _l_(436364)

  aux = _c_(436362, _a_(436345, _n_(436344, "np", lambda: np), "dot"), _c_(436358, _a_(436347, _n_(436346, "np", lambda: np), "dot"), _c_(436354, _a_(436349, _n_(436348, "np", lambda: np), "dot"), _n_(436350, "posvec", lambda: posvec), _c_(436353, _n_(436351, "rotate_rpy", lambda: rotate_rpy), _n_(436352, "rotvec", lambda: rotvec)[0]) ), _c_(436357, _n_(436355, "rotate_pitch", lambda: rotate_pitch), _n_(436356, "rotvec", lambda: rotvec)[1]) ), _c_(436361, _n_(436359, "rotate_yaw", lambda: rotate_yaw), _n_(436360, "rotvec", lambda: rotvec)[2]))
  _l_(436363)
  return aux

mypose = _c_(436369, _a_(436366, _n_(436365, "np", lambda: np), "ndarray"), shape=(1,3), dtype=_a_(436368, _n_(436367, "np", lambda: np), "float"))
_l_(436370)
mypose = _c_(436374, _a_(436372, _n_(436371, "np", lambda: np), "array"), [3.0,1.0,1.0], dtype=_n_(436373, "float", lambda: float))
_l_(436375)

_c_(436378, _n_(436376, "print", lambda: print), _n_(436377, "mypose", lambda: mypose))
_l_(436379)

base = _a_(436381, _n_(436380, "np", lambda: np), "pi") / 6.0
_l_(436382)

rotateang = _c_(436387, _a_(436384, _n_(436383, "np", lambda: np), "ndarray"), shape=(1,3), dtype=_a_(436386, _n_(436385, "np", lambda: np), "float"))
_l_(436388)
rotateang = _c_(436395, _a_(436390, _n_(436389, "np", lambda: np), "array"), [_n_(436391, "base", lambda: base), _n_(436392, "base", lambda: base)/2.0, _n_(436393, "base", lambda: base)], dtype=_n_(436394, "float", lambda: float))
_l_(436396)

_c_(436399, _n_(436397, "print", lambda: print), _n_(436398, "rotateang", lambda: rotateang))
_l_(436400)

newpose = _c_(436405, _a_(436402, _n_(436401, "np", lambda: np), "ndarray"), shape=(1,3), dtype=_a_(436404, _n_(436403, "np", lambda: np), "float"))
_l_(436406)
newpose = _c_(436410, _n_(436407, "rotate_rpy", lambda: rotate_rpy), _n_(436408, "mypose", lambda: mypose), _n_(436409, "rotateang", lambda: rotateang))#enbug
_l_(436411)#enbug
_c_(436414, _n_(436412, "print", lambda: print), _n_(436413, "newpose", lambda: newpose));
_l_(436415)