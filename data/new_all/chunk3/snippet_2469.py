# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76818922/typeerror-object-of-type-linkpreview-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class PreviewLink(_n_(533790, "APIView", lambda: APIView)):
    _l_(533825)

    permission_classes = (IsAuthenticated, IsNotSuspended)
    _l_(533791)
    throttle_scope = 'link_preview'
    _l_(533792)

    def post(self, request):
        _l_(533824)

        serializer = _c_(533797, _n_(533793, "PreviewLinkSerializer", lambda: PreviewLinkSerializer), data=_a_(533795, _n_(533794, "request", lambda: request), "data"), context={"request": _n_(533796, "request", lambda: request)})
        _l_(533798)
        _c_(533801, _a_(533800, _n_(533799, "serializer", lambda: serializer), "is_valid"), raise_exception=True)
        _l_(533802)
        data = _a_(533804, _n_(533803, "serializer", lambda: serializer), "validated_data")
        _l_(533805)

        link = _c_(533808, _a_(533807, _n_(533806, "data", lambda: data), "get"), 'link')
        _l_(533809)
        user = _a_(533811, _n_(533810, "request", lambda: request), "user")
        _l_(533812)

        link_preview = _c_(533816, _a_(533814, _n_(533813, "user", lambda: user), "preview_link"), _n_(533815, "link", lambda: link))
        _l_(533817)
        aux = _c_(533822, _n_(533818, "Response", lambda: Response), _n_(533819, "link_preview", lambda: link_preview), status=_a_(533821, _n_(533820, "status", lambda: status), "HTTP_200_OK"))
        _l_(533823)

        return aux

class LinkIsPreviewable(_n_(533826, "APIView", lambda: APIView)):
    _l_(533861)

    permission_classes = (IsAuthenticated, IsNotSuspended)
    _l_(533827)
    throttle_scope = 'link_preview'
    _l_(533828)

    def post(self, request):
        _l_(533860)

        serializer = _c_(533833, _n_(533829, "PreviewLinkSerializer", lambda: PreviewLinkSerializer), data=_a_(533831, _n_(533830, "request", lambda: request), "data"), context={"request": _n_(533832, "request", lambda: request)})
        _l_(533834)
        _c_(533837, _a_(533836, _n_(533835, "serializer", lambda: serializer), "is_valid"), raise_exception=True)
        _l_(533838)
        data = _a_(533840, _n_(533839, "serializer", lambda: serializer), "validated_data")
        _l_(533841)

        link = _c_(533844, _a_(533843, _n_(533842, "data", lambda: data), "get"), 'link')
        _l_(533845)

        try:
            _l_(533853)

            is_previewable = _c_(533848, _n_(533846, "link_preview", lambda: link_preview), url=_n_(533847, "link", lambda: link))
            _l_(533849)
        except _n_(533850, "Exception", lambda: Exception) as e:
            _l_(533852)

            is_previewable = False
            _l_(533851)
        aux = _c_(533858, _n_(533854, "Response", lambda: Response), {
            'is_previewable': _n_(533855, "is_previewable", lambda: is_previewable)
        }, status=_a_(533857, _n_(533856, "status", lambda: status), "HTTP_200_OK"))
        _l_(533859)

        return aux