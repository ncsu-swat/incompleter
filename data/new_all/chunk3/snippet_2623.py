# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68434807/typeerror-conversion-from-decimalfield-to-decimal-is-not-supported
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class User(_n_(552806, "AbstractUser", lambda: AbstractUser)):
    _l_(552812)

    pass
    _l_(552807)

    def __str__(self):
        _l_(552811)

        aux = f"{_a_(552809, _n_(552808, 'self', lambda: self), 'username')}"
        _l_(552810)
        return aux

class AuctionItem(_a_(552814, _n_(552813, "models", lambda: models), "Model")):
    _l_(552843)

    '''
    Description of Auction Item
    '''
    _l_(552815)

    category_choices = [
        ("Fa", "Fashion"),
        ("To", "Toys"),
        ("Fo", "Food"),
        ("El", "Electronics"),
        ("Ho", "Home")
    ]
    _l_(552816)

    title = _c_(552818, _a_(552817, models, "CharField"), max_length=16)
    _l_(552819)
    description = _c_(552821, _a_(552820, models, "CharField"), max_length=128)
    _l_(552822)
    image = _c_(552824, _a_(552823, models, "URLField"))
    _l_(552825)
    category = _c_(552827, _a_(552826, models, "CharField"), max_length=16, choices=category_choices)
    _l_(552828)
    create_time = _c_(552830, _a_(552829, models, "DateTimeField"), auto_now_add=True)
    _l_(552831)
    seller = _c_(552835, _a_(552832, models, "ForeignKey"), _n_(552833, "User", lambda: User), on_delete=_a_(552834, models, "CASCADE"), null=True, related_name="owned")
    _l_(552836)
    initial_price = _c_(552838, _a_(552837, models, "DecimalField"), max_digits=10, decimal_places=2, null=True)
    _l_(552839)
    current_price = _c_(552841, _a_(552840, models, "DecimalField"), max_digits=10, decimal_places=2, null=True, default=0)
    _l_(552842)

class BiddingPrice(_a_(552845, _n_(552844, "models", lambda: models), "Model")):
    _l_(552860)

    '''
    Bidding price of each item
    '''
    _l_(552846)
    bid_price = _c_(552848, _a_(552847, models, "DecimalField"), max_digits=10, decimal_places=2, default=0)
    _l_(552849)
    bidder = _c_(552853, _a_(552850, models, "ForeignKey"), _n_(552851, "User", lambda: User), on_delete=_a_(552852, models, "CASCADE"), null=True)
    _l_(552854)
    auction_item = _c_(552858, _a_(552855, models, "ForeignKey"), _n_(552856, "AuctionItem", lambda: AuctionItem), on_delete=_a_(552857, models, "CASCADE"), null=True, related_name="bidding_price")
    _l_(552859)

class Comments(_a_(552862, _n_(552861, "models", lambda: models), "Model")):
    _l_(552876)

    '''
    Comments made by different users
    '''
    _l_(552863)
    comments = _c_(552865, _a_(552864, models, "CharField"), max_length=200)
    _l_(552866)
    commentor = _c_(552870, _a_(552867, models, "ForeignKey"), _n_(552868, "User", lambda: User), on_delete=_a_(552869, models, "CASCADE"), null=True, related_name="comments_given")
    _l_(552871)
    connected_item = _c_(552874, _a_(552872, models, "ManyToManyField"), _n_(552873, "AuctionItem", lambda: AuctionItem))
    _l_(552875)