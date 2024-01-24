# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42098053/typeerror-object-takes-no-parameters-in-python-3-x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Media(_n_(678887, "Resource", lambda: Resource)):
    _l_(678896)


    def get(self):
        _l_(678895)

        m = _c_(678889, _n_(678888, "Media", lambda: Media), 'id', 'taken_time')
        _l_(678890)
        aux = _c_(678893, _n_(678891, "jsonify", lambda: jsonify), _n_(678892, "m", lambda: m))
        _l_(678894)
        return aux

media_api = _c_(678899, _n_(678897, "Blueprint", lambda: Blueprint), 'resources.media', _n_(678898, "__name__", lambda: __name__))
_l_(678900)
api = _c_(678903, _n_(678901, "Api", lambda: Api), _n_(678902, "media_api", lambda: media_api))
_l_(678904)
_c_(678908, _a_(678906, _n_(678905, "api", lambda: api), "add_resource"), _n_(678907, "Media", lambda: Media),
    '/medias',
    endpoint='medias'
)
_l_(678909)