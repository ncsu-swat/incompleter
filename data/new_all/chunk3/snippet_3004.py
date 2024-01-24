# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54966674/python-typeerror-object-of-type-user-is-not-json-serializable-after-upgrading
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TaggedArticle(_a_(544578, _n_(544577, "models", lambda: models), "Model")):
    _l_(544606)

    user = _c_(544581, _a_(544579, models, "ForeignKey"), User, related_name='tagging', on_delete=_a_(544580, models, "CASCADE"))
    _l_(544582)
    email = _c_(544584, _a_(544583, models, "EmailField"), max_length=255)
    _l_(544585)
    category_fit = _c_(544587, _a_(544586, models, "CharField"), choices=choices, max_length=255)
    _l_(544588)
    article = _c_(544591, _a_(544589, models, "ForeignKey"), Article, related_name='articles', on_delete=_a_(544590, models, "CASCADE"))
    _l_(544592)
    link = _c_(544594, _a_(544593, models, "URLField"), max_length=255,)
    _l_(544595)
    relevant_feedback = _c_(544597, _a_(544596, models, "TextField"), blank=True)
    _l_(544598)
    category = _c_(544600, _a_(544599, models, "CharField"), max_length=255,)
    _l_(544601)
    created_at = _c_(544604, _a_(544602, models, "DateTimeField"), default=_a_(544603, timezone, "now"), editable=False)
    _l_(544605)