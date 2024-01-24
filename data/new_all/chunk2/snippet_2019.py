# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69516737/getting-a-type-error-at-articles-1-get-got-multiple-values-for-argument-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Article_List(_n_(449636, "APIView", lambda: APIView)):
    _l_(449680)

    def get(self,request):
        _l_(449651)

        articles = _c_(449640, _a_(449639, _a_(449638, _n_(449637, "Article", lambda: Article), "objects"), "all"))
        _l_(449641)
        serializer = _c_(449644, _n_(449642, "ArticleSerializer", lambda: ArticleSerializer), _n_(449643, "articles", lambda: articles), many=True)
        _l_(449645)
        aux = _c_(449649, _n_(449646, "Response", lambda: Response), _a_(449648, _n_(449647, "serializer", lambda: serializer), "data"))
        _l_(449650)
        return aux
    def post(self,request):
        _l_(449679)

        serializer = _c_(449655, _n_(449652, "ArticleSerializer", lambda: ArticleSerializer), data=_a_(449654, _n_(449653, "request", lambda: request), "data"))
        _l_(449656)
        if _c_(449659, _a_(449658, _n_(449657, "serializer", lambda: serializer), "is_valid")):
            _l_(449671)

            _c_(449662, _a_(449661, _n_(449660, "serializer", lambda: serializer), "save"))
            _l_(449663)
            aux = _c_(449669, _n_(449664, "Response", lambda: Response), _a_(449666, _n_(449665, "serializer", lambda: serializer), "data"), status=_a_(449668, _n_(449667, "status", lambda: status), "HTTP_201_CREATED"))
            _l_(449670)
            return aux
        aux = _c_(449677, _n_(449672, "Response", lambda: Response), _a_(449674, _n_(449673, "serializer", lambda: serializer), "errors"), status=_a_(449676, _n_(449675, "status", lambda: status), "HTTP_400_BAD_REQUEST"))  # Bad Request
        _l_(449678)  # Bad Request
        return aux  # Bad Request


class ArticleDetails(_n_(449681, "APIView", lambda: APIView)):
    _l_(449760)

    def get_objects(self, id):
        _l_(449697)

        try:
            _l_(449696)

            aux = _c_(449686, _a_(449684, _a_(449683, _n_(449682, "Article", lambda: Article), "objects"), "get"), id=_n_(449685, "id", lambda: id))
            _l_(449687)
            return aux
        except _a_(449689, _n_(449688, "Article", lambda: Article), "DoesNotExist"):
            _l_(449695)

            aux = _c_(449693, _n_(449690, "Response", lambda: Response), status=_a_(449692, _n_(449691, "status", lambda: status), "HTTP_404_NOT_FOUND"))
            _l_(449694)
            return aux

    def get(self, id):
        _l_(449712)

        article = _c_(449701, _a_(449699, _n_(449698, "self", lambda: self), "get_objects"), _n_(449700, "id", lambda: id))
        _l_(449702)
        serializer = _c_(449705, _n_(449703, "ArticleSerializer", lambda: ArticleSerializer), _n_(449704, "article", lambda: article))
        _l_(449706)
        aux = _c_(449710, _n_(449707, "Response", lambda: Response), _a_(449709, _n_(449708, "serializer", lambda: serializer), "data"))
        _l_(449711)
        return aux

    def put(self, request , id):
        _l_(449744)

        article = _c_(449716, _a_(449714, _n_(449713, "self", lambda: self), "get_objects"), _n_(449715, "id", lambda: id))
        _l_(449717)
        serializer = _c_(449722, _n_(449718, "ArticleSerializer", lambda: ArticleSerializer), _n_(449719, "article", lambda: article), data=_a_(449721, _n_(449720, "request", lambda: request), "data"))
        _l_(449723)
        if _c_(449726, _a_(449725, _n_(449724, "serializer", lambda: serializer), "is_valid")):
            _l_(449736)

            _c_(449729, _a_(449728, _n_(449727, "serializer", lambda: serializer), "save"))
            _l_(449730)
            aux = _c_(449734, _n_(449731, "Response", lambda: Response), _a_(449733, _n_(449732, "serializer", lambda: serializer), "data"))
            _l_(449735)
            return aux
        aux = _c_(449742, _n_(449737, "Response", lambda: Response), _a_(449739, _n_(449738, "serializer", lambda: serializer), "errors"), status=_a_(449741, _n_(449740, "status", lambda: status), "HTTP_400_BAD_REQUEST"))
        _l_(449743)
        return aux
    def delete(self, request,id):
        _l_(449759)

        article = _c_(449748, _a_(449746, _n_(449745, "self", lambda: self), "get_objects"), _n_(449747, "id", lambda: id))
        _l_(449749)
        _c_(449752, _a_(449751, _n_(449750, "article", lambda: article), "delete"))
        _l_(449753)
        aux = _c_(449757, _n_(449754, "Response", lambda: Response), status=_a_(449756, _n_(449755, "status", lambda: status), "HTTP_204_NO_CONTENT"))
        _l_(449758)
        return aux