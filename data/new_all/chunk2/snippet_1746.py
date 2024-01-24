# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58784123/one-to-one-relationship-how-to-fix-got-attributeerror-when-attempting-to-get-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class ProfileSerializer (_a_(475496, _n_(475495, "serializers", lambda: serializers), "ModelSerializer")):
    _l_(475506)

    user = _c_(475498, _a_(475497, serializers, "CharField"), source='user.username')
    _l_(475499)
    image = _c_(475501, _a_(475500, serializers, "ImageField"), use_url=True)
    _l_(475502)

    class Meta:
        _l_(475505)

        model = Profile
        _l_(475503)
        fields = ('user', 'bio', 'image')
        _l_(475504)