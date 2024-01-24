# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75572426/python-oop-typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(609675)

except ImportError:
    pass
class Item:
    _l_(609754)

    pay_rate = 0.8
    _l_(609676)
    all = []
    _l_(609677)
    def __init__(self, name: _n_(609678, "str", lambda: str), price: _n_(609679, "int", lambda: int) , quantity: _n_(609680, "int", lambda: int)):
        _l_(609700)

        #run validation to the received arguments
        assert _n_(609681, "quantity", lambda: quantity) >= 0, "The {quantity} quantity should be greater or equal to zero"
        _l_(609682)
        assert _n_(609683, "price", lambda: price) >= 0, "The price should be greater or equal to zero"
        _l_(609684)

        #assigned to the self object      
        _n_(609685, "self", lambda: self).name = _n_(609686, "name", lambda: name)
        _l_(609687)
        _n_(609688, "self", lambda: self).price = _n_(609689, "price", lambda: price)
        _l_(609690)
        _n_(609691, "self", lambda: self).quantity = _n_(609692, "quantity", lambda: quantity)
        _l_(609693)

        #Action to execute
        _c_(609698, _a_(609696, _a_(609695, _n_(609694, "Item", lambda: Item), "all"), "append"), _n_(609697, "self", lambda: self))
        _l_(609699)

    def calculate_total_price(self):
        _l_(609706)

        aux = _a_(609702, _n_(609701, "self", lambda: self), "price") * _a_(609704, _n_(609703, "self", lambda: self), "quantity")
        _l_(609705)
        return aux

    def apply_discount(self):
        _l_(609713)

        _n_(609707, "self", lambda: self).price = _a_(609709, _n_(609708, "self", lambda: self), "price") * _a_(609711, _n_(609710, "self", lambda: self), "pay_rate")
        _l_(609712)

    @_n_(609714, "classmethod", lambda: classmethod)
    def intantiate_from_csv(cls):
        _l_(609745)

        with _c_(609716, _n_(609715, "open", lambda: open), 'items.csv', 'r') as f:
            _l_(609726)

            reader = _c_(609720, _a_(609718, _n_(609717, "csv", lambda: csv), "DictReader"), _n_(609719, "f", lambda: f))
            _l_(609721)
            items = _c_(609724, _n_(609722, "list", lambda: list), _n_(609723, "reader", lambda: reader))
            _l_(609725)

        for item in _n_(609727, "items", lambda: items):
            _l_(609744)

            _c_(609742, _n_(609728, "Item", lambda: Item), name=_c_(609731, _a_(609730, _n_(609729, "item", lambda: item), "get"), 'name'),
                price=_c_(609736, _n_(609732, "float", lambda: float), _c_(609735, _a_(609734, _n_(609733, "item", lambda: item), "get"), 'price')),
                quantity=_c_(609741, _n_(609737, "int", lambda: int), _c_(609740, _a_(609739, _n_(609738, "item", lambda: item), "get"), 'quantity')),
            )
            _l_(609743)

    def __repr__(self):
        _l_(609753)

        aux = f"Item('{_a_(609747, _n_(609746, 'self', lambda: self), 'name')}', {_a_(609749, _n_(609748, 'self', lambda: self), 'price')}, {_a_(609751, _n_(609750, 'self', lambda: self), 'quantity')})"
        _l_(609752)
        return aux


# items


_c_(609757, _a_(609756, _n_(609755, "Item", lambda: Item), "intantiate_from_csv"))
_l_(609758)
_c_(609762, _n_(609759, "print", lambda: print), _a_(609761, _n_(609760, "Item", lambda: Item), "all"))
_l_(609763)