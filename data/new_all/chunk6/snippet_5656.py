# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41475703/beautiful-soup-attributeerror-nonetype-object-has-no-attribute-find
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
foodDict = {}
_l_(373416)
foodList = _c_(373419, _a_(373418, _n_(373417, "bsObj", lambda: bsObj), "findAll"), "td")
_l_(373420)
for foodItem in _n_(373421, "foodList", lambda: foodList):
    _l_(373480)

    _c_(373426, _n_(373422, "print", lambda: print), "foodItems: " +_c_(373425, _a_(373424, _n_(373423, "foodItem", lambda: foodItem), "getText")))
    _l_(373427)
    meal = _c_(373437, _a_(373436, _c_(373435, _a_(373434, _c_(373433, _a_(373432, _a_(373431, _a_(373430, _a_(373429, _n_(373428, "foodItem", lambda: foodItem), "parent"), "parent"), "parent"), "find"), "h4"), "getText")), "lower"))
    _l_(373438)
    _c_(373441, _n_(373439, "print", lambda: print), "Meal: " +_n_(373440, "meal", lambda: meal))
    _l_(373442)
    diningHall = _c_(373455, _a_(373454, _c_(373453, _a_(373452, _c_(373451, _a_(373450, _a_(373449, _a_(373448, _a_(373447, _a_(373446, _a_(373445, _a_(373444, _n_(373443, "foodItem", lambda: foodItem), "parent"), "parent"), "parent"), "parent"), "parent"), "parent"), "find"), "h2"), "getText")), "lower"))
    _l_(373456)
    s = "-"
    _l_(373457)
    seq = (_n_(373458, "meal", lambda: meal), _n_(373459, "diningHall", lambda: diningHall))
    _l_(373460)
    mealAndHall = _c_(373464, _a_(373462, _n_(373461, "s", lambda: s), "join"), _n_(373463, "seq", lambda: seq))
    _l_(373465)
    _n_(373466, "foodDict", lambda: foodDict)[_c_(373473, _a_(373472, _c_(373471, _a_(373470, _c_(373469, _a_(373468, _n_(373467, "foodItem", lambda: foodItem), "getText")), "lower")), "strip"))] = _n_(373474, "mealAndHall", lambda: mealAndHall)
    _l_(373475)
    _c_(373478, _n_(373476, "print", lambda: print), _n_(373477, "foodDict", lambda: foodDict))
    _l_(373479)