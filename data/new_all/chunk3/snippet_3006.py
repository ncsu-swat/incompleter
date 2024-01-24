# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54966674/python-typeerror-object-of-type-user-is-not-json-serializable-after-upgrading
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TagView(_n_(566604, "LoginRequiredMixin", lambda: LoginRequiredMixin), _a_(566606, _n_(566605, "generic", lambda: generic), "CreateView")):
    _l_(566699)

    form_class = _a_(566607, forms, "TagForm")
    _l_(566608)

    def post(self, request, *args, **kwargs):
        _l_(566698)

        try:
            _l_(566697)

            post_data = _c_(566612, _a_(566611, _a_(566610, _n_(566609, "request", lambda: request), "POST"), "copy"))
            _l_(566613)
            _c_(566619, _a_(566615, _n_(566614, "post_data", lambda: post_data), "update"), {'user': _a_(566618, _a_(566617, _n_(566616, "request", lambda: request), "user"), "pk")})
            _l_(566620)
            _c_(566624, _n_(566621, "print", lambda: print), _a_(566623, _n_(566622, "post_data", lambda: post_data), "values"))
            _l_(566625)
            form = _c_(566629, _a_(566627, _n_(566626, "forms", lambda: forms), "TagForm"), _n_(566628, "post_data", lambda: post_data))
            _l_(566630)
            if _c_(566633, _a_(566632, _n_(566631, "form", lambda: form), "is_valid")):
                _l_(566671)

                tag = _c_(566636, _a_(566635, _n_(566634, "form", lambda: form), "save"), commit=False)
                _l_(566637)
                _n_(566638, "tag", lambda: tag).user = _a_(566640, _n_(566639, "request", lambda: request), "user")
                _l_(566641)
                _n_(566642, "tag", lambda: tag).email = _a_(566645, _a_(566644, _n_(566643, "request", lambda: request), "user"), "email")
                _l_(566646)
                _c_(566649, _a_(566648, _n_(566647, "tag", lambda: tag), "save"))
                _l_(566650)
                _a_(566652, _n_(566651, "request", lambda: request), "session")['user'] = _a_(566654, _n_(566653, "tag", lambda: tag), "user")
                _l_(566655)
                _a_(566657, _n_(566656, "request", lambda: request), "session")['email'] = _a_(566659, _n_(566658, "tag", lambda: tag), "email")
                _l_(566660)
            else:
                _c_(566664, _n_(566661, "print", lambda: print), _a_(566663, _n_(566662, "form", lambda: form), "errors"))
                _l_(566665)
                aux = _c_(566669, _n_(566666, "HttpResponse", lambda: HttpResponse), _a_(566668, _n_(566667, "form", lambda: form), "errors"), status=400)
                _l_(566670)
                return aux

            _c_(566673, _n_(566672, "print", lambda: print), 'going to redirect after successful tagging.')
            _l_(566674)
            aux = _c_(566678, _n_(566675, "HttpResponseRedirect", lambda: HttpResponseRedirect), _c_(566677, _n_(566676, "reverse", lambda: reverse), 'users:dashboard'))
            _l_(566679)
            return aux

        except _n_(566680, "Exception", lambda: Exception) as exp:
            _l_(566696)

            _c_(566684, _a_(566682, _n_(566681, "logging", lambda: logging), "error"), _n_(566683, "exp", lambda: exp))
            _l_(566685)
            _c_(566690, _n_(566686, "print", lambda: print), _c_(566689, _a_(566687, 'error is: {}', "format"), _n_(566688, "exp", lambda: exp)))
            _l_(566691)
            aux = _c_(566694, _n_(566692, "HttpResponse", lambda: HttpResponse), _n_(566693, "exp", lambda: exp), status=400)
            _l_(566695)
            return aux