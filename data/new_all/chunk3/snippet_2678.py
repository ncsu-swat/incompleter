# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67081201/django-throws-attributeerror-str-object-has-no-attribute-meta-when-i-regis
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db import models
    _l_(569333)

except ImportError:
    pass
try:
    from django.contrib.auth import get_user_model
    _l_(569335)

except ImportError:
    pass


class Post(_a_(569337, _n_(569336, "models", lambda: models), "Model")):
    _l_(569370)

    author = _c_(569344, _a_(569339, _n_(569338, "models", lambda: models), "ForeignKey"), _c_(569341, _n_(569340, "get_user_model", lambda: get_user_model)), on_delete=_a_(569343, _n_(569342, "models", lambda: models), "CASCADE"), verbose_name='Автор', related_name='posts', null=True)
    _l_(569345)
    title = _c_(569348, _a_(569347, _n_(569346, "models", lambda: models), "CharField"), verbose_name='Заголовок объявления', max_length=255)
    _l_(569349)
    text = _c_(569352, _a_(569351, _n_(569350, "models", lambda: models), "TextField"), verbose_name='Текст объявления')
    _l_(569353)
    CATEGORIES = (
        ('T','Танки'),
        ('HM','Хилы'),
        ('DD','ДД'),
        ('TrM','Торговцы'),
        ('GM','Гилдмастеры'),
        ('QG','Квестгиверы'),
        ('FM','Кузнецы'),
        ('LM','Кожевники'),
        ('PM','Зельевары'),
        ('WM','Мастера заклинаний')
    )
    _l_(569354)

    category = _c_(569357, _a_(569356, _n_(569355, "models", lambda: models), "CharField"), verbose_name='Категория', max_length=3, choices=CATEGORIES)
    _l_(569358)
    pub_date = _c_(569361, _a_(569360, _n_(569359, "models", lambda: models), "DateTimeField"), auto_now_add=True, verbose_name='Дата создания')
    _l_(569362)

    class Meta:
        _l_(569365)

        verbose_name = 'Пост'
        _l_(569363)
        verbose_name_plural = 'Посты'
        _l_(569364)

    def __str__(self):
        _l_(569369)

        aux = _a_(569367, _n_(569366, "self", lambda: self), "title")
        _l_(569368)
        return aux