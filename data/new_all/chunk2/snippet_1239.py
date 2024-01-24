# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67819164/typeerror-at-ap1-checkbooks-type-object-is-not-iterable-return-auth-for
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from rest_framework import serializers
    _l_(425609)

except ImportError:
    pass
try:
    from . models import Book,BookNumber
    _l_(425611)

except ImportError:
    pass

class BookNumberSerializer(_a_(425613, _n_(425612, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(425618)

    class Meta:
        _l_(425617)

        model=_n_(425614, "BookNumber", lambda: BookNumber)
        _l_(425615)
        fields=['id','isbn_10','isbn_30']
        _l_(425616)


class BookSerializer(_a_(425620, _n_(425619, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(425628)

    number=_c_(425622, _n_(425621, "BookNumberSerializer", lambda: BookNumberSerializer), many=False)
    _l_(425623)
    class Meta:
        _l_(425627)

        model=_n_(425624, "Book", lambda: Book)
        _l_(425625)
        fields=['id','title','author','number']
        _l_(425626)