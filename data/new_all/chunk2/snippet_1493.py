# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51384124/typeerror-mimetext-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from email.mime.multipart import MIMEMultipart
    _l_(465673)

except ImportError:
    pass
try:
    from email.mime.text import MIMEText
    _l_(465675)

except ImportError:
    pass
try:
    from email.mime.base import MIMEBase
    _l_(465677)

except ImportError:
    pass

msg = _c_(465679, _n_(465678, "MIMEMultipart", lambda: MIMEMultipart))
_l_(465680)

_n_(465681, "msg", lambda: msg)['Subject'] = 'Test message'
_l_(465682)
_n_(465683, "msg", lambda: msg)['From'] = _n_(465684, "sender", lambda: sender)
_l_(465685)
_n_(465686, "msg", lambda: msg)['To'] = _n_(465687, "row", lambda: row)['email']
_l_(465688)
_n_(465689, "msg", lambda: msg).attach = _c_(465692, _n_(465690, "MIMEText", lambda: MIMEText), _n_(465691, "HTML_CONTENT", lambda: HTML_CONTENT), 'html')
_l_(465693)
filename = _n_(465694, "newFileName", lambda: newFileName)
_l_(465695)
attachment = _c_(465698, _n_(465696, "open", lambda: open), _n_(465697, "newFileName", lambda: newFileName), "rb")
_l_(465699)
part = _c_(465701, _n_(465700, "MIMEBase", lambda: MIMEBase), 'application', 'octet-stream')
_l_(465702)
_c_(465708, _a_(465704, _n_(465703, "part", lambda: part), "set_payload"), _c_(465707, _a_(465706, _n_(465705, "attachment", lambda: (attachment)), "read")))
_l_(465709)
_c_(465713, _a_(465711, _n_(465710, "encoders", lambda: encoders), "encode_base64"), _n_(465712, "part", lambda: part))
_l_(465714)
_c_(465718, _a_(465716, _n_(465715, "part", lambda: part), "add_header"), 'Content-Disposition', "attachment; filename= %s" % _n_(465717, "filename", lambda: filename))
_l_(465719)

_c_(465723, _a_(465721, _n_(465720, "msg", lambda: msg), "attach"), _n_(465722, "part", lambda: part))
_l_(465724)