# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43901079/typeerror-cant-concat-bytes-to-str-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
request_body = {'grant_type':'password','username': _n_(407118, "username", lambda: username),'password': _n_(407119, "password", lambda: password)}
_l_(407120)
request_headers = {'Content-Type' : 'application/x-www-form-urlencoded','Authorization': "hash string"}
_l_(407121)
http = _c_(407124, _a_(407123, _n_(407122, "urllib3", lambda: urllib3), "PoolManager"))
_l_(407125)
response = _c_(407130, _a_(407127, _n_(407126, "http", lambda: http), "request"), 'POST', 'https://api/url/endpoint', headers=_n_(407128, "request_headers", lambda: request_headers), body=_n_(407129, "request_body", lambda: request_body))
_l_(407131)