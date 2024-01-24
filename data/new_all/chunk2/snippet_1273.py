# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58622983/attributeerror-after-processing-the-view
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class SongDetailView(_n_(445140, "DetailView", lambda: DetailView)):
    _l_(445182)

    model = Song
    _l_(445141)
    template_name = 'song/song_detail.html'
    _l_(445142)

    def get_context_data(self,**kwargs):
        _l_(445181)

        ctx = _c_(445146, _a_(445144, _n_(445143, "super", lambda: super)(), "get_context_data"), **_n_(445145, "kwargs", lambda: kwargs))
        _l_(445147)

        if _a_(445151, _a_(445150, _a_(445149, _n_(445148, "self", lambda: self), "request"), "user"), "is_authenticated"):
            _l_(445178)

            vote = _c_(445160, _a_(445154, _a_(445153, _n_(445152, "Vote", lambda: Vote), "objects"), "get_vote_or_unsaved_blank_vote"), song=_a_(445156, _n_(445155, "self", lambda: self), "object"), user = _a_(445159, _a_(445158, _n_(445157, "self", lambda: self), "request"), "user"))
            _l_(445161)
            vote_url = _c_(445166, _n_(445162, "reverse", lambda: reverse), 'music:song_vote_create', kwargs={'song_id':_a_(445165, _a_(445164, _n_(445163, "vote", lambda: vote), "song"), "id")})
            _l_(445167)
            vote_form = _c_(445170, _n_(445168, "SongVoteForm", lambda: SongVoteForm), instance=_n_(445169, "vote", lambda: vote))
            _l_(445171)
            _n_(445172, "ctx", lambda: ctx)['vote_form'] = _n_(445173, "vote_form", lambda: vote_form)
            _l_(445174)
            _n_(445175, "ctx", lambda: ctx)['vote_url'] = _n_(445176, "vote_url", lambda: vote_url)
            _l_(445177)
        aux = _n_(445179, "ctx", lambda: ctx)
        _l_(445180)
        return aux

class SongVoteCreateView(_n_(445183, "View", lambda: View)):
    _l_(445239)

    form_class = SongVoteForm
    _l_(445184)
    context = {}
    _l_(445185)

    def get_success_url(self,**kwargs):
        _l_(445195)

        song_id = _c_(445189, _a_(445188, _a_(445187, _n_(445186, "self", lambda: self), "kwargs"), "get"), 'song_id')
        _l_(445190)
        aux = _c_(445193, _n_(445191, "reverse", lambda: reverse), 'music:song_detail', kwargs={'pk':_n_(445192, "song_id", lambda: song_id)})
        _l_(445194)
        return aux

    def post(self,request,pk=None,song_id=None):
        _l_(445238)

        user = _a_(445198, _a_(445197, _n_(445196, "self", lambda: self), "request"), "user")
        _l_(445199)
        song_obj = _c_(445204, _a_(445202, _a_(445201, _n_(445200, "Song", lambda: Song), "objects"), "get"), pk=_n_(445203, "song_id", lambda: song_id))
        _l_(445205)
        vote_obj,created = _c_(445211, _a_(445208, _a_(445207, _n_(445206, "Vote", lambda: Vote), "objects"), "get_or_create"), song = _n_(445209, "song_obj", lambda: song_obj),user = _n_(445210, "user", lambda: user)) 
        _l_(445212) 
        vote_form = _c_(445217, _n_(445213, "SongVoteForm", lambda: SongVoteForm), _a_(445215, _n_(445214, "request", lambda: request), "POST"), instance=_n_(445216, "vote_obj", lambda: vote_obj))
        _l_(445218)

        if _c_(445221, _a_(445220, _n_(445219, "vote_form", lambda: vote_form), "is_valid")):
            _l_(445237)

            new_vote = _c_(445224, _a_(445223, _n_(445222, "vote_form", lambda: vote_form), "save"), commit=False)
            _l_(445225)
            _n_(445226, "new_vote", lambda: new_vote).user = _a_(445229, _a_(445228, _n_(445227, "self", lambda: self), "request"), "user")
            _l_(445230)
            _c_(445233, _a_(445232, _n_(445231, "new_vote", lambda: new_vote), "save"))
            _l_(445234)
            aux = _n_(445235, "new_vote", lambda: new_vote)
            _l_(445236)
            return aux