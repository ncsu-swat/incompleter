# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54055170/filenotfounderror-errno-2-no-such-file-or-directory-after-resizing-the-images
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Profile(_a_(466198, _n_(466197, "models", lambda: models), "Model")):
    _l_(466268)

    user = _c_(466201, _a_(466199, models, "OneToOneField"), User, on_delete=_a_(466200, models, "CASCADE"))        
    _l_(466202)        
    profile_image = _c_(466204, _a_(466203, models, "ImageField"), upload_to='profile_images/', default='', blank=True, null=True)
    _l_(466205)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        _l_(466267)

        im = _c_(466210, _a_(466207, _n_(466206, "Image", lambda: Image), "open"), _a_(466209, _n_(466208, "self", lambda: self), "profile_image"))
        _l_(466211)
        output = _c_(466213, _n_(466212, "BytesIO", lambda: BytesIO))
        _l_(466214)
        basewidth = 300
        _l_(466215)
        wpercent = (_n_(466216, "basewidth", lambda: basewidth)/_c_(466220, _n_(466217, "float", lambda: float), _a_(466219, _n_(466218, "im", lambda: im), "size")[0]))
        _l_(466221)
        hsize = _c_(466230, _n_(466222, "int", lambda: int), (_c_(466226, _n_(466223, "float", lambda: float), _a_(466225, _n_(466224, "img", lambda: img), "size")[1])*_c_(466229, _n_(466227, "float", lambda: float), _n_(466228, "wpercent", lambda: wpercent))))
        _l_(466231)
        im = _c_(466236, _a_(466233, _n_(466232, "im", lambda: im), "resize"), (_n_(466234, "basewidth", lambda: basewidth), _n_(466235, "hsize", lambda: hsize)))
        _l_(466237)
        _c_(466241, _a_(466239, _n_(466238, "im", lambda: im), "save"), _n_(466240, "output", lambda: output), format='JPEG', quality=100)
        _l_(466242)
        _c_(466245, _a_(466244, _n_(466243, "output", lambda: output), "seek"), 0)
        _l_(466246)
        _n_(466247, "self", lambda: self).profile_image = _c_(466259, _n_(466248, "InMemoryUploadedFile", lambda: InMemoryUploadedFile), _n_(466249, "output", lambda: output), 'ImageField', "%s.jpg" % _c_(466254, _a_(466253, _a_(466252, _a_(466251, _n_(466250, "self", lambda: self), "profile_image"), "name"), "split"), '.')[0], 'image/jpeg',
                                        _c_(466258, _a_(466256, _n_(466255, "sys", lambda: sys), "getsizeof"), _n_(466257, "output", lambda: output)), None)
        _l_(466260)

        _c_(466265, _a_(466264, _n_(466261, "super", lambda: super)(_n_(466262, "Profile", lambda: Profile), _n_(466263, "self", lambda: self)), "save"))
        _l_(466266)