# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25491328/typeerror-when-creating-a-wtform-with-mongoengine-and-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(393804)

except ImportError:
    pass
try:
    from flask import Flask
    _l_(393806)

except ImportError:
    pass
try:
    from flask import render_template
    _l_(393808)

except ImportError:
    pass
try:
    from flask.ext.mongoengine import MongoEngine
    _l_(393810)

except ImportError:
    pass
try:
    from flask.ext.mongoengine.wtf import model_form
    _l_(393812)

except ImportError:
    pass
try:
    import mongoengine.base
    _l_(393814)

except ImportError:
    pass


app = _c_(393817, _n_(393815, "Flask", lambda: Flask), _n_(393816, "__name__", lambda: __name__))
_l_(393818)


_a_(393820, _n_(393819, "app", lambda: app), "config")['MONGODB_SETTINGS'] = {
    'db': 'davidystephenson',
    'host': 'ds059908.mongolab.com',
    'username': 'david',
    'password': 'opensecret',
    'port': 59908,
}
_l_(393821)
database = _c_(393824, _n_(393822, "MongoEngine", lambda: MongoEngine), _n_(393823, "app", lambda: app))
_l_(393825)


class Post(_a_(393827, _n_(393826, "database", lambda: database), "Document")):
    _l_(393862)

    author = _c_(393830, _a_(393829, _n_(393828, "database", lambda: database), "StringField"), default='David Y. Stephenson', max_length=255, required=True
    )
    _l_(393831)
    body = _c_(393834, _a_(393833, _n_(393832, "database", lambda: database), "StringField"), required=True)
    _l_(393835)
    comments = _c_(393841, _a_(393837, _n_(393836, "database", lambda: database), "ListField"), _c_(393840, _a_(393839, _n_(393838, "database", lambda: database), "EmbeddedDocumentField"), 'Comment')
    )
    _l_(393842)
    slug = _c_(393845, _a_(393844, _n_(393843, "database", lambda: database), "StringField"), max_length=255, required=True, unique=True)
    _l_(393846)
    tease = _c_(393849, _a_(393848, _n_(393847, "database", lambda: database), "StringField"), max_length=255, required=True)
    _l_(393850)
    time = _c_(393856, _a_(393852, _n_(393851, "database", lambda: database), "DateTimeField"), default=_a_(393855, _a_(393854, _n_(393853, "datetime", lambda: datetime), "datetime"), "now"), required=True
    )
    _l_(393857)
    title = _c_(393860, _a_(393859, _n_(393858, "database", lambda: database), "StringField"), max_length=255, required=True, unique=True)
    _l_(393861)


@_c_(393865, _a_(393864, _n_(393863, "app", lambda: app), "route"), '/')
def index():
    _l_(393869)

    aux = _c_(393867, _n_(393866, "render_template", lambda: render_template), 'index.html')
    _l_(393868)
    return aux


@_c_(393872, _a_(393871, _n_(393870, "app", lambda: app), "route"), '/blog/')
def blog():
    _l_(393882)

    posts = _c_(393876, _a_(393875, _a_(393874, _n_(393873, "Post", lambda: Post), "objects"), "all"))
    _l_(393877)
    aux = _c_(393880, _n_(393878, "render_template", lambda: render_template), 'blog.html', posts=_n_(393879, "posts", lambda: posts))
    _l_(393881)
    return aux


@_c_(393885, _a_(393884, _n_(393883, "app", lambda: app), "route"), '/blog/<slug>')
def post(slug):
    _l_(393896)

    post = _c_(393890, _a_(393888, _a_(393887, _n_(393886, "Post", lambda: Post), "objects"), "get"), slug=_n_(393889, "slug", lambda: slug))
    _l_(393891)
    aux = _c_(393894, _n_(393892, "render_template", lambda: render_template), 'post.html', post=_n_(393893, "post", lambda: post))
    _l_(393895)
    return aux


@_c_(393899, _a_(393898, _n_(393897, "app", lambda: app), "route"), '/blog/new')
def new():
    _l_(393928)

    _c_(393908, _a_(393902, _a_(393901, _n_(393900, "app", lambda: app), "logger"), "debug"), _c_(393907, _n_(393903, "isinstance", lambda: isinstance), _n_(393904, "Post", lambda: Post), _a_(393906, _a_(393905, mongoengine, "base"), "BaseDocument")))
    _l_(393909)
    _c_(393918, _a_(393912, _a_(393911, _n_(393910, "app", lambda: app), "logger"), "debug"), _c_(393917, _n_(393913, "isinstance", lambda: isinstance), _n_(393914, "Post", lambda: Post), _a_(393916, _a_(393915, mongoengine, "base"), "DocumentMetaclass")))
    _l_(393919)
    form = _c_(393922, _n_(393920, "model_form", lambda: model_form), _n_(393921, "Post", lambda: Post))
    _l_(393923)
    aux = _c_(393926, _n_(393924, "render_template", lambda: render_template), 'new_blog.html', form=_n_(393925, "form", lambda: form))
    _l_(393927)
    return aux

if _n_(393929, "__name__", lambda: __name__) == '__main__':
    _l_(393934)

    _c_(393932, _a_(393931, _n_(393930, "app", lambda: app), "run"), debug=True)
    _l_(393933)