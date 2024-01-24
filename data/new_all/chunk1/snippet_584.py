# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70564695/typeerror-unsupported-operand-types-for-float-and-decimal-decimal
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ExchangeRates(_n_(408271, "TimeStampedModel", lambda: TimeStampedModel)):
    _l_(408309)

    date = _c_(408273, _a_(408272, models, "DateField"), unique=True)
    _l_(408274)
    timestamp = _c_(408276, _a_(408275, models, "BigIntegerField"), blank=True, null=True)
    _l_(408277)
    base_currency = _c_(408279, _a_(408278, models, "CharField"), max_length=10, default='GBP')
    _l_(408280)
    data = _c_(408281, JSONField)
    _l_(408282)

    def get_currency_rate(self, currency):
        _l_(408289)

        aux = _c_(408287, _n_(408283, "Decimal", lambda: Decimal), _a_(408285, _n_(408284, "self", lambda: self), "data")[_n_(408286, "currency", lambda: currency)])
        _l_(408288)
        return aux

    def convert(self, from_currency, to_currency, value):
        _l_(408308)

        from_rate = _c_(408293, _a_(408291, _n_(408290, "self", lambda: self), "get_currency_rate"), _n_(408292, "from_currency", lambda: from_currency))
        _l_(408294)
        to_rate = _c_(408298, _a_(408296, _n_(408295, "self", lambda: self), "get_currency_rate"), _n_(408297, "to_currency", lambda: to_currency))
        _l_(408299)
        aux = _c_(408306, _n_(408300, "round", lambda: round), (_c_(408303, _n_(408301, "Decimal", lambda: Decimal), _n_(408302, "value", lambda: value) or 0) / _n_(408304, "from_rate", lambda: from_rate)) * _n_(408305, "to_rate", lambda: to_rate), 6)
        _l_(408307)


        return aux