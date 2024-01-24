# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65362791/typeerror-object-of-type-set-is-not-json-serializable-while-using-requests
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(400934)

except ImportError:
    pass
headd = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Pragma":"no-cache" ,
    "Accept":"*/*" 
}
_l_(400935)
content = {
    f"\"_username\":\"MY_EMAIL\",\"_password\":\"MY_PASSWORD\",\"_remember_me\":true" 
}
_l_(400936)
_c_(400944, _n_(400937, "print", lambda: print), _a_(400943, _c_(400942, _a_(400939, _n_(400938, "requests", lambda: requests), "get"), 'https://www.bang.com/login_check',headers=_n_(400940, "headd", lambda: headd),json=_n_(400941, "content", lambda: content)), "text"))
_l_(400945)