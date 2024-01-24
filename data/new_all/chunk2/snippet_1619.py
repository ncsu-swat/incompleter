# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69744733/attributeerror-wsgirequest-object-has-no-attribute-get-heroku
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PostDetail(_a_(450744, _n_(450743, "generics", lambda: generics), "GenericAPIView")):
    _l_(450807)

    """Blog post details"""
    queryset = _c_(450747, _a_(450746, _a_(450745, Post, "objects"), "all"))
    _l_(450748)
    serializer_class = _a_(450749, serializers, "PostSerializer")
    _l_(450750)
    authentication_classes = (JWTAuthentication,)
    _l_(450751)
    permission_classes = (PostsProtectOrReadOnly, IsMentorOnly,)
    _l_(450752)
    lookup_field = 'slug'
    _l_(450753)

    def get_post_object(self, slug):
        _l_(450760)

        post = _c_(450756, _n_(450754, "get_blog_by_slug", lambda: get_blog_by_slug), _n_(450755, "slug", lambda: slug))
        _l_(450757)
        aux = _n_(450758, "post", lambda: post)
        _l_(450759)
        return aux

    def get(self, request, slug):
        _l_(450806)

        post = _c_(450764, _a_(450762, _n_(450761, "self", lambda: self), "get_post_object"), _n_(450763, "slug", lambda: slug))
        _l_(450765)
        if not _n_(450766, "post", lambda: post):
            _l_(450775)

            aux = _c_(450773, _a_(450768, _n_(450767, "response", lambda: response), "Response"), {
                'errors': _c_(450770, _n_(450769, "_", lambda: _), 'Sorry, Blog post with the specified slug does'
                            'not exist')
            }, status=_a_(450772, _n_(450771, "status", lambda: status), "HTTP_404_NOT_FOUND"))
            _l_(450774)
            return aux

        # track views of a viewed blog post.
        ip_address = _c_(450778, _n_(450776, "get_ip_address", lambda: get_ip_address), _n_(450777, "request", lambda: request))
        _l_(450779)
        obj = _c_(450784, _a_(450782, _a_(450781, _n_(450780, "CustomIPAddress", lambda: CustomIPAddress), "objects"), "create"), address=_n_(450783, "ip_address", lambda: ip_address))
        _l_(450785)
        _c_(450790, _a_(450788, _a_(450787, _n_(450786, "post", lambda: post), "address_views"), "add"), _n_(450789, "obj", lambda: obj))
        _l_(450791)

        serializer = _c_(450796, _a_(450793, _n_(450792, "self", lambda: self), "serializer_class"), _n_(450794, "post", lambda: post), context=_n_(450795, "request", lambda: request))
        _l_(450797)
        aux = _c_(450804, _a_(450799, _n_(450798, "response", lambda: response), "Response"), _a_(450801, _n_(450800, "serializer", lambda: serializer), "data"), status=_a_(450803, _n_(450802, "status", lambda: status), "HTTP_200_OK"))
        _l_(450805)
        return aux