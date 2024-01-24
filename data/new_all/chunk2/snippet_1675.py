# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64344750/typeerror-init-missing-1-required-positional-argument-axis-how-can-i-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CustomScale(_a_(434137, _n_(434136, "mscale", lambda: mscale), "ScaleBase")):
    _l_(434213)

    name = 'custom'
    _l_(434138)

    def __init__(self,axis, **kwargs):
        _l_(434147)

        _c_(434143, _a_(434141, _a_(434140, _n_(434139, "mscale", lambda: mscale), "ScaleBase"), "__init__"), _n_(434142, "self", lambda: self))
        _l_(434144)
        _n_(434145, "self", lambda: self).thresh = None #thresh
        _l_(434146) #thresh

    def get_transform(self):
        _l_(434154)

        aux = _c_(434152, _a_(434149, _n_(434148, "self", lambda: self), "CustomTransform"), _a_(434151, _n_(434150, "self", lambda: self), "thresh"))
        _l_(434153)
        return aux

    def set_default_locators_and_formatters(self, axis):
        _l_(434156)

        pass
        _l_(434155)

    class CustomTransform(_a_(434157, mtransforms, "Transform")):
        _l_(434184)

        input_dims = 1
        _l_(434158)
        output_dims = 1
        _l_(434159)
        is_separable = True
        _l_(434160)

        def __init__(self, thresh):
            _l_(434170)

            _c_(434165, _a_(434163, _a_(434162, _n_(434161, "mtransforms", lambda: mtransforms), "Transform"), "__init__"), _n_(434164, "self", lambda: self))
            _l_(434166)
            _n_(434167, "self", lambda: self).thresh = _n_(434168, "thresh", lambda: thresh)
            _l_(434169)

        def transform_non_affine(self, a):
            _l_(434176)

            aux = _c_(434174, _a_(434172, _n_(434171, "np", lambda: np), "log"), 1+_n_(434173, "a", lambda: a))
            _l_(434175)
            return aux

        def inverted(self):
            _l_(434183)

            aux = _c_(434181, _a_(434178, _n_(434177, "CustomScale", lambda: CustomScale), "InvertedCustomTransform"), _a_(434180, _n_(434179, "self", lambda: self), "thresh"))
            _l_(434182)
            return aux

    class InvertedCustomTransform(_a_(434185, mtransforms, "Transform")):
        _l_(434212)

        input_dims = 1
        _l_(434186)
        output_dims = 1
        _l_(434187)
        is_separable = True
        _l_(434188)

        def __init__(self, thresh):
            _l_(434198)

            _c_(434193, _a_(434191, _a_(434190, _n_(434189, "mtransforms", lambda: mtransforms), "Transform"), "__init__"), _n_(434192, "self", lambda: self))
            _l_(434194)
            _n_(434195, "self", lambda: self).thresh = _n_(434196, "thresh", lambda: thresh)
            _l_(434197)

        def transform_non_affine(self, a):
            _l_(434204)

            aux = _c_(434202, _a_(434200, _n_(434199, "np", lambda: np), "exp"), _n_(434201, "a", lambda: a))-1
            _l_(434203)
            return aux

        def inverted(self):
            _l_(434211)

            aux = _c_(434209, _a_(434206, _n_(434205, "CustomScale", lambda: CustomScale), "CustomTransform"), _a_(434208, _n_(434207, "self", lambda: self), "thresh"))
            _l_(434210)
            return aux

# Now that the Scale class has been defined, it must be registered so
# that ``matplotlib`` can find it.
_c_(434217, _a_(434215, _n_(434214, "mscale", lambda: mscale), "register_scale"), _n_(434216, "CustomScale", lambda: CustomScale))
_l_(434218)
z = [0,0.1,0.3,0.9,1,2,5]
_l_(434219)
thick = [20,40,20,60,37,32,21]
_l_(434220)

fig = _c_(434223, _a_(434222, _n_(434221, "plt", lambda: plt), "figure"), figsize=(8,5))
_l_(434224)
ax1 = _c_(434227, _a_(434226, _n_(434225, "fig", lambda: fig), "add_subplot"), 111)
_l_(434228)
_c_(434233, _a_(434230, _n_(434229, "ax1", lambda: ax1), "plot"), _n_(434231, "z", lambda: z), _n_(434232, "thick", lambda: thick), marker='o', linewidth=2, c='k')
_l_(434234)

_c_(434237, _a_(434236, _n_(434235, "plt", lambda: plt), "xlabel"), r'$\rm{redshift}$', size=16)
_l_(434238)
_c_(434241, _a_(434240, _n_(434239, "plt", lambda: plt), "ylabel"), r'$\rm{thickness\ (kpc)}$', size=16)
_l_(434242)
_c_(434247, _a_(434246, _c_(434245, _a_(434244, _n_(434243, "plt", lambda: plt), "gca")), "set_yscale"), 'custom')
_l_(434248)
_c_(434251, _a_(434250, _n_(434249, "plt", lambda: plt), "show"))
_l_(434252)