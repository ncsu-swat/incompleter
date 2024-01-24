# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71188328/typeerror-nonetype-object-is-not-subscriptable-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if 0 < _n_(352255, "i", lambda: i) < _n_(352256, "noSteps", lambda: noSteps):
    _l_(352282)

    order = _c_(352269, _a_(352268, _c_(352267, _a_(352259, _a_(352258, _n_(352257, "client", lambda: client), "LinearOrder"), "LinearOrder_new"), side=_n_(352260, "side", lambda: side), symbol="BTCUSDT", order_type="Limit",
                                                qty=_n_(352261, "allocatedQuantities", lambda: allocatedQuantities)[_n_(352262, "i", lambda: i)], price=_n_(352263, "priceArray", lambda: priceArray)[_n_(352264, "i", lambda: i)],
                                                time_in_force="GoodTillCancel",
                                                reduce_only=False, close_on_trigger=False,
                                                take_profit=_n_(352265, "takeProfits", lambda: takeProfits)[_n_(352266, "i", lambda: i)]), "result"))
    _l_(352270)
    _c_(352273, _n_(352271, "print", lambda: print), _n_(352272, "order", lambda: order))
    _l_(352274)
    temp_order = _n_(352275, "order", lambda: order)[0]['result']['order_id']
    _l_(352276)
    _c_(352280, _a_(352278, _n_(352277, "ordersArray", lambda: ordersArray), "append"), _n_(352279, "temp_order", lambda: temp_order))
    _l_(352281)