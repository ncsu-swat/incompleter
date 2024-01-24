# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73186251/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-during-m
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Google(_n_(593424, "GoogleTranslator", lambda: GoogleTranslator), _n_(593425, "GoogleDrive", lambda: GoogleDrive)):
  _l_(593446)

  
  @_n_(593426, "staticmethod", lambda: staticmethod)
  def translate(text: _n_(593427, "str", lambda: str), goal_language: _n_(593428, "str", lambda: str) = "EN") -> Optional[_n_(593429, "str", lambda: str)]:
    _l_(593436)

    aux = _c_(593434, _a_(593431, _n_(593430, "super", lambda: super)(), "translate"), _n_(593432, "text", lambda: text), _n_(593433, "goal_language", lambda: goal_language))
    _l_(593435)
    return aux

  @_n_(593437, "staticmethod", lambda: staticmethod)
  def save_to_drive(text: _n_(593438, "str", lambda: str)) -> _n_(593439, "str", lambda: str):
    _l_(593445)

    aux = _c_(593443, _a_(593441, _n_(593440, "super", lambda: super)(), "save_to_drive"), _n_(593442, "text", lambda: text))
    _l_(593444)
    return aux