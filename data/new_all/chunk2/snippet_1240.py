# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(452516)

except ImportError:
    pass

class BookNumber(_a_(452518, _n_(452517, "models", lambda: models), "Model")):
    _l_(452527)

    isbn_10=_c_(452521, _a_(452520, _n_(452519, "models", lambda: models), "CharField"), max_length=10,blank=True)
    _l_(452522)
    isbn_30=_c_(452525, _a_(452524, _n_(452523, "models", lambda: models), "CharField"), max_length=12,blank=True)
    _l_(452526)


# Create your models here.
class Book(_a_(452529, _n_(452528, "models", lambda: models), "Model")):
    _l_(452569)

    title=_c_(452532, _a_(452531, _n_(452530, "models", lambda: models), "CharField"), max_length=32)
    _l_(452533)
    author=_c_(452536, _a_(452535, _n_(452534, "models", lambda: models), "CharField"), max_length=30)
    _l_(452537)
    is_publise=_c_(452540, _a_(452539, _n_(452538, "models", lambda: models), "BooleanField"), default=False)
    _l_(452541)
    publise_date=_c_(452544, _a_(452543, _n_(452542, "models", lambda: models), "DateField"), auto_now_add=False,auto_now=False,blank=True)
    _l_(452545)
    upload_time=_c_(452548, _a_(452547, _n_(452546, "models", lambda: models), "DateField"), auto_now_add=True,auto_now=False)#consider the current time.
    _l_(452549)#consider the current time.
    front_page=_c_(452552, _a_(452551, _n_(452550, "models", lambda: models), "FileField"), upload_to="content_folder/",default="")
    _l_(452553)
    end_page_image=_c_(452556, _a_(452555, _n_(452554, "models", lambda: models), "ImageField"), upload_to="Image_folder/",blank=True)
    _l_(452557)
    number=_c_(452563, _a_(452559, _n_(452558, "models", lambda: models), "OneToOneField"), _n_(452560, "BookNumber", lambda: BookNumber),null=True,blank=True,on_delete=_a_(452562, _n_(452561, "models", lambda: models), "CASCADE"))#This line means only 1 isbn_10 & isbn_30 number will be assigned to one number in
    _l_(452564)#This line means only 1 isbn_10 & isbn_30 number will be assigned to one number in

    def __str__(self):
        _l_(452568)

        aux = _a_(452566, _n_(452565, "self", lambda: self), "title")
        _l_(452567)
        return aux