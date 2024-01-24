# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27882285/blender-bge-import-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Controller = _c_(446822, _a_(446821, _a_(446820, _n_(446819, "bge", lambda: bge), "logic"), "getCurrentController"))
_l_(446823)
Owner = _a_(446825, _n_(446824, "Controller", lambda: Controller), "owner")
_l_(446826)
Move = _a_(446828, _n_(446827, "Controller", lambda: Controller), "actuators")['Spin']
_l_(446829)
PressLeft = _a_(446831, _n_(446830, "Controller", lambda: Controller), "sensors")['SpinLeft']
_l_(446832)
PressRight = _a_(446834, _n_(446833, "Controller", lambda: Controller), "sensors")['SpinRight']
_l_(446835)
Speed = _a_(446837, _n_(446836, "Move", lambda: Move), "dRot")[1]
_l_(446838)

if _a_(446840, _n_(446839, "PressLeft", lambda: PressLeft), "positive"):
  _l_(446859)

  Speed = _n_(446841, "Speed", lambda: Speed) + 0.5
  _l_(446842)
  _n_(446843, "Move", lambda: Move).dRot = [0.0, _n_(446844, "Speed", lambda: Speed), 0.0]
  _l_(446845)
  _c_(446849, _a_(446847, _n_(446846, "Controller", lambda: Controller), "activate"), _n_(446848, "Move", lambda: Move))
  _l_(446850)
elif _a_(446852, _n_(446851, "PressRight", lambda: PressRight), "positive"):
  _l_(446858)

  Speed = _n_(446853, "Speed", lambda: Speed) - 0.5
  _l_(446854)
  _n_(446855, "Move", lambda: Move).dRot = [0.0, _n_(446856, "Speed", lambda: Speed), 0.0]
  _l_(446857)