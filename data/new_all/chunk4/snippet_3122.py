# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43557978/getting-error-as-typeerror-at-add-follow-1-init-takes-1-positional-argu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib.auth.decorators import login_required
    _l_(612970)

except ImportError:
    pass
try:
    from django.shortcuts import render
    _l_(612972)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(612974)

except ImportError:
    pass
try:
    from django.core.files.storage import FileSystemStorage
    _l_(612976)

except ImportError:
    pass
try:
    from django.core.urlresolvers import reverse
    _l_(612978)

except ImportError:
    pass
try:
    from django.shortcuts import render, get_object_or_404
    _l_(612980)

except ImportError:
    pass
try:
    from .forms import AlbumForm
    _l_(612982)

except ImportError:
    pass
try:
    from .models import Album
    _l_(612984)

except ImportError:
    pass
try:
    from django.http import HttpResponse,HttpResponseForbidden
    _l_(612986)

except ImportError:
    pass

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
_l_(612987)

# Create your views here.
def home(request):
    _l_(612996)

    context = {}
    _l_(612988)
    template = 'home.html'
    _l_(612989)
    aux = _c_(612994, _n_(612990, "render", lambda: render), _n_(612991, "request", lambda: request), _n_(612992, "template", lambda: template), _n_(612993, "context", lambda: context))
    _l_(612995)
    return aux

def about(request):
    _l_(613005)

    context = {}
    _l_(612997)
    template = 'about.html'
    _l_(612998)
    aux = _c_(613003, _n_(612999, "render", lambda: render), _n_(613000, "request", lambda: request), _n_(613001, "template", lambda: template), _n_(613002, "context", lambda: context))
    _l_(613004)
    return aux

@_c_(613007, _n_(613006, "login_required", lambda: login_required))
def userProfile(request):
    _l_(613020)

    user = _a_(613009, _n_(613008, "request", lambda: request), "user")
    _l_(613010)
    context = {'user': _n_(613011, "user", lambda: user)}
    _l_(613012)
    template = 'profile.html'
    _l_(613013)
    aux = _c_(613018, _n_(613014, "render", lambda: render), _n_(613015, "request", lambda: request), _n_(613016, "template", lambda: template), _n_(613017, "context", lambda: context))
    _l_(613019)
    return aux



