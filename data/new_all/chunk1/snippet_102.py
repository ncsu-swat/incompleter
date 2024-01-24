# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30032078/typeerror-init-takes-1-positional-argument-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from app import app, db
    _l_(381545)

except ImportError:
    pass
try:
    from flask import render_template, request, url_for
    _l_(381547)

except ImportError:
    pass
try:
    from forms import CreateForm
    _l_(381549)

except ImportError:
    pass
try:
    from models import Post
    _l_(381551)

except ImportError:
    pass


@_c_(381554, _a_(381553, _n_(381552, "app", lambda: app), "route"), '/')
def homepage():
    _l_(381558)

    aux = _c_(381556, _n_(381555, "render_template", lambda: render_template), 'base.html')
    _l_(381557)
    return aux


@_c_(381561, _a_(381560, _n_(381559, "app", lambda: app), "route"), '/create', methods=['GET', 'POST'])
def create():
    _l_(381604)

    form = _c_(381563, _n_(381562, "CreateForm", lambda: CreateForm), csrf_enabled=False)
    _l_(381564)
    if _a_(381566, _n_(381565, "request", lambda: request), "method") == 'GET':
        _l_(381571)

        aux = _c_(381569, _n_(381567, "render_template", lambda: render_template), 'create.html', form=_n_(381568, "form", lambda: form))
        _l_(381570)
        return aux
    if _a_(381573, _n_(381572, "request", lambda: request), "method") == 'POST':
        _l_(381598)

        if _c_(381576, _a_(381575, _n_(381574, "form", lambda: form), "validate_on_submit")):
            _l_(381597)

            create_post = _c_(381584, _n_(381577, "Post", lambda: Post), _a_(381580, _a_(381579, _n_(381578, "form", lambda: form), "title"), "data"), _a_(381583, _a_(381582, _n_(381581, "form", lambda: form), "text"), "data"))
            _l_(381585)
            _c_(381590, _a_(381588, _a_(381587, _n_(381586, "db", lambda: db), "session"), "add"), _n_(381589, "create_post", lambda: create_post))
            _l_(381591)
            _c_(381595, _a_(381594, _a_(381593, _n_(381592, "db", lambda: db), "session"), "commit"))
            _l_(381596)
    aux = _c_(381602, _n_(381599, "redirect", lambda: redirect), _c_(381601, _n_(381600, "url_for", lambda: url_for), 'homepage'))
    _l_(381603)
    return aux