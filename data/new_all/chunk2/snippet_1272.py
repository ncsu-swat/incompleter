# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58622983/attributeerror-after-processing-the-view
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class VoteManager(_a_(442349, _n_(442348, "models", lambda: models), "Manager")):
    _l_(442368)


    def get_vote_or_unsaved_blank_vote(self,song,user):
        _l_(442367)

        try:
            _l_(442366)

            aux = _c_(442355, _a_(442352, _a_(442351, _n_(442350, "Vote", lambda: Vote), "objects"), "get"), song=_n_(442353, "song", lambda: song),user=_n_(442354, "user", lambda: user))
            _l_(442356)
            return aux

        except _n_(442357, "ObjectDoesNotExist", lambda: ObjectDoesNotExist):
            _l_(442365)

            aux = _c_(442363, _a_(442360, _a_(442359, _n_(442358, "Vote", lambda: Vote), "objects"), "create"), song=_n_(442361, "song", lambda: song),user=_n_(442362, "user", lambda: user))
            _l_(442364)
            return aux

class Vote(_a_(442370, _n_(442369, "models", lambda: models), "Model")):
    _l_(442393)

    UP = 1
    _l_(442371)
    DOWN = -1
    _l_(442372)
    VALUE_CHOICE = ((UP, "👍️"),(DOWN, "👎️"),)
    _l_(442373)


    like = _c_(442375, _a_(442374, models, "SmallIntegerField"), null=True, blank=True, choices=VALUE_CHOICE)
    _l_(442376)
    user = _c_(442379, _a_(442377, models, "ForeignKey"), User,on_delete=_a_(442378, models, "CASCADE"))
    _l_(442380)
    song = _c_(442383, _a_(442381, models, "ForeignKey"), Song, on_delete=_a_(442382, models, "CASCADE"))
    _l_(442384)
    voted_on = _c_(442386, _a_(442385, models, "DateTimeField"), auto_now=True)
    _l_(442387)

    objects = _c_(442389, _n_(442388, "VoteManager", lambda: VoteManager))
    _l_(442390)

    class Meta:
        _l_(442392)

        unique_together = ('user', 'song')
        _l_(442391)