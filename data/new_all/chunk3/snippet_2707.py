# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66065071/got-attributeerror-when-attempting-to-get-a-value-for-field-text-on-serializer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CommentSerializer(_a_(568372, _n_(568371, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(568382)

    owner = _c_(568374, _a_(568373, serializers, "StringRelatedField"))
    _l_(568375)
    post = _c_(568377, _a_(568376, serializers, "StringRelatedField"))
    _l_(568378)

    class Meta:
        _l_(568381)

        model = Comment
        _l_(568379)
        fields = ['text', 'created_at', 'post', 'owner']
        _l_(568380)