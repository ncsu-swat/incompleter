# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59939620/attributeerror-postdetailview-object-has-no-attribute-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Post(_a_(698759, _n_(698758, "models", lambda: models), "Model")):
    _l_(698783)

    title = _c_(698761, _a_(698760, models, "CharField"), max_length=20)
    _l_(698762)
    content =  _c_(698764, _a_(698763, models, "TextField"))
    _l_(698765)
    date_posted = _c_(698767, _a_(698766, models, "DateTimeField"))
    _l_(698768)
    author = _c_(698771, _a_(698769, models, "ForeignKey"), User, on_delete=_a_(698770, models, "CASCADE"))
    _l_(698772)


    def __str__(self):
        _l_(698776)

        aux = _a_(698774, _n_(698773, "self", lambda: self), "title") 
        _l_(698775) 
        return aux 

    def get_absolute_url(self):
        _l_(698782)

        aux = _c_(698780, _n_(698777, "reverse", lambda: reverse), 'post-detail', kwargs={'pk':_a_(698779, _n_(698778, "self", lambda: self), "pk")})
        _l_(698781)
        return aux


class Comment(_a_(698785, _n_(698784, "models", lambda: models), "Model")):
    _l_(698806)

    post = _c_(698789, _a_(698786, models, "ForeignKey"), _n_(698787, "Post", lambda: Post),on_delete=_a_(698788, models, "CASCADE"),related_name='comments')
    _l_(698790)
    name = _c_(698792, _a_(698791, models, "CharField"), max_length=80)
    _l_(698793)
    email = _c_(698795, _a_(698794, models, "EmailField"))
    _l_(698796)
    body = _c_(698798, _a_(698797, models, "TextField"))
    _l_(698799)
    created_on = _c_(698801, _a_(698800, models, "DateTimeField"), auto_now_add=True)
    _l_(698802)
    active = _c_(698804, _a_(698803, models, "BooleanField"), default=False)
    _l_(698805)