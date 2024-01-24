# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60431962/django-attributeerror-when-trying-to-add-an-object-to-a-manytomanyfield
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class AddFriendRedirect(_n_(702785, "RedirectView", lambda: RedirectView)):
    _l_(702840)

    def get_redirect_url(self,*args,**kwargs):
        _l_(702839)

        username = _c_(702789, _a_(702788, _a_(702787, _n_(702786, "self", lambda: self), "kwargs"), "get"), "username")
        _l_(702790)
        obj = _c_(702794, _n_(702791, "get_object_or_404", lambda: get_object_or_404), _n_(702792, "UserProfileInfo", lambda: UserProfileInfo),slug=_n_(702793, "username", lambda: username))
        _l_(702795)
        url_ = _c_(702798, _a_(702797, _n_(702796, "obj", lambda: obj), "get_absolute_url"))
        _l_(702799)
        user = _a_(702802, _a_(702801, _n_(702800, "self", lambda: self), "request"), "user")
        _l_(702803)
        if _a_(702805, _n_(702804, "user", lambda: user), "is_authenticated"):
            _l_(702836)

            if _n_(702806, "user", lambda: user) in _c_(702810, _a_(702809, _a_(702808, _n_(702807, "obj", lambda: obj), "friends"), "all")):
                _l_(702835)

                _c_(702815, _a_(702813, _a_(702812, _n_(702811, "obj", lambda: obj), "friends"), "remove"), _n_(702814, "user", lambda: user))
                _l_(702816)
                _c_(702821, _a_(702819, _a_(702818, _n_(702817, "user", lambda: user), "friends"), "remove"), _n_(702820, "obj", lambda: obj)) # these are the fields causing the error
                _l_(702822) # these are the fields causing the error
            else:
                _c_(702827, _a_(702825, _a_(702824, _n_(702823, "obj", lambda: obj), "friends"), "add"), _n_(702826, "user", lambda: user))
                _l_(702828)
                _c_(702833, _a_(702831, _a_(702830, _n_(702829, "user", lambda: user), "friends"), "add"), _n_(702832, "obj", lambda: obj)) # these are the fields causing the error
                _l_(702834) # these are the fields causing the error
        aux = _n_(702837, "url_", lambda: url_)
        _l_(702838)
        return aux