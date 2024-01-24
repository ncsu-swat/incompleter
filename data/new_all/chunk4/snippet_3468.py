# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73842091/attribute-error-object-has-no-attributes-while-trying-to-update-the-manytoo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ReviewSerializer(_a_(604856, _n_(604855, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(604863)

    username = _c_(604858, _a_(604857, serializers, "StringRelatedField"), read_only=True)
    _l_(604859)
    
    class Meta:
        _l_(604862)

        model = Review
        _l_(604860)
        exclude = ["watchlist"]
        _l_(604861)


class WatchListSerializer(_a_(604865, _n_(604864, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(604872)

    ### using relation serializer to list all the reviews in a movie 
    reviews = _c_(604867, _n_(604866, "ReviewSerializer", lambda: ReviewSerializer), many=True, read_only=True)
    _l_(604868)

    class Meta:
        _l_(604871)

        model = WatchList
        _l_(604869)
        fields = "__all__"
        _l_(604870)