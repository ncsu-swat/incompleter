# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55292116/python-imap-typeerror-nonetype-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import imaplib, time, email, mailbox, datetime
    _l_(433054)

except ImportError:
    pass
server = "imap.gmail.com"
_l_(433055)
port = 993
_l_(433056)
user = "Redacted"
_l_(433057)
password = "Redacted"
_l_(433058)

def main():
    _l_(433161)

    while True:
        _l_(433160)

        conn = _c_(433063, _a_(433060, _n_(433059, "imaplib", lambda: imaplib), "IMAP4_SSL"), _n_(433061, "server", lambda: server), _n_(433062, "port", lambda: port))
        _l_(433064)
        _c_(433069, _a_(433066, _n_(433065, "conn", lambda: conn), "login"), _n_(433067, "user", lambda: user), _n_(433068, "password", lambda: password))
        _l_(433070)
        _c_(433073, _a_(433072, _n_(433071, "conn", lambda: conn), "list"))
        _l_(433074)
        _c_(433077, _a_(433076, _n_(433075, "conn", lambda: conn), "select"), 'inbox', readonly=True)
        _l_(433078)
        result, data = _c_(433081, _a_(433080, _n_(433079, "conn", lambda: conn), "search"), None, '(UNSEEN SUBJECT "Alert: Storage Almost At Max Capacity")')
        _l_(433082)
        i = _c_(433087, _n_(433083, "len", lambda: len), _c_(433086, _a_(433085, _n_(433084, "data", lambda: data)[0], "split")))
        _l_(433088)

        for x in _c_(433091, _n_(433089, "range", lambda: range), _n_(433090, "i", lambda: i)):
            _l_(433155)

            latest_email_uid = _c_(433094, _a_(433093, _n_(433092, "data", lambda: data)[0], "split"))[_n_(433095, "x", lambda: x)]
            _l_(433096)
            result, email_data = _c_(433100, _a_(433098, _n_(433097, "conn", lambda: conn), "uid"), 'fetch', _n_(433099, "latest_email_uid", lambda: latest_email_uid), '(RFC822)')
            _l_(433101)
            raw_email = _n_(433102, "email_data", lambda: email_data)[0][1] #This is where it throws the error
            _l_(433103) #This is where it throws the error
            raw_email_string = _c_(433106, _a_(433105, _n_(433104, "raw_email", lambda: raw_email), "decode"), 'utf-8')
            _l_(433107)
            email_message = _c_(433111, _a_(433109, _n_(433108, "email", lambda: email), "message_from_string"), _n_(433110, "raw_email_string", lambda: raw_email_string))
            _l_(433112)
            date_tuple = _c_(433117, _a_(433115, _a_(433114, _n_(433113, "email", lambda: email), "utils"), "parsedate_tz"), _n_(433116, "email_message", lambda: email_message)['Date'])
            _l_(433118)
            local_date = _c_(433127, _a_(433121, _a_(433120, _n_(433119, "datetime", lambda: datetime), "datetime"), "fromtimestamp"), _c_(433126, _a_(433124, _a_(433123, _n_(433122, "email", lambda: email), "utils"), "mktime_tz"), _n_(433125, "date_tuple", lambda: date_tuple)))
            _l_(433128)
            local_message_date = "%s" %_c_(433133, _n_(433129, "str", lambda: str), _c_(433132, _a_(433131, _n_(433130, "local_date", lambda: local_date), "strftime"), "%a, %d %b %Y %H:%M:%S"))
            _l_(433134)
            for part in _c_(433137, _a_(433136, _n_(433135, "email_message", lambda: email_message), "walk")):
                _l_(433154)

                if _c_(433140, _a_(433139, _n_(433138, "part", lambda: part), "get_content_type")) == "text/plain":
                    _l_(433153)

                    body = _c_(433143, _a_(433142, _n_(433141, "part", lambda: part), "get_payload"), decode=True)
                    _l_(433144)
                    body = _c_(433147, _a_(433146, _n_(433145, "body", lambda: body), "decode"), 'utf-8')
                    _l_(433148)
                    body = _c_(433151, _a_(433150, _n_(433149, "body", lambda: body), "split"))
                    _l_(433152)
        _c_(433158, _a_(433157, _n_(433156, "conn", lambda: conn), "close"))
        _l_(433159)

if _n_(433162, "__name__", lambda: __name__) == "__main__":
    _l_(433166)

    _c_(433164, _n_(433163, "main", lambda: main))
    _l_(433165)