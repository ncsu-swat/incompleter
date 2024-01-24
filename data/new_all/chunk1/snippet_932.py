# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25491328/typeerror-when-creating-a-wtform-with-mongoengine-and-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(407108, _a_(407107, _n_(407106, "app", lambda: app), "route"), '/blog/new')
def new():
    _l_(407117)

    form = _c_(407111, _n_(407109, "model_form", lambda: model_form), _n_(407110, "Post", lambda: Post))
    _l_(407112)
    aux = _c_(407115, _n_(407113, "render_template", lambda: render_template), 'new_blog.html', form=_n_(407114, "form", lambda: form))
    _l_(407116)
    return aux