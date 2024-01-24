# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42930366/how-to-remove-typeerror-in-robobrowser
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
url = 'http://xx.yy.zz.abc:defg/opac/html/checkouts'  
_l_(543058)  
browser = _c_(543060, _n_(543059, "RoboBrowser", lambda: RoboBrowser), history=False ,parser='lxml')  
_l_(543061)  
_c_(543065, _a_(543063, _n_(543062, "browser", lambda: browser), "open"), url=_n_(543064, "url", lambda: url))  
_l_(543066)  

sign_up = _c_(543069, _a_(543068, _n_(543067, "browser", lambda: browser), "get_form"), action='./memberlogin')
_l_(543070)
_n_(543071, "sign_up", lambda: sign_up)['txtmemberid'].value = 'user-id'
_l_(543072)
opens = _c_(543076, _a_(543074, _n_(543073, "browser", lambda: browser), "submit_form"), _n_(543075, "sign_up", lambda: sign_up))
_l_(543077)
_c_(543081, _n_(543078, "print", lambda: print), _a_(543080, _n_(543079, "opens", lambda: opens), "parsed"))
_l_(543082)