# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63771033/i-am-trying-to-display-added-items-to-my-cart-page-but-when-i-render-my-cart-pa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Order(_a_(426416, _n_(426415, "models", lambda: models), "Model")):
    _l_(426466)

    costumer = _c_(426419, _a_(426417, models, "ForeignKey"), Costumer, on_delete=_a_(426418, models, "SET_NULL"), blank=True, null=True)
    _l_(426420)
    date_ordered = _c_(426422, _a_(426421, models, "DateTimeField"), auto_now_add=True)
    _l_(426423)
    complete = _c_(426425, _a_(426424, models, "BooleanField"), default=False, null=True, blank=False)
    _l_(426426)
    transaction_id = _c_(426428, _a_(426427, models, "CharField"), max_length=200, null=True)
    _l_(426429)

    def __str__(self):
        _l_(426435)

        aux = _c_(426433, _n_(426430, "str", lambda: str), _a_(426432, _n_(426431, "self", lambda: self), "id"))
        _l_(426434)
        return aux
    
    @ _n_(426436, "property", lambda: property)
    def get_cart_total(self):
        _l_(426450)

        orderitems = _c_(426440, _a_(426439, _a_(426438, _n_(426437, "self", lambda: self), "orderitem_set"), "all"))
        _l_(426441)
        total = _c_(426446, _n_(426442, "sum", lambda: sum), [_a_(426444, _n_(426443, "item", lambda: item), "get_total") for item in _n_(426445, "orderitems", lambda: orderitems)])
        _l_(426447)
        aux = _n_(426448, "total", lambda: total)
        _l_(426449)
        return aux
    
    @ _n_(426451, "property", lambda: property)
    def get_cart_items(self):
        _l_(426465)

        orderitems = _c_(426455, _a_(426454, _a_(426453, _n_(426452, "self", lambda: self), "orderitem_set"), "all"))
        _l_(426456)
        total = _c_(426461, _n_(426457, "sum", lambda: sum), [_a_(426459, _n_(426458, "item", lambda: item), "quantity") for item in _n_(426460, "orderitems", lambda: orderitems)])
        _l_(426462)
        aux = _n_(426463, "total", lambda: total)
        _l_(426464)
        return aux