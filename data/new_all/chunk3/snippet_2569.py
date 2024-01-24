# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71246045/error-typeerror-float-argument-must-be-a-string-or-a-number-not-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(523655)

except ImportError:
    pass

class Item:
    _l_(523735)

    pay_rate = 0.8 # The pay rate after 20% discount
    _l_(523656) # The pay rate after 20% discount
    all = []
    _l_(523657)
    def __init__(self, name: _n_(523658, "str", lambda: str), price: _n_(523659, "float", lambda: float), quantity=0):
        _l_(523681)

        # Run validations to the received arguments
        assert _n_(523660, "price", lambda: price) >= 0, f"Price {_n_(523661, 'price', lambda: price)} is below 0!"
        _l_(523662)
        assert _n_(523663, "quantity", lambda: quantity) >= 0, f"Price {_n_(523664, 'price', lambda: price)} is below 0!"
        _l_(523665)


        # Assign to self object
        _n_(523666, "self", lambda: self).name = _n_(523667, "name", lambda: name)
        _l_(523668)
        _n_(523669, "self", lambda: self).price = _n_(523670, "price", lambda: price)
        _l_(523671)
        _n_(523672, "self", lambda: self).quantity = _n_(523673, "quantity", lambda: quantity)
        _l_(523674)


        # Actions to execute
        _c_(523679, _a_(523677, _a_(523676, _n_(523675, "Item", lambda: Item), "all"), "append"), _n_(523678, "self", lambda: self))
        _l_(523680)


    def calculate_total_price(self):
        _l_(523687)

        aux = _a_(523683, _n_(523682, "self", lambda: self), "price") * _a_(523685, _n_(523684, "self", lambda: self), "quantity")
        _l_(523686)
        return aux

    def apply_discount(self):
        _l_(523694)

        _n_(523688, "self", lambda: self).price = _a_(523690, _n_(523689, "self", lambda: self), "price") * _a_(523692, _n_(523691, "self", lambda: self), "pay_rate")
        _l_(523693)

    @_n_(523695, "classmethod", lambda: classmethod)
    def instantiate_from_csv(cls):
        _l_(523726)

        with _c_(523697, _n_(523696, "open", lambda: open), 'items.csv', 'r') as f:
            _l_(523707)

            reader = _c_(523701, _a_(523699, _n_(523698, "csv", lambda: csv), "DictReader"), _n_(523700, "f", lambda: f))
            _l_(523702)
            items = _c_(523705, _n_(523703, "list", lambda: list), _n_(523704, "reader", lambda: reader))
            _l_(523706)

        for item in _n_(523708, "items", lambda: items):
            _l_(523725)


            _c_(523723, _n_(523709, "Item", lambda: Item), name=_c_(523712, _a_(523711, _n_(523710, "item", lambda: item), "get"), 'name'),
                price=_c_(523717, _n_(523713, "float", lambda: float), _c_(523716, _a_(523715, _n_(523714, "item", lambda: item), "get"), 'price')),
                quantity=_c_(523722, _n_(523718, "int", lambda: int), _c_(523721, _a_(523720, _n_(523719, "item", lambda: item), "get"), 'quantity')),
                )
            _l_(523724)


    def __repr__(self):
        _l_(523734)

        aux = f"Item('{_a_(523728, _n_(523727, 'self', lambda: self), 'name')}', {_a_(523730, _n_(523729, 'self', lambda: self), 'price')}, {_a_(523732, _n_(523731, 'self', lambda: self), 'quantity')})"
        _l_(523733)
        return aux

_c_(523738, _a_(523737, _n_(523736, "Item", lambda: Item), "instantiate_from_csv"))
_l_(523739)
_c_(523743, _n_(523740, "print", lambda: print), _a_(523742, _n_(523741, "Item", lambda: Item), "all")) 
_l_(523744) 