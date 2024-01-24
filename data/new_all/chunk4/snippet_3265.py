# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76475514/typeerror-cannot-parse-argument-of-type-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PagSeguroView(_n_(623779, "LoginRequiredMixin", lambda: LoginRequiredMixin), _n_(623780, "RedirectView", lambda: RedirectView)):
    _l_(623827)


    def get_redirect_url(self, *args, **kwargs):
        _l_(623826)

        order_pk = _c_(623784, _a_(623783, _a_(623782, _n_(623781, "self", lambda: self), "kwargs"), "get"), 'pk')
        _l_(623785)
        order = _c_(623795, _n_(623786, "get_object_or_404", lambda: get_object_or_404), _c_(623793, _a_(623789, _a_(623788, _n_(623787, "Order", lambda: Order), "objects"), "filter"), user=_a_(623792, _a_(623791, _n_(623790, "self", lambda: self), "request"), "user")), pk=_n_(623794, "order_pk", lambda: order_pk)
        )
        _l_(623796)
        pg = _c_(623799, _a_(623798, _n_(623797, "order", lambda: order), "pagseguro"))
        _l_(623800)
        _n_(623801, "pg", lambda: pg).redirect_url = _c_(623809, _a_(623804, _a_(623803, _n_(623802, "self", lambda: self), "request"), "build_absolute_uri"), _c_(623808, _n_(623805, "reverse", lambda: reverse), 'checkout:order_detail', args=[_a_(623807, _n_(623806, "order", lambda: order), "pk")])
        )
        _l_(623810)
        _n_(623811, "pg", lambda: pg).notification_url = _c_(623817, _a_(623814, _a_(623813, _n_(623812, "self", lambda: self), "request"), "build_absolute_uri"), _c_(623816, _n_(623815, "reverse", lambda: reverse), 'checkout:pagseguro_notification')
        )
        _l_(623818)
        response = _c_(623821, _a_(623820, _n_(623819, "pg", lambda: pg), "checkout"))
        _l_(623822)
        aux = _a_(623824, _n_(623823, "response", lambda: response), "payment_url")
        _l_(623825)
        return aux