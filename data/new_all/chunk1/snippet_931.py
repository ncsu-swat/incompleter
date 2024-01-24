# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25491328/typeerror-when-creating-a-wtform-with-mongoengine-and-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Post(_a_(388124, _n_(388123, "database", lambda: database), "Document")):
    _l_(388150)

    author = _c_(388126, _a_(388125, database, "StringField"), default='David Y. Stephenson', max_length=255, required=True
    )
    _l_(388127)
    body = _c_(388129, _a_(388128, database, "StringField"), required=True)
    _l_(388130)
    comments = _c_(388134, _a_(388131, database, "ListField"), _c_(388133, _a_(388132, database, "EmbeddedDocumentField"), 'Comment')
    )
    _l_(388135)
    slug = _c_(388137, _a_(388136, database, "StringField"), max_length=255, required=True, unique=True)
    _l_(388138)
    tease = _c_(388140, _a_(388139, database, "StringField"), max_length=255, required=True)
    _l_(388141)
    time = _c_(388145, _a_(388142, database, "DateTimeField"), default=_a_(388144, _a_(388143, datetime, "datetime"), "now"), required=True
    )
    _l_(388146)
    title = _c_(388148, _a_(388147, database, "StringField"), max_length=255, required=True, unique=True)
    _l_(388149)