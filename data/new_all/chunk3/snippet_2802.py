# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62749290/how-to-use-add-a-descriptor-to-catch-and-raise-typeerror-upon-attribute-fetches
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
...
_l_(548809)
class ArticleField:
    _l_(548814)


    def __init__(self, field_type: _a_(548810, typing, "Type")[_a_(548811, typing, "Any")]):
        _l_(548813)

        pass
        _l_(548812)


class Article:
    _l_(548832)


    def __init__(self, title: _n_(548815, "str", lambda: str), author: _n_(548816, "str", lambda: str), publication_date: _a_(548817, datetime, "datetime"), content: _n_(548818, "str", lambda: str)):
        _l_(548831)

        _n_(548819, "self", lambda: self).title = _n_(548820, "title", lambda: title)
        _l_(548821)
        _n_(548822, "self", lambda: self).author = _n_(548823, "author", lambda: author)
        _l_(548824)
        _n_(548825, "self", lambda: self).publication_date = _n_(548826, "publication_date", lambda: publication_date)
        _l_(548827)
        _n_(548828, "self", lambda: self).content = _n_(548829, "content", lambda: content)
        _l_(548830)
...
_l_(548833)