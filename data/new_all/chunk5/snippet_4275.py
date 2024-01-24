# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60431962/django-attributeerror-when-trying-to-add-an-object-to-a-manytomanyfield
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AddFriendRedirect(_n_(697897, "RedirectView", lambda: RedirectView)):
    _l_(697952)

    def get_redirect_url(self,*args,**kwargs):
        _l_(697951)

        username = _c_(697901, _a_(697900, _a_(697899, _n_(697898, "self", lambda: self), "kwargs"), "get"), "username")
        _l_(697902)
        obj = _c_(697906, _n_(697903, "get_object_or_404", lambda: get_object_or_404), _n_(697904, "UserProfileInfo", lambda: UserProfileInfo),slug=_n_(697905, "username", lambda: username))
        _l_(697907)
        url_ = _c_(697910, _a_(697909, _n_(697908, "obj", lambda: obj), "get_absolute_url"))
        _l_(697911)
        user = _a_(697914, _a_(697913, _n_(697912, "self", lambda: self), "request"), "user")
        _l_(697915)
        if _a_(697917, _n_(697916, "user", lambda: user), "is_authenticated"):
            _l_(697948)

            if _n_(697918, "user", lambda: user) in _c_(697922, _a_(697921, _a_(697920, _n_(697919, "obj", lambda: obj), "friends"), "all")):
                _l_(697947)

                _c_(697927, _a_(697925, _a_(697924, _n_(697923, "obj", lambda: obj), "friends"), "remove"), _n_(697926, "user", lambda: user))
                _l_(697928)
                _c_(697933, _a_(697931, _a_(697930, _n_(697929, "user", lambda: user), "friends"), "remove"), _n_(697932, "obj", lambda: obj)) # these are the fields causing the error
                _l_(697934) # these are the fields causing the error
            else:
                _c_(697939, _a_(697937, _a_(697936, _n_(697935, "obj", lambda: obj), "friends"), "add"), _n_(697938, "user", lambda: user))
                _l_(697940)
                _c_(697945, _a_(697943, _a_(697942, _n_(697941, "user", lambda: user), "friends"), "add"), _n_(697944, "obj", lambda: obj)) # these are the fields causing the error
                _l_(697946) # these are the fields causing the error
        aux = _n_(697949, "url_", lambda: url_)
        _l_(697950)
        return aux