# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57184677/attributeerror-module-yagmail-has-no-attribute-smtp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import yagmail
    _l_(556362)

except ImportError:
    pass
receiver = "pat*******@gmail.com"
_l_(556363)
body = "Hello there from Yagmail"
_l_(556364)
filename = "c.pdf"
_l_(556365)

yag = _c_(556367, _n_(556366, "yagmail", lambda: yagmail), user="dar**********@gmail.com", password="**********", host='smtp.gmail.com')
_l_(556368)
_c_(556374, _a_(556370, _n_(556369, "yag", lambda: yag), "send"), to=_n_(556371, "receiver", lambda: receiver),
    subject="Yagmail test with attachment",
    contents=_n_(556372, "body", lambda: body), 
    attachments=_n_(556373, "filename", lambda: filename),
)
_l_(556375)