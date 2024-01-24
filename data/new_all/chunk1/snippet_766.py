# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58575057/update-throwing-typeerror-serializer-update-got-an-unexpected-keyword-argum
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SMSMessages(_a_(387238, _n_(387237, "models", lambda: models), "Model")):
    _l_(387263)

    sms_number_to = _c_(387240, _a_(387239, models, "CharField"), max_length=14)
    _l_(387241)
    sms_content = _c_(387243, _a_(387242, models, "CharField"), max_length=160)
    _l_(387244)
    sending_user = _c_(387247, _a_(387245, models, "ForeignKey"), "SMSUser", on_delete=_a_(387246, models, "PROTECT"), related_name="user_that_sent")
    _l_(387248)
    sent_date = _c_(387250, _a_(387249, models, "DateTimeField"), auto_now=True)
    _l_(387251)
    delivery_status = _c_(387253, _a_(387252, models, "BooleanField"), default=False)
    _l_(387254)

    class Meta:
        _l_(387256)

        verbose_name_plural = "SMSMessages"
        _l_(387255)

    def __str__(self):
        _l_(387262)

        aux = _c_(387260, _n_(387257, "str", lambda: str), _a_(387259, _n_(387258, "self", lambda: self), "sending_user"))
        _l_(387261)
        return aux