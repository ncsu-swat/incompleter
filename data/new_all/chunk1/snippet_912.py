# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42956867/attributeerror-function-object-has-no-attribute-views
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(404511)

except ImportError:
    pass
try:
    from django.db.models import permalink
    _l_(404513)

except ImportError:
    pass

# Create your models here.

class Blog(_a_(404515, _n_(404514, "models", lambda: models), "Model")):
    _l_(404541)

    title = _c_(404518, _a_(404517, _n_(404516, "models", lambda: models), "CharField"), max_length = 100,unique = True)
    _l_(404519)
    slug = _c_(404522, _a_(404521, _n_(404520, "models", lambda: models), "CharField"), max_length = 100,unique = True)
    _l_(404523)
    body = _c_(404526, _a_(404525, _n_(404524, "models", lambda: models), "TextField"))
    _l_(404527)
    posted = _c_(404530, _a_(404529, _n_(404528, "models", lambda: models), "DateField"), db_index = True,auto_now_add = True)
    _l_(404531)

    def __unicode__(self):
        _l_(404535)

        aux = '%s' % _a_(404533, _n_(404532, "self", lambda: self), "title")
        _l_(404534)
        return aux

    @_n_(404536, "permalink", lambda: permalink)
    def get_absolute_url(self):
        _l_(404540)

        aux = ('view-blog-post',None, {'slug' : _a_(404538, _n_(404537, "self", lambda: self), "slug")})
        _l_(404539)
        return aux

class Category(_a_(404543, _n_(404542, "models", lambda: models), "Model")):
    _l_(404561)

    title = _c_(404546, _a_(404545, _n_(404544, "models", lambda: models), "CharField"), max_length = 100,db_index = True)
    _l_(404547)
    slug = _c_(404550, _a_(404549, _n_(404548, "models", lambda: models), "SlugField"), max_length = 100,db_index = True)
    _l_(404551)

    def __unicode__(self):
        _l_(404555)

        aux = '%s' % _a_(404553, _n_(404552, "self", lambda: self), "title")
        _l_(404554)
        return aux

    @_n_(404556, "permalink", lambda: permalink)
    def get_absolute_url(self):
        _l_(404560)

        aux = ('view_blog_category', None, { 'slug': _a_(404558, _n_(404557, "self", lambda: self), "slug") })
        _l_(404559)
        return aux