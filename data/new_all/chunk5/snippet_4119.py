# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62757155/typeerror-field-id-expected-a-number-but-got-user
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(684099)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(684101)

except ImportError:
    pass
try:
    from django.db.models.signals import pre_save
    _l_(684103)

except ImportError:
    pass
try:
    from django.utils.text import slugify
    _l_(684105)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(684107)

except ImportError:
    pass
try:
    from django.db.models.signals import post_delete
    _l_(684109)

except ImportError:
    pass
try:
    from django.dispatch import receiver
    _l_(684111)

except ImportError:
    pass
try:
    from PIL import Image
    _l_(684113)

except ImportError:
    pass

def upload_location(instance, filename, **kwargs):
    _l_(684129)

    file_path = _c_(684125, _a_(684114, 'blog/{author.id}/{title}-{filename}', "format"), author_id = _c_(684119, _n_(684115, "str", lambda: str), _a_(684118, _a_(684117, _n_(684116, "instance", lambda: instance), "author"), "id")), title=_c_(684123, _n_(684120, "str", lambda: str), _a_(684122, _n_(684121, "instance", lambda: instance), "title")), filename=_n_(684124, "filename", lambda: filename)
    )
    _l_(684126)
    aux = _n_(684127, "file_path", lambda: file_path)
    _l_(684128)
    return aux

class BlogPost(_a_(684131, _n_(684130, "models", lambda: models), "Model")):
    _l_(684169)

    title           = _c_(684134, _a_(684133, _n_(684132, "models", lambda: models), "CharField"), max_length=50, null=False, blank=False)
    _l_(684135)
    description     = _c_(684138, _a_(684137, _n_(684136, "models", lambda: models), "CharField"), max_length=500, null=False, blank=False)
    _l_(684139)
    image           = _c_(684143, _a_(684141, _n_(684140, "models", lambda: models), "ImageField"), upload_to=_n_(684142, "upload_location", lambda: upload_location), null=False, blank=False)
    _l_(684144)
    date_published  = _c_(684147, _a_(684146, _n_(684145, "models", lambda: models), "DateTimeField"), auto_now_add=True, verbose_name="date published")
    _l_(684148)
    date_updated    = _c_(684151, _a_(684150, _n_(684149, "models", lambda: models), "DateTimeField"), auto_now=True, verbose_name="date updated")
    _l_(684152)
    author          = _c_(684159, _a_(684154, _n_(684153, "models", lambda: models), "ForeignKey"), _a_(684156, _n_(684155, "settings", lambda: settings), "AUTH_USER_MODEL"), on_delete=_a_(684158, _n_(684157, "models", lambda: models), "CASCADE"))
    _l_(684160)
    slug            = _c_(684163, _a_(684162, _n_(684161, "models", lambda: models), "SlugField"), blank=True, unique=True)
    _l_(684164)

    def __str__(self):
        _l_(684168)

        aux = _a_(684166, _n_(684165, "self", lambda: self), "title")
        _l_(684167)
        return aux

@_c_(684173, _n_(684170, "receiver", lambda: receiver), _n_(684171, "post_delete", lambda: post_delete), sender=_n_(684172, "BlogPost", lambda: BlogPost))
def submission_delete(sender, instance, **kwargs):
    _l_(684179)

    _c_(684177, _a_(684176, _a_(684175, _n_(684174, "instance", lambda: instance), "image"), "delete"), False)
    _l_(684178)

def pre_save_blog_post_reciever(sender, instance, *args, **kwargs):
    _l_(684192)

    if not _a_(684181, _n_(684180, "instance", lambda: instance), "slug"):
        _l_(684191)

        _n_(684182, "instance", lambda: instance).slug = _c_(684189, _n_(684183, "slugify", lambda: slugify), _a_(684186, _a_(684185, _n_(684184, "instance", lambda: instance), "author"), "username") + "-" + _a_(684188, _n_(684187, "instance", lambda: instance), "title"))
        _l_(684190)

_c_(684197, _a_(684194, _n_(684193, "pre_save", lambda: pre_save), "connect"), _n_(684195, "pre_save_blog_post_reciever", lambda: pre_save_blog_post_reciever), sender=_n_(684196, "BlogPost", lambda: BlogPost))
_l_(684198)