def create_form(request):
    _l_(613081)

    form = _c_(613026, _n_(613021, "AlbumForm", lambda: AlbumForm), _a_(613023, _n_(613022, "request", lambda: request), "POST") or None, _a_(613025, _n_(613024, "request", lambda: request), "FILES") or None)
    _l_(613027)
    if _c_(613030, _a_(613029, _n_(613028, "form", lambda: form), "is_valid")):
        _l_(613073)

        album = _c_(613033, _a_(613032, _n_(613031, "form", lambda: form), "save"), commit=False)
        _l_(613034)
        _n_(613035, "album", lambda: album).user = _a_(613037, _n_(613036, "request", lambda: request), "user")
        _l_(613038)
        _n_(613039, "album", lambda: album).image= _a_(613041, _n_(613040, "request", lambda: request), "FILES")['image']
        _l_(613042)
        file_type = _c_(613047, _a_(613046, _a_(613045, _a_(613044, _n_(613043, "album", lambda: album), "image"), "url"), "split"), '.')[-1]
        _l_(613048)
        file_type = _c_(613051, _a_(613050, _n_(613049, "file_type", lambda: file_type), "lower"))
        _l_(613052)
        if _n_(613053, "file_type", lambda: file_type) not in _n_(613054, "IMAGE_FILE_TYPES", lambda: IMAGE_FILE_TYPES):
            _l_(613063)

            context = {
                'album': _n_(613055, "album", lambda: album),
                'form': _n_(613056, "form", lambda: form),
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            _l_(613057)
            aux = _c_(613061, _n_(613058, "render", lambda: render), _n_(613059, "request", lambda: request), 'detail.html', _n_(613060, "context", lambda: context))
            _l_(613062)
            return aux
        _c_(613066, _a_(613065, _n_(613064, "album", lambda: album), "save"))
        _l_(613067)
        aux = _c_(613071, _n_(613068, "render", lambda: render), _n_(613069, "request", lambda: request), 'create_form.html', {'album': _n_(613070, "album", lambda: album)})
        _l_(613072)
        return aux
    context = {
        "form": _n_(613074, "form", lambda: form),
    }
    _l_(613075)
    aux = _c_(613079, _n_(613076, "render", lambda: render), _n_(613077, "request", lambda: request), 'create_form.html', _n_(613078, "context", lambda: context))
    _l_(613080)
    return aux

def detail(request):
    _l_(613090)

    user = _a_(613083, _n_(613082, "request", lambda: request), "user")
    _l_(613084)
    aux = _c_(613088, _n_(613085, "render", lambda: render), _n_(613086, "request", lambda: request), 'detail.html', {'user': _n_(613087, "user", lambda: user)})
    _l_(613089)
    #album = get_object_or_404(Album, pk=id)
    return aux
try:
    from django.shortcuts import render, redirect
    _l_(613092)

except ImportError:
    pass
try:
    from .models import Album
    _l_(613094)

except ImportError:
    pass
try:
    from django.views.generic import TemplateView,View
    _l_(613096)

except ImportError:
    pass
try:
    from django.db.models import Q
    _l_(613098)

except ImportError:
    pass
try:
    from django.core.urlresolvers import reverse
    _l_(613100)

except ImportError:
    pass
try:
    from . import models
    _l_(613102)

except ImportError:
    pass
try:
    from django.contrib.auth.models import Permission, User
    _l_(613104)

except ImportError:
    pass


class ListaFollow(_n_(613105, "TemplateView", lambda: TemplateView)):
    _l_(613152)

    template_name = 'lista_follow.html'
    _l_(613106)
    def get_context_data(self,**kwargs):
        _l_(613151)

        context = _c_(613112, _a_(613110, _n_(613107, "super", lambda: super)(_n_(613108, "ListaFollow", lambda: ListaFollow),_n_(613109, "self", lambda: self)), "get_context_data"), **_n_(613111, "kwargs", lambda: kwargs))
        _l_(613113)
        _n_(613114, "context", lambda: context)['all'] = _c_(613118, _a_(613117, _a_(613116, _n_(613115, "Album", lambda: Album), "objects"), "all"))
        _l_(613119)
        _n_(613120, "context", lambda: context)['me'] = _c_(613127, _a_(613123, _a_(613122, _n_(613121, "User", lambda: User), "objects"), "get"), user=_a_(613126, _a_(613125, _n_(613124, "self", lambda: self), "request"), "user"))
        _l_(613128)
        _n_(613129, "context", lambda: context)['notme'] = _c_(613136, _a_(613132, _a_(613131, _n_(613130, "Album", lambda: Album), "objects"), "filter"), follow__user=_a_(613135, _a_(613134, _n_(613133, "self", lambda: self), "request"), "user"))
        _l_(613137)
        _n_(613138, "context", lambda: context)['notfollow'] = _c_(613147, _a_(613141, _a_(613140, _n_(613139, "Album", lambda: Album), "objects"), "filter"), ~_c_(613146, _n_(613142, "Q", lambda: Q), follow__user=_a_(613145, _a_(613144, _n_(613143, "self", lambda: self), "request"), "user")))
        _l_(613148)
        aux = _n_(613149, "context", lambda: context)
        _l_(613150)
        return aux

class AddFollow(_n_(613153, "View", lambda: View)):
    _l_(613181)

    def get(self,request, id):
        _l_(613180)

        me=_c_(613160, _a_(613157, _a_(613156, _a_(613155, _n_(613154, "models", lambda: models), "Album"), "objects"), "get"), user=_a_(613159, _n_(613158, "request", lambda: request), "user"))
        _l_(613161)
        followed = _c_(613167, _a_(613165, _a_(613164, _a_(613163, _n_(613162, "models", lambda: models), "Album"), "objects"), "get"), id=_n_(613166, "id", lambda: id)) #el wey
        _l_(613168) #el wey
        _c_(613173, _a_(613171, _a_(613170, _n_(613169, "me", lambda: me), "follow"), "add"), _n_(613172, "followed", lambda: followed))
        _l_(613174)
        aux = _c_(613178, _n_(613175, "redirect", lambda: redirect), _c_(613177, _n_(613176, "reverse", lambda: reverse), 'imagec/about.html'))
        _l_(613179)
        return aux

class RemoveFollow(_n_(613182, "View", lambda: View)):
    _l_(613210)

    def get(self,request, id):
        _l_(613209)

        me=_c_(613189, _a_(613186, _a_(613185, _a_(613184, _n_(613183, "models", lambda: models), "Album"), "objects"), "get"), user=_a_(613188, _n_(613187, "request", lambda: request), "user")) #instancia del usuario con el id que quiero crear
        _l_(613190) #instancia del usuario con el id que quiero crear
        followed = _c_(613196, _a_(613194, _a_(613193, _a_(613192, _n_(613191, "models", lambda: models), "Album"), "objects"), "get"), id=_n_(613195, "id", lambda: id))
        _l_(613197)
        _c_(613202, _a_(613200, _a_(613199, _n_(613198, "me", lambda: me), "follow"), "remove"), _n_(613201, "followed", lambda: followed)) #creo el usuario con mi nombre y la relacion
        _l_(613203) #creo el usuario con mi nombre y la relacion
        aux = _c_(613207, _n_(613204, "redirect", lambda: redirect), _c_(613206, _n_(613205, "reverse", lambda: reverse), 'imagec/about.html'))
        _l_(613208)
        return aux