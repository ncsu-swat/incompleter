# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45911113/formatting-strings-s-returns-typeerror-a-float-is-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(467364)

except ImportError:
    pass

date = _c_(467375, _a_(467374, (_c_(467370, _a_(467369, _c_(467368, _a_(467367, _a_(467366, _n_(467365, "datetime", lambda: datetime), "datetime"), "today")), "date")) - _c_(467373, _a_(467372, _n_(467371, "datetime", lambda: datetime), "timedelta"), days=100)), "strftime"), "%m/%d/%Y")
_l_(467376)
date = _c_(467379, _n_(467377, "str", lambda: str), _n_(467378, "date", lambda: date))
_l_(467380)
date = _c_(467383, _a_(467382, _n_(467381, "date", lambda: date), "replace"), "/","%2F")
_l_(467384)

def genUrl(account, date, lastName, firstName):
    _l_(467401)

    url = "https://arpmp-ph.hidinc.com/arappl/bdarpdmq/pmqadhocrpt.html?a=&page=recipqry&disp-bdate=%s&disp-edate=%s&recip-list=02685245&output=web&dt-sort-by=rcpdt&mode=Recipient_Query&w_method=POST&suplist=BM0650386&base-prsb=0&base-phrm=0&base-recip=1&tot-recip=1&report=PHY&recip-sex=A&recip-dob=01%2F21%2F1964&account-id=%s&date=%s&dob-days=0&recip-name=%s&recip-fname=%s&enum-read-cnt=2&enum-keep-cnt=1&etime=5&pagename=pmqrecipqry&pdmdir=arpdm&pdmstate=ar&scriptname=%2Farappl%2Fbdarpdmq&exprecip=yes" %(_n_(467385, "date", lambda: date), _c_(467391, _n_(467386, "str", lambda: str), _c_(467390, _a_(467389, _a_(467388, _n_(467387, "datetime", lambda: datetime), "datetime"), "now"))), _n_(467392, "account", lambda: account), _n_(467393, "date", lambda: date), _n_(467394, "lastName", lambda: lastName), _n_(467395, "firstName", lambda: firstName))
    _l_(467396)
    _c_(467399, _n_(467397, "print", lambda: print), _n_(467398, "url", lambda: url))
    _l_(467400)

_c_(467404, _n_(467402, "genUrl", lambda: genUrl), "example",_n_(467403, "date", lambda: date), "Smith", "Jogn")
_l_(467405)