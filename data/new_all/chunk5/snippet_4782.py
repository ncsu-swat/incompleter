# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74951298/typeerror-slice-indices-must-be-integers-or-none-or-have-an-index-method-er
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(673096)

except ImportError:
    pass
try:
    import requests
    _l_(673098)

except ImportError:
    pass
try:
    import bs4
    _l_(673100)

except ImportError:
    pass
try:
    from Essentials import Static
    _l_(673102)

except ImportError:
    pass


class CmsIDs:
    _l_(673251)

    def GetIDs():
        _l_(673196)

        # cont = requests.get(""https://www.facebook.com:443/help"", headers=Static.headers) # syntax error
        cont = _c_(673107, _a_(673104, _n_(673103, "requests", lambda: requests), "get"), "https://www.facebook.com:443/help", headers=_a_(673106, _n_(673105, "Static", lambda: Static), "headers"))
        _l_(673108)
        soup = _c_(673113, _a_(673110, _n_(673109, "bs4", lambda: bs4), "BeautifulSoup"), _a_(673112, _n_(673111, "cont", lambda: cont), "content"), "html5lib")
        _l_(673114)

        text = _c_(673117, _a_(673116, _n_(673115, "soup", lambda: soup), "find_all"), "script")
        _l_(673118)

        start = ""
        _l_(673119)
        txtstr = ""
        _l_(673120)

  

        for i in _c_(673125, _n_(673121, "range", lambda: range), _c_(673124, _n_(673122, "len", lambda: len), _n_(673123, "text", lambda: text))):
            _l_(673156)

    
            mystr = _n_(673126, "text", lambda: text)[_n_(673127, "i", lambda: i)]
            _l_(673128)

            # mystr = text[i]
            _c_(673133, _n_(673129, "print", lambda: print), "this is: ", _c_(673132, _a_(673131, _n_(673130, "mystr", lambda: mystr), "find"), '__bbox":'))
            _l_(673134)
            if _c_(673140, _a_(673139, _c_(673138, _a_(673137, _n_(673135, "text", lambda: text)[_n_(673136, "i", lambda: i)], "get_text")), "find"), '__bbox":') != -1:
                _l_(673155)

                # print(i, text[i].get_text())
                txtstr += _c_(673144, _a_(673143, _n_(673141, "text", lambda: text)[_n_(673142, "i", lambda: i)], "get_text"))
                _l_(673145)
                start = _c_(673151, _a_(673150, _c_(673149, _a_(673148, _n_(673146, "text", lambda: text)[_n_(673147, "i", lambda: i)], "get_text")), "find"), '__bbox":') + _c_(673153, _n_(673152, "len", lambda: len), '__bbox":')
                _l_(673154)

        _c_(673159, _n_(673157, "print", lambda: print), 'start:', _n_(673158, "start", lambda: start))
        _l_(673160)

        count = 0
        _l_(673161)
        for end, char in _c_(673166, _n_(673162, "enumerate", lambda: enumerate), _n_(673163, "txtstr", lambda: txtstr)[_n_(673164, "start", lambda: start):], _n_(673165, "start", lambda: start)):
            _l_(673176)

            if _n_(673167, "char", lambda: char) == '{':
                _l_(673169)

                count += 1
                _l_(673168)
            if _n_(673170, "char", lambda: char) == '}':
                _l_(673172)

                count -= 1
                _l_(673171)
            if _n_(673173, "count", lambda: count) == 0:
                _l_(673175)

                break
                _l_(673174)
        _c_(673179, _n_(673177, "print", lambda: print), 'end:', _n_(673178, "end", lambda: end))
        _l_(673180)

        # --- convert JSON string to Python structure (dict/list) ---

        data = _c_(673186, _a_(673182, _n_(673181, "json", lambda: json), "loads"), _n_(673183, "txtstr", lambda: txtstr)[_n_(673184, "start", lambda: start):_n_(673185, "end", lambda: end)+1])
        _l_(673187)
        # pp.pprint(data)
        _c_(673189, _n_(673188, "print", lambda: print), '--- search ---')
        _l_(673190)
        _c_(673194, _a_(673192, _n_(673191, "CmsIDs", lambda: CmsIDs), "search"), _n_(673193, "data", lambda: data))
        _l_(673195)

    def search(data):
        _l_(673250)

        if _c_(673200, _n_(673197, "isinstance", lambda: isinstance), _n_(673198, "data", lambda: data), _n_(673199, "dict", lambda: dict)):
            _l_(673237)

            found = False
            _l_(673201)
            if 'cms_object_id' in _n_(673202, "data", lambda: data):
                _l_(673208)

                _c_(673205, _n_(673203, "print", lambda: print), 'cms_object_id', _n_(673204, "data", lambda: data)['cms_object_id'])
                _l_(673206)
                found = True
                _l_(673207)
            if 'cmsID' in _n_(673209, "data", lambda: data):
                _l_(673215)

                _c_(673212, _n_(673210, "print", lambda: print), 'cmsID', _n_(673211, "data", lambda: data)['cmsID'])
                _l_(673213)
                found = True
                _l_(673214)
            if 'name' in _n_(673216, "data", lambda: data):
                _l_(673222)

                _c_(673219, _n_(673217, "print", lambda: print), 'name', _n_(673218, "data", lambda: data)['name'])
                _l_(673220)
                found = True
                _l_(673221)
            if _n_(673223, "found", lambda: found):
                _l_(673227)

                _c_(673225, _n_(673224, "print", lambda: print), '---')
                _l_(673226)
            for val in _c_(673230, _a_(673229, _n_(673228, "data", lambda: data), "values")):
                _l_(673236)

                _c_(673234, _a_(673232, _n_(673231, "CmsIDs", lambda: CmsIDs), "search"), _n_(673233, "val", lambda: val))
                _l_(673235)
        if _c_(673241, _n_(673238, "isinstance", lambda: isinstance), _n_(673239, "data", lambda: data), _n_(673240, "list", lambda: list)):
            _l_(673249)

            for val in _n_(673242, "data", lambda: data):
                _l_(673248)

                _c_(673246, _a_(673244, _n_(673243, "CmsIDs", lambda: CmsIDs), "search"), _n_(673245, "val", lambda: val))
                _l_(673247)


if _n_(673252, "__name__", lambda: __name__) == '__main__':
    _l_(673257)

    _c_(673255, _a_(673254, _n_(673253, "CmsIDs", lambda: CmsIDs), "GetIDs"))
    _l_(673256)