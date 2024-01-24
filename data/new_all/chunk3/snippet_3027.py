# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53463416/django-attributeerror-int-object-has-no-attribute-save
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CreateEvent(_n_(557078, "IsVerifiedMixin", lambda: IsVerifiedMixin), _n_(557079, "CreateView", lambda: CreateView)):
    _l_(557134)

    model = Event
    _l_(557080)
    form_class = EventForm
    _l_(557081)
    template_name = 'event/event_form.html'
    _l_(557082)

    def form_valid(self, form, *args, **kwargs):
        _l_(557133)

        _n_(557083, "self", lambda: self).object = _c_(557086, _a_(557085, _n_(557084, "form", lambda: form), "save"), commit=False)
        _l_(557087)
        _a_(557089, _n_(557088, "self", lambda: self), "object").user = _a_(557092, _a_(557091, _n_(557090, "self", lambda: self), "request"), "user")
        _l_(557093)
        _c_(557100, _n_(557094, "print", lambda: print), _a_(557099, _a_(557098, _a_(557097, _a_(557096, _n_(557095, "self", lambda: self), "object"), "user"), "profile"), "total_events")) #This prints 0
        _l_(557101) #This prints 0
        _a_(557105, _a_(557104, _a_(557103, _n_(557102, "self", lambda: self), "object"), "user"), "profile").total_events += 1
        _l_(557106)
        _c_(557113, _n_(557107, "print", lambda: print), _a_(557112, _a_(557111, _a_(557110, _a_(557109, _n_(557108, "self", lambda: self), "object"), "user"), "profile"), "total_events")) # This prints 1
        _l_(557114) # This prints 1
        _c_(557121, _a_(557120, _a_(557119, _a_(557118, _a_(557117, _a_(557116, _n_(557115, "self", lambda: self), "object"), "user"), "profile"), "total_events"), "save")) # If I don't use this statement it does not save to database. But It gives me the above error
        _l_(557122) # If I don't use this statement it does not save to database. But It gives me the above error
        _c_(557126, _a_(557125, _a_(557124, _n_(557123, "self", lambda: self), "object"), "save"))
        _l_(557127)
        aux = _c_(557131, _a_(557129, _n_(557128, "super", lambda: super)(), "form_valid"), _n_(557130, "form", lambda: form))
        _l_(557132)
        return aux