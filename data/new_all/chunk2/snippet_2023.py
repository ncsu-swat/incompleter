# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68994258/django-typeerror-httpresponseforbidden-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render, get_object_or_404, redirect
    _l_(467586)

except ImportError:
    pass
try:
    from django.contrib.auth import authenticate
    _l_(467588)

except ImportError:
    pass
try:
    from django.http import request, HttpResponse
    _l_(467590)

except ImportError:
    pass
try:
    from django.contrib import messages
    _l_(467592)

except ImportError:
    pass
try:
    from .forms import *
    _l_(467594)

except ImportError:
    pass
try:
    from .models import *
    _l_(467596)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(467598)

except ImportError:
    pass
try:
    from django.contrib.auth.decorators import login_required
    _l_(467600)

except ImportError:
    pass

# Create your views here.
def register(request):
    _l_(467633)

    if _a_(467602, _n_(467601, "request", lambda: request), "method") == 'POST':
        _l_(467627)

        form = _c_(467606, _n_(467603, "CompRegisterForm", lambda: CompRegisterForm), _a_(467605, _n_(467604, "request", lambda: request), "POST"))
        _l_(467607)
        if _c_(467610, _a_(467609, _n_(467608, "form", lambda: form), "is_valid")):
            _l_(467623)

            _c_(467613, _a_(467612, _n_(467611, "form", lambda: form), "save"))
            _l_(467614)
            username = _c_(467618, _a_(467617, _a_(467616, _n_(467615, "form", lambda: form), "cleaned_data"), "get"), 'username')
            _l_(467619)
            aux = _c_(467621, _n_(467620, "redirect", lambda: redirect), 'Login')
            _l_(467622)
            return aux
    else:
        form = _c_(467625, _n_(467624, "CompRegisterForm", lambda: CompRegisterForm))
        _l_(467626)
    aux = _c_(467631, _n_(467628, "render", lambda: render), _n_(467629, "request", lambda: request), 'Users/register.html', {'form': _n_(467630, "form", lambda: form)})
    _l_(467632)
    return aux


@_n_(467634, "login_required", lambda: login_required)
def profile(request):
    _l_(467697)

    if _a_(467636, _n_(467635, "request", lambda: request), "method") == 'POST':
        _l_(467688)

        u_form = _c_(467642, _n_(467637, "CompUpdateForm", lambda: CompUpdateForm), _a_(467639, _n_(467638, "request", lambda: request), "POST"), instance=_a_(467641, _n_(467640, "request", lambda: request), "user"))
        _l_(467643)
        p_form = _c_(467652, _n_(467644, "ProfilePicForm", lambda: ProfilePicForm), _a_(467646, _n_(467645, "request", lambda: request), "POST"),
                                _a_(467648, _n_(467647, "request", lambda: request), "FILES"),
                                instance=_a_(467651, _a_(467650, _n_(467649, "request", lambda: request), "user"), "profile"))
        _l_(467653)
        if _c_(467656, _a_(467655, _n_(467654, "u_form", lambda: u_form), "is_valid")) and _c_(467659, _a_(467658, _n_(467657, "p_form", lambda: p_form), "is_valid")):
            _l_(467676)

            _c_(467662, _a_(467661, _n_(467660, "u_form", lambda: u_form), "save"))
            _l_(467663)
            _c_(467666, _a_(467665, _n_(467664, "p_form", lambda: p_form), "save"))
            _l_(467667)
            _c_(467671, _a_(467669, _n_(467668, "messages", lambda: messages), "success"), _n_(467670, "request", lambda: request), f'Your account has been updated!')
            _l_(467672)
            aux = _c_(467674, _n_(467673, 'redirect', lambda: redirect), 'Profile_Page')
            _l_(467675)
            return aux

    else:
        u_form = _c_(467680, _n_(467677, 'CompUpdateForm', lambda: CompUpdateForm), instance=_a_(467679, _n_(467678, 'request', lambda: request), 'user'))
        _l_(467681)
        p_form = _c_(467686, _n_(467682, 'ProfilePicForm', lambda: ProfilePicForm), instance=_a_(467685, _a_(467684, _n_(467683, 'request', lambda: request), 'user'), 'profile'))
        _l_(467687)

    context = {
        'u_form': _n_(467689, 'u_form', lambda: u_form),
        'p_form': _n_(467690, 'p_form', lambda: p_form)
    }
    _l_(467691)
    aux = _c_(467695, _n_(467692, 'render', lambda: render), _n_(467693, 'request', lambda: request), 'Users/profile.html', _n_(467694, 'context', lambda: context))
    _l_(467696)

    return aux