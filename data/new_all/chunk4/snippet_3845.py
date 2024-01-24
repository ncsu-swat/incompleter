# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25674812/typeerror-cannot-concatenate-str-and-int-objects-need-help-fixing
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
ItemName = 0.0
_l_(639166)
Pounds = 0.0
_l_(639167)
Ounces = 0.0
_l_(639168)
Unit_Price = 0.0
_l_(639169)
Pound_Price = 0.0
_l_(639170)
Total_Price = 0.0
_l_(639171)

ItemName = _c_(639173, _n_(639172, "raw_input", lambda: raw_input), "Enter ItemName")
_l_(639174)
Pounds = _c_(639178, _n_(639175, "int", lambda: int), _c_(639177, _n_(639176, "input", lambda: input), "Enter amount of Pounds"))
_l_(639179)
Ounces = _c_(639183, _n_(639180, "int", lambda: int), _c_(639182, _n_(639181, "input", lambda: input), "Enter amuont of Ounces"))
_l_(639184)
Pound_Price = _c_(639188, _n_(639185, "int", lambda: int), _c_(639187, _n_(639186, "input", lambda: input), "Enter Pound_Price"))
_l_(639189)
Unit_Price = _c_(639193, _n_(639190, "int", lambda: int), _c_(639192, _n_(639191, "input", lambda: input), "Enter Unit_Price"))
_l_(639194)

Total_Price = _n_(639195, "Pound_Price", lambda: Pound_Price) * (_n_(639196, "Pounds", lambda: Pounds) + _n_(639197, "Ounces", lambda: Ounces) / 16)
_l_(639198)

_c_(639201, _n_(639199, "print", lambda: print), "Item name is: " + _n_(639200, "ItemName", lambda: ItemName))
_l_(639202)
_c_(639205, _n_(639203, "print", lambda: print), "Your Unit price is: $" + _n_(639204, "Unit_Price", lambda: Unit_Price))
_l_(639206)
_c_(639209, _n_(639207, "print", lambda: print), "Your Total Comes To: $" + _n_(639208, "Total_Price", lambda: Total_Price))
_l_(639210)