# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37175460/typeerror-post-data-should-be-bytes-or-an-iterable-of-bytes-it-cannot-be-of-ty
#!/usr/bin/env python
#coding: utf-8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
userid="NicoNicoCreate@gmail.com"
_l_(550479)
passwd="********"
_l_(550480)
try:
    import sys, re, cgi, urllib, urllib.request, urllib.error, http.cookiejar, xml.dom.minidom, time, urllib.parse
    _l_(550482)

except ImportError:
    pass
try:
    import simplejson as json
    _l_(550484)

except ImportError:
    pass

def getToken():
    _l_(550511)

    html = _c_(550489, _a_(550488, _c_(550487, _a_(550486, _a_(550485, urllib, "request"), "urlopen"), "http://www.nicovideo.jp/my/mylist"), "read"))
    _l_(550490)
    for line in _c_(550493, _a_(550492, _n_(550491, "html", lambda: html), "splitlines")):
        _l_(550506)

        mo = _c_(550497, _a_(550495, _n_(550494, "re", lambda: re), "match"), r'^\s*NicoAPI\.token = "(?P<token>[\d\w-]+)";\s*',_n_(550496, "line", lambda: line))
        _l_(550498)
        if _n_(550499, "mo", lambda: mo):
            _l_(550505)

            token = _c_(550502, _a_(550501, _n_(550500, "mo", lambda: mo), "group"), 'token')
            _l_(550503)
            break
            _l_(550504)
    assert _n_(550507, "token", lambda: token)
    _l_(550508)
    aux = _n_(550509, "token", lambda: token)
    _l_(550510)
    return aux

def mylist_create(name):
    _l_(550547)

    cmdurl = "http://www.nicovideo.jp/api/mylistgroup/add"
    _l_(550512)
    q = {}
    _l_(550513)
    _n_(550514, "q", lambda: q)['name'] = _c_(550517, _a_(550516, _n_(550515, "name", lambda: name), "encode"), "utf-8")
    _l_(550518)
    _n_(550519, "q", lambda: q)['description'] = ""
    _l_(550520)
    _n_(550521, "q", lambda: q)['public'] = 0
    _l_(550522)
    _n_(550523, "q", lambda: q)['default_sort'] = 0
    _l_(550524)
    _n_(550525, "q", lambda: q)['icon_id'] = 0
    _l_(550526)
    _n_(550527, "q", lambda: q)['token'] = _n_(550528, "token", lambda: token)
    _l_(550529)
    cmdurl += "?" + _c_(550535, _a_(550534, _c_(550533, _a_(550531, _a_(550530, urllib, "parse"), "urlencode"), _n_(550532, "q", lambda: q)), "encode"), "utf-8")
    _l_(550536)
    j = _c_(550543, _a_(550538, _n_(550537, "json", lambda: json), "load"), _c_(550542, _a_(550540, _a_(550539, urllib, "request"), "urlopen"), _n_(550541, "cmdurl", lambda: cmdurl)), encoding='utf-8')
    _l_(550544)
    aux = _n_(550545, "j", lambda: j)['id']
    _l_(550546)
    return aux

def addvideo_tomylist(mid,smids):
    _l_(550584)

    for smid in _n_(550548, "smids", lambda: smids):
        _l_(550583)

        cmdurl = "http://www.nicovideo.jp/api/mylist/add"
        _l_(550549)
        q = {}
        _l_(550550)
        _n_(550551, "q", lambda: q)['group_id'] = _n_(550552, "mid", lambda: mid)
        _l_(550553)
        _n_(550554, "q", lambda: q)['item_type'] = 0
        _l_(550555)
        _n_(550556, "q", lambda: q)['item_id'] = _n_(550557, "smid", lambda: smid)
        _l_(550558)
        _n_(550559, "q", lambda: q)['description'] = u""
        _l_(550560)
        _n_(550561, "q", lambda: q)['token'] = _n_(550562, "token", lambda: token)
        _l_(550563)
        cmdurl += "?" + _c_(550569, _a_(550568, _c_(550567, _a_(550565, _a_(550564, urllib, "parse"), "urlencode"), _n_(550566, "q", lambda: q)), "encode"), "utf-8")
        _l_(550570)
        j = _c_(550577, _a_(550572, _n_(550571, "json", lambda: json), "load"), _c_(550576, _a_(550574, _a_(550573, urllib, "request"), "urlopen"), _n_(550575, "cmdurl", lambda: cmdurl)), encoding='utf-8')
        _l_(550578)
        _c_(550581, _a_(550580, _n_(550579, "time", lambda: time), "sleep"), 0.5)
        _l_(550582)

#Login
opener = _c_(550593, _a_(550586, _a_(550585, urllib, "request"), "build_opener"), _c_(550592, _a_(550588, _a_(550587, urllib, "request"), "HTTPCookieProcessor"), _c_(550591, _a_(550590, _a_(550589, http, "cookiejar"), "CookieJar"))))
_l_(550594)
_c_(550598, _a_(550596, _a_(550595, urllib, "request"), "install_opener"), _n_(550597, "opener", lambda: opener))
_l_(550599)
_c_(550609, _a_(550608, _c_(550607, _a_(550601, _a_(550600, urllib, "request"), "urlopen"), "https://secure.nicovideo.jp/secure/login",
                _c_(550606, _a_(550603, _a_(550602, urllib, "parse"), "urlencode"), {"mail":_n_(550604, "userid", lambda: userid), "password":_n_(550605, "passwd", lambda: passwd)}) ), "encode"), "utf-8")
_l_(550610)
#GetToken
token = _c_(550612, _n_(550611, "getToken", lambda: getToken))
_l_(550613)
#MakeMylist&AddMylist
mid = _c_(550615, _n_(550614, "mylist_create", lambda: mylist_create), u"Testlist")
_l_(550616)
_c_(550619, _n_(550617, "addvideo_tomylist", lambda: addvideo_tomylist), _n_(550618, "mid", lambda: mid), ["sm9","sm1097445", "sm1715919"  ] )
_l_(550620)