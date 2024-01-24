# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55150153/typeerror-at-myapp-beds
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BedsView(_n_(358799, "View", lambda: View)):
    _l_(358887)

    def get_user_details(self, username, mat_number):
        _l_(358832)

        try:
            _l_(358812)

            user = _c_(358804, _a_(358802, _a_(358801, _n_(358800, "User", lambda: User), "objects"), "get"), username=_n_(358803, "username", lambda: username))
            _l_(358805)
        except _a_(358807, _n_(358806, "User", lambda: User), "DoesNotExist"):
            _l_(358811)

            aux = _c_(358809, _n_(358808, "redirect", lambda: redirect), 'index') 
            _l_(358810) 
            return aux 
        userbeds = _c_(358821, _a_(358819, _c_(358818, _a_(358815, _a_(358814, _n_(358813, "Userbed", lambda: Userbed), "objects"), "filter"), user=_n_(358816, "user", lambda: user), mat_number=_n_(358817, "mat_number", lambda: mat_number)), "order_by"), -_n_(358820, "posted_date", lambda: posted_date))[0]
        _l_(358822)
        form = _c_(358826, _n_(358823, "UserBedsForm", lambda: UserBedsForm), {'mat_number':_a_(358825, _n_(358824, "userbeds", lambda: userbeds), "mat_number")})
        _l_(358827)
        aux = (_n_(358828, "user", lambda: user), _n_(358829, "userbeds", lambda: userbeds),_n_(358830, "form", lambda: form))
        _l_(358831)
        return aux

    @_c_(358833, method_decorator, login_required)
    def get(self, request, username, mat_number):
        _l_(358847)

        (user,userbeds,form) = _c_(358838, _a_(358835, _n_(358834, "self", lambda: self), "get_user_details"), _n_(358836, "username", lambda: username), _n_(358837, "mat_number", lambda: mat_number))
        _l_(358839)
        aux = _c_(358845, _n_(358840, "render", lambda: render), _n_(358841, "request", lambda: request), 'myapp/beds.html', {'userbeds':_n_(358842, "userbeds", lambda: userbeds), 'selecteduser':_n_(358843, "user", lambda: user), 'form':_n_(358844, "form", lambda: form)})
        _l_(358846)
        return aux

    @_c_(358848, method_decorator, login_required)
    def post(self, request, username):
        _l_(358886)

        (user, userbeds, form) = _c_(358853, _a_(358850, _n_(358849, "self", lambda: self), "get_user_details"), _n_(358851, "username", lambda: username), _n_(358852, "mat_number", lambda: mat_number))
        _l_(358854)
        form = _c_(358859, _n_(358855, "UserBedsForm", lambda: UserBedsForm), _a_(358857, _n_(358856, "request", lambda: request), "POST"), instance=_n_(358858, "userbeds", lambda: userbeds))
        _l_(358860)
        if _c_(358863, _a_(358862, _n_(358861, "form", lambda: form), "is_valid")):
            _l_(358878)

            _c_(358866, _a_(358865, _n_(358864, "form", lambda: form), "save"), commit=True)
            _l_(358867)
            aux = _c_(358871, _n_(358868, "redirect", lambda: redirect), 'beds', _a_(358870, _n_(358869, "user", lambda: user), "username"))
            _l_(358872)
            return aux
        else:
            _c_(358876, _n_(358873, "print", lambda: print), _a_(358875, _n_(358874, "form", lambda: form), "errors"))
            _l_(358877)
        aux = _c_(358884, _n_(358879, "render", lambda: render), _n_(358880, "request", lambda: request), 'myapp/beds.html', {'userbeds':_n_(358881, "userbeds", lambda: userbeds), 'selecteduser':_n_(358882, "user", lambda: user), 'form':_n_(358883, "form", lambda: form)})
        _l_(358885)
        return aux