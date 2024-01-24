# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64190731/typeerror-at-init-got-an-unexpected-keyword-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BidCreateView(_n_(572439, "LoginRequiredMixin", lambda: LoginRequiredMixin), _n_(572440, "CreateView", lambda: CreateView)):
    _l_(572533)

    
    model = Bid
    _l_(572441)
    form_class = BidForm
    _l_(572442)
    template_name = "auction/auction_detail.html"
    _l_(572443)

    def get_context_data(self, **kwargs):
        _l_(572468)

        bidder = _a_(572446, _a_(572445, _n_(572444, "self", lambda: self), "request"), "user")
        _l_(572447)
        c = _c_(572451, _a_(572449, _n_(572448, "super", lambda: super)(), "get_context_data"), **_n_(572450, "kwargs", lambda: kwargs))
        _l_(572452)
        _n_(572453, "c", lambda: c)["auction"] = _a_(572455, _n_(572454, "self", lambda: self), "auction")
        _l_(572456)
        if _a_(572458, _n_(572457, "bidder", lambda: bidder), "id") is _a_(572462, _a_(572461, _a_(572460, _n_(572459, "self", lambda: self), "auction"), "user"), "id"):
            _l_(572465)

            _n_(572463, "c", lambda: c)["form"] = None
            _l_(572464)
        aux = _n_(572466, "c", lambda: c)
        _l_(572467)
        return aux

    ###get_form_kwargs() method to supply user and listing during form creation
    def get_form_kwargs(self):
        _l_(572488)


        kwargs = _c_(572471, _a_(572470, _n_(572469, "super", lambda: super)(), "get_form_kwargs"))
        _l_(572472)
        pk_ = _c_(572476, _a_(572475, _a_(572474, _n_(572473, "self", lambda: self), "kwargs"), "get"), 'pk')
        _l_(572477)
        auction = _c_(572482, _a_(572480, _a_(572479, _n_(572478, "Listing", lambda: Listing), "objects"), "get"), pk = _n_(572481, "pk_", lambda: pk_))
        _l_(572483)
        kwargs = {
            'auction' : _n_(572484, "auction", lambda: auction)
        }
        _l_(572485)
        aux = _n_(572486, "kwargs", lambda: kwargs)
        _l_(572487)

        return aux

    def form_invalid(self, form):
        _l_(572494)

        aux = _c_(572492, _a_(572490, _n_(572489, "super", lambda: super)(), "form_invalid"), _n_(572491, "form", lambda: form))
        _l_(572493)
        return aux

    def form_valid(self, form):
        _l_(572532)

        bid_amount = _a_(572496, _n_(572495, "form", lambda: form), "cleaned_data")["amount"]
        _l_(572497)

        try:
            _l_(572520)

            with _c_(572500, _a_(572499, _n_(572498, "transaction", lambda: transaction), "atomic")):
                _l_(572511)

                _c_(572509, _a_(572502, _n_(572501, "Bid", lambda: Bid), "high_bid"), _a_(572504, _n_(572503, "self", lambda: self), "auction"),
                    _a_(572507, _a_(572506, _n_(572505, "self", lambda: self), "request"), "user"),
                    _n_(572508, "bid_amount", lambda: bid_amount)
                )
                _l_(572510)
        except _n_(572512, "IntegrityError", lambda: IntegrityError):
            _l_(572519)

            _c_(572517, _a_(572514, _n_(572513, "messages", lambda: messages), "error"), _a_(572516, _n_(572515, "self", lambda: self), "request"), "An unexpected error has occured")
            _l_(572518)

        _c_(572525, _a_(572522, _n_(572521, "messages", lambda: messages), "success"), _a_(572524, _n_(572523, "self", lambda: self), "request"), "Bid submitted successfully!")
        _l_(572526)
        aux = _c_(572530, _a_(572528, _n_(572527, "super", lambda: super)(), "form_valid"), _n_(572529, "form", lambda: form))
        _l_(572531)

        return aux