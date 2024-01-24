# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60412580/attributeerror-nonetype-object-has-no-attribute-read-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
app = _c_(700555, _n_(700553, "Flask", lambda: Flask), _n_(700554, "__name__", lambda: __name__))
_l_(700556)
_a_(700558, _n_(700557, "app", lambda: app), "config")['JSON_AS_ASCII'] = False
_l_(700559)
_a_(700561, _n_(700560, "app", lambda: app), "config")['JSONIFY_PRETTYPRINT_REGULAR'] = True
_l_(700562)


@_c_(700565, _a_(700564, _n_(700563, "app", lambda: app), "route"), '/', methods=['GET'])
def index():
    _l_(700569)

    aux = _c_(700567, _n_(700566, "render_template", lambda: render_template), 'index.html')
    _l_(700568)
    return aux


@_c_(700572, _a_(700571, _n_(700570, "app", lambda: app), "route"), '/web/predict', methods=['POST'])
def web_predict():
    _l_(700603)

    image1 = _c_(700578, _a_(700577, _c_(700576, _a_(700575, _a_(700574, _n_(700573, "request", lambda: request), "files"), "get"), 'image1'), "read"))
    _l_(700579)
    image2 = _c_(700585, _a_(700584, _c_(700583, _a_(700582, _a_(700581, _n_(700580, "request", lambda: request), "files"), "get"), 'image2'), "read"))
    _l_(700586)

    result = _c_(700590, _n_(700587, "process", lambda: process), _n_(700588, "image1", lambda: image1), _n_(700589, "image2", lambda: image2))
    _l_(700591)
    result = _c_(700597, _n_(700592, "Markup", lambda: Markup), _c_(700596, _a_(700594, _n_(700593, "json2html", lambda: json2html), "convert"), _n_(700595, "result", lambda: result)))
    _l_(700598)
    aux = _c_(700601, _n_(700599, "render_template", lambda: render_template), 'index.html', result=_n_(700600, "result", lambda: result))
    _l_(700602)
    return aux