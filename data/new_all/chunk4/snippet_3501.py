# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73186251/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-during-m
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AbsTranslator(_n_(638456, "ABC", lambda: ABC)):
  _l_(638462)

  @abstractmethod
  def translate(text: _n_(638457, "str", lambda: str), goal_language: _n_(638458, "str", lambda: str)) -> Optional[_n_(638459, "str", lambda: str)]:
    _l_(638461)

    pass
    _l_(638460)

class AbsDrive(_n_(638463, "ABC", lambda: ABC)):
  _l_(638467)

  @abstractmethod
  def save_to_drive(text: _n_(638464, "str", lambda: str)) -> None:
    _l_(638466)

    pass
    _l_(638465)