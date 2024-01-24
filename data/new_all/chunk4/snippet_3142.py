# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40929221/typeerror-received-when-using-microsoft-cognitive-computer-vision-api-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import http.client, urllib.request, urllib.parse, urllib.error, base64
    _l_(620675)

except ImportError:
    pass

MICROSOFT_CV_SUBSCRIPTION_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
_l_(620676)

headers = {
   # Request headers
   'Content-Type': 'application/json',
   'Ocp-Apim-Subscription-Key': _n_(620677, "MICROSOFT_CV_SUBSCRIPTION_KEY", lambda: MICROSOFT_CV_SUBSCRIPTION_KEY),
}
_l_(620678)

params = _c_(620681, _a_(620680, _a_(620679, urllib, "parse"), "urlencode"), {
   'visualFeatures': 'Categories,Adult,Faces,Description,ImageType',
   'details': 'Celebrities',
   'language': 'en',
})
_l_(620682)

data = {
    'url':'http://img.wennermedia.com/article-leads-vertical-300/1250530894_brad_pitt_290x402.jpg',
}
_l_(620683)

try:
    _l_(620722)

    conn = _c_(620686, _a_(620685, _a_(620684, http, "client"), "HTTPSConnection"), 'api.projectoxford.ai')
    _l_(620687)
    _c_(620693, _a_(620689, _n_(620688, "conn", lambda: conn), "request"), "POST", "/vision/v1.0/analyze?%s" % _n_(620690, "params", lambda: params), _n_(620691, "data", lambda: data), _n_(620692, "headers", lambda: headers))
    _l_(620694)
    response = _c_(620697, _a_(620696, _n_(620695, "conn", lambda: conn), "getresponse"))
    _l_(620698)
    data = _c_(620701, _a_(620700, _n_(620699, "response", lambda: response), "read"))
    _l_(620702)
    _c_(620705, _n_(620703, "print", lambda: print), _n_(620704, "data", lambda: data))
    _l_(620706)
    _c_(620709, _a_(620708, _n_(620707, "conn", lambda: conn), "close"))
    _l_(620710)
except _n_(620711, "Exception", lambda: Exception) as e:
    _l_(620721)

    _c_(620719, _n_(620712, "print", lambda: print), _c_(620718, _a_(620713, "[Errno {0}] {1}", "format"), _a_(620715, _n_(620714, "e", lambda: e), "errno"), _a_(620717, _n_(620716, "e", lambda: e), "strerror")))
    _l_(620720)