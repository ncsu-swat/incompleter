# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53715464/typeerror-a-bytes-like-object-is-required-not-str-during-oauth-2-0-callbac
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
authentication_token = _a_(547257, _n_(547256, "request", lambda: request), "args")['code']
_l_(547258)
code_payload = {
    "grant_type": "authorization_code",
    "code": _c_(547261, _n_(547259, "str", lambda: str), _n_(547260, "authentication_token", lambda: authentication_token)),
    "redirect_uri": _n_(547262, "REDIRECT_URI", lambda: REDIRECT_URI)
}
_l_(547263)
encoded_oauth2_tokens = _c_(547270, _a_(547265, _n_(547264, "base64", lambda: base64), "b64encode"), _c_(547269, _a_(547266, '{}:{}', "format"), _n_(547267, "CLIENT_ID", lambda: CLIENT_ID), _n_(547268, "CLIENT_SECRET", lambda: CLIENT_SECRET)))        
_l_(547271)        
headers = {"Authorization": _c_(547274, _a_(547272, "Basic {}", "format"), _n_(547273, "encoded_oauth2_tokens", lambda: encoded_oauth2_tokens))}
_l_(547275)
post_request = _c_(547281, _a_(547277, _n_(547276, "requests", lambda: requests), "post"), _n_(547278, "SPOTIFY_TOKEN_URL", lambda: SPOTIFY_TOKEN_URL), data=_n_(547279, "code_payload", lambda: code_payload), headers=_n_(547280, "headers", lambda: headers))  
_l_(547282)  