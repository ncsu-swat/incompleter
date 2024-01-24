# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49000930/django-attributeerror-tag-object-has-no-attribute-summary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Summary(_a_(665655, _n_(665654, "models", lambda: models), "Model")):
    _l_(665680)


    question_text = _c_(665657, _a_(665656, models, "CharField"), max_length=255)
    _l_(665658)
    created_at = _c_(665660, _a_(665659, models, "DateTimeField"), auto_now_add=True)
    _l_(665661)
    url = _c_(665663, _a_(665662, models, "URLField"), null=False)
    _l_(665664)
    cover_image = _c_(665666, _a_(665665, models, "CharField"), max_length=255)
    _l_(665667)
    tags = _c_(665669, _a_(665668, models, "ManyToManyField"), 'Tag', related_name='summaries', blank=True)
    _l_(665670)
    userProfileSummary = _c_(665672, _a_(665671, models, "ManyToManyField"), 'UserProfile', through='UserProfileSummary')
    _l_(665673)

    def __str__(self):
        _l_(665677)

        aux = _a_(665675, _n_(665674, "self", lambda: self), "question_text")
        _l_(665676)
        return aux

    class Meta:
        _l_(665679)

        verbose_name_plural = "Summaries"
        _l_(665678)