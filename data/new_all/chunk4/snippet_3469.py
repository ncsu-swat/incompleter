# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73842091/attribute-error-object-has-no-attributes-while-trying-to-update-the-manytoo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ReviewCreateView(_a_(607829, _n_(607828, "generics", lambda: generics), "CreateAPIView")):
    _l_(607894)

    serializer_class = ReviewSerializer
    _l_(607830)
    permission_classes = [IsAuthenticated]
    _l_(607831)

    def get_queryset(self):
        _l_(607837)

        aux = _c_(607835, _a_(607834, _a_(607833, _n_(607832, "Review", lambda: Review), "objects"), "all"))
        _l_(607836)
        return aux

    def perform_create(self, serializer):
        _l_(607893)

        ##posting the comment in a movie using movies primary key
        primary_key = _c_(607841, _a_(607840, _a_(607839, _n_(607838, "self", lambda: self), "kwargs"), "get"), "pk")
        _l_(607842)
        watchlist = _c_(607847, _a_(607845, _a_(607844, _n_(607843, "WatchList", lambda: WatchList), "objects"), "get"), pk=_n_(607846, "primary_key", lambda: primary_key))
        _l_(607848)

        #NOt allowing the same user to comment on the same movie twice
        username = _a_(607851, _a_(607850, _n_(607849, "self", lambda: self), "request"), "user")
        _l_(607852)
        review_queryset = _c_(607858, _a_(607855, _a_(607854, _n_(607853, "Review", lambda: Review), "objects"), "filter"), watchlist=_n_(607856, "watchlist", lambda: watchlist), username=_n_(607857, "username", lambda: username))
        _l_(607859)
        if _c_(607862, _a_(607861, _n_(607860, "review_queryset", lambda: review_queryset), "exists")):
            _l_(607866)

            raise _c_(607864, _n_(607863, "ValidationError", lambda: ValidationError), "You cannot comment on the same movie Twice")
            _l_(607865)

        ##NOTE: want to updated this section
        if _a_(607868, _n_(607867, "watchlist", lambda: watchlist), "avg_rating") == 0:
            _l_(607879)

            _n_(607869, "watchlist", lambda: watchlist).avg_rating = _a_(607871, _n_(607870, "serializer", lambda: serializer), "validated_data")['avg_rating']
            _l_(607872)
        else:
            _n_(607873, "watchlist", lambda: watchlist).avg_rating = (_a_(607875, _n_(607874, "watchlist", lambda: watchlist), "avg_rating") + _a_(607877, _n_(607876, "serializer", lambda: serializer), "validated_data")['avg_rating'])/2
            _l_(607878)

        _n_(607880, "watchlist", lambda: watchlist).num_rating += 1
        _l_(607881)
        _c_(607885, _a_(607884, _a_(607883, _n_(607882, "watchlist", lambda: watchlist), "avg_rating"), "save"))
        _l_(607886)
        _c_(607891, _a_(607888, _n_(607887, "serializer", lambda: serializer), "save"), watchlist=_n_(607889, "watchlist", lambda: watchlist), username=_n_(607890, "username", lambda: username))
        _l_(607892)