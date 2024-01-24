# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58213802/how-to-fix-attributeerror-mapper-object-has-no-attribute-persist-selectable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(537406)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(537408)

except ImportError:
    pass
try:
    from flask import Flask
    _l_(537410)

except ImportError:
    pass
try:
    from sqlalchemy.orm.mapper import configure_mappers
    _l_(537412)

except ImportError:
    pass
try:
    from flask_sqlalchemy import SQLAlchemy, BaseQuery
    _l_(537414)

except ImportError:
    pass
try:
    from sqlalchemy_searchable import SearchQueryMixin
    _l_(537416)

except ImportError:
    pass
try:
    from sqlalchemy_utils.types import TSVectorType
    _l_(537418)

except ImportError:
    pass
try:
    from sqlalchemy_searchable import make_searchable
    _l_(537420)

except ImportError:
    pass

basedir = _c_(537429, _a_(537423, _a_(537422, _n_(537421, "os", lambda: os), "path"), "abspath"), _c_(537428, _a_(537426, _a_(537425, _n_(537424, "os", lambda: os), "path"), "dirname"), _n_(537427, "__file__", lambda: __file__)))
_l_(537430)

app = _c_(537433, _n_(537431, "Flask", lambda: Flask), _n_(537432, "__name__", lambda: __name__))
_l_(537434)
_a_(537436, _n_(537435, "app", lambda: app), "config")['SECRET_KEY'] = 'samplesecret'
_l_(537437)
_a_(537439, _n_(537438, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/blog'
_l_(537440)

db = _c_(537442, _n_(537441, "SQLAlchemy", lambda: SQLAlchemy))
_l_(537443)
_c_(537447, _n_(537444, "make_searchable", lambda: make_searchable), _a_(537446, _n_(537445, "db", lambda: db), "metadata"))
_l_(537448)

class PostQuery(_n_(537449, "BaseQuery", lambda: BaseQuery), _n_(537450, "SearchQueryMixin", lambda: SearchQueryMixin)):
    _l_(537452)

    pass
    _l_(537451)

class Post(_a_(537454, _n_(537453, "db", lambda: db), "Model")):
    _l_(537525)

    query_class = _n_(537455, "PostQuery", lambda: PostQuery)
    _l_(537456)
    id = _c_(537461, _a_(537458, _n_(537457, "db", lambda: db), "Column"), _a_(537460, _n_(537459, "db", lambda: db), "Integer"), primary_key=True)
    _l_(537462)
    title = _c_(537468, _a_(537464, _n_(537463, "db", lambda: db), "Column"), _c_(537467, _a_(537466, _n_(537465, "db", lambda: db), "String"), 255), nullable=False)
    _l_(537469)
    date_posted = _c_(537476, _a_(537471, _n_(537470, "db", lambda: db), "Column"), _a_(537473, _n_(537472, "db", lambda: db), "DateTime"), nullable=False, default=_a_(537475, _n_(537474, "datetime", lambda: datetime), "utcnow"))
    _l_(537477)
    content = _c_(537482, _a_(537479, _n_(537478, "db", lambda: db), "Column"), _a_(537481, _n_(537480, "db", lambda: db), "Text"), nullable=False)
    _l_(537483)
    search_vector = _c_(537488, _a_(537485, _n_(537484, "db", lambda: db), "Column"), _c_(537487, _n_(537486, "TSVectorType", lambda: TSVectorType), 'title', 'content'))
    _l_(537489)
    image_thumb = _c_(537495, _a_(537491, _n_(537490, "db", lambda: db), "Column"), _c_(537494, _a_(537493, _n_(537492, "db", lambda: db), "String"), 255), nullable=False, default='default.jpg')
    _l_(537496)
    slug = _c_(537501, _a_(537498, _n_(537497, "db", lambda: db), "Column"), _a_(537500, _n_(537499, "db", lambda: db), "Text"))
    _l_(537502)
    publish = _c_(537508, _a_(537504, _n_(537503, "db", lambda: db), "Column"), _c_(537507, _a_(537506, _n_(537505, "db", lambda: db), "Boolean")), nullable=False, server_default='1')
    _l_(537509)
    headline = _c_(537515, _a_(537511, _n_(537510, "db", lambda: db), "Column"), _c_(537514, _a_(537513, _n_(537512, "db", lambda: db), "Boolean")), nullable=False)
    _l_(537516)
    dibaca = _c_(537521, _a_(537518, _n_(537517, "db", lambda: db), "Column"), _a_(537520, _n_(537519, "db", lambda: db), "Integer"), nullable=False, default=0)
    _l_(537522)

    def __repr__(self):
        _l_(537524)

        aux = "Post('{self.title}', '{self.date_posted}')"
        _l_(537523)
        return aux

_c_(537528, _a_(537527, _n_(537526, "db", lambda: db), "configure_mappers")) #very important!
_l_(537529) #very important!

_c_(537539, _n_(537530, "print", lambda: print), _c_(537538, _a_(537537, _c_(537536, _a_(537535, _c_(537534, _a_(537533, _a_(537532, _n_(537531, "Post", lambda: Post), "query"), "search"), u'something'), "limit"), 5), "all")))
_l_(537540)