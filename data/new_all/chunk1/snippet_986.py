# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59066080/attributeerror-module-django-contrib-auth-has-no-attribute-models-what-am
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def calicutpara(request):
    _l_(396217)

    aux = _c_(396215, _n_(396213, "render", lambda: render), _n_(396214, "request", lambda: request), 'calicutpara.html')
    _l_(396216)
    return aux

class signup(_n_(396218, "CreateView", lambda: CreateView)):
    _l_(396224)

    form_class = _a_(396219, forms, "userCreateForm")
    _l_(396220)
    success_url = _c_(396221, reverse_lazy, 'login')
    _l_(396222)
    template_name = 'signup.html'
    _l_(396223)