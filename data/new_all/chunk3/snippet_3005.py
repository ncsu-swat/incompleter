# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54966674/python-typeerror-object-of-type-user-is-not-json-serializable-after-upgrading
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TagForm(_a_(540661, _n_(540660, "forms", lambda: forms), "ModelForm")):
    _l_(540668)

    class Meta:
        _l_(540667)

        model = TaggedArticle
        _l_(540662)
        fields = ('user', 'category_fit', 'article', 'link', 'relevant_feedback', 'category',)
        _l_(540663)
        widgets = {
            'category_fit': _c_(540665, _a_(540664, forms, "RadioSelect"))
        }
        _l_(540666)