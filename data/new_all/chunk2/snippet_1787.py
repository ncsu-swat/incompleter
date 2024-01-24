# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55964272/nameerror-name-url-data-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from html.parser import HTMLParser
    _l_(436454)

except ImportError:
    pass
try:
    import urllib.request
    _l_(436456)

except ImportError:
    pass

class CustomHTMLParser(_n_(436457, "HTMLParser", lambda: HTMLParser)):
    _l_(436486)

    def __init__(self):
        _l_(436469)

        _c_(436461, _a_(436459, _n_(436458, "HTMLParser", lambda: HTMLParser), "__init__"), _n_(436460, "self", lambda: self))
        _l_(436462)
        _n_(436463, "self", lambda: self).tag_flag = False
        _l_(436464)
        _n_(436465, "self", lambda: self).tag_line_num = 0
        _l_(436466)
        _n_(436467, "self", lambda: self).tag_string = 'temporary_tag'
        _l_(436468)

    def initiate_vars(self, tag_string):
        _l_(436473)

        _n_(436470, "self", lambda: self).tag_string = _n_(436471, "tag_string", lambda: tag_string)
        _l_(436472)

    def handle_starttag(self, tag, attrs):
        _l_(436485)

        #if tag == 'tag_to_search_for':
        if _n_(436474, "tag", lambda: tag) == _a_(436476, _n_(436475, "self", lambda: self), "tag_string"):
            _l_(436484)

            _n_(436477, "self", lambda: self).tag_flag = True
            _l_(436478)
            _n_(436479, "self", lambda: self).tag_line_num = _c_(436482, _a_(436481, _n_(436480, "self", lambda: self), "getpos"))
            _l_(436483)


if _n_(436487, "__name__", lambda: __name__)== '__main__':
    _l_(436565)

    #simple_str = 'string_to_search_for'
    simple_str = 'Host Status'
    _l_(436488)

    my_url = 'TEST_URL'
    _l_(436489)

    parser_obj = _c_(436491, _n_(436490, "CustomHTMLParser", lambda: CustomHTMLParser))
    _l_(436492)

    #parser_obj.initiate_vars('tag_to_search_for')
    _c_(436495, _a_(436494, _n_(436493, "parser_obj", lambda: parser_obj), "initiate_vars"), 'script')
    _l_(436496)

    #html_file = open('location_of_html_file//file.html')
    my_request = _c_(436500, _a_(436498, _a_(436497, urllib, "request"), "Request"), _n_(436499, "my_url", lambda: my_url))
    _l_(436501)

    try:
        _l_(436511)

        url_data = _c_(436505, _a_(436503, _a_(436502, urllib, "request"), "urlopen"), _n_(436504, "my_request", lambda: my_request))
        _l_(436506)
    except:
        _l_(436510)

        _c_(436508, _n_(436507, "print", lambda: print), "There was some error opening the URL")
        _l_(436509)

    html_str = _c_(436516, _a_(436515, _c_(436514, _a_(436513, _n_(436512, "url_data", lambda: url_data), "read")), "decode"), 'utf8')
    _l_(436517)
    #html_str = html_file.read()

    #print (html_str)

    html_search_result = _c_(436525, _a_(436521, _c_(436520, _a_(436519, _n_(436518, "html_str", lambda: html_str), "lower")), "find"), _c_(436524, _a_(436523, _n_(436522, "simple_str", lambda: simple_str), "lower")))
    _l_(436526)
    if _n_(436527, "html_search_result", lambda: html_search_result) != -1:
        _l_(436540)

        _c_(436532, _n_(436528, "print", lambda: print), _c_(436531, _a_(436529, 'The word {} was found', "format"), _n_(436530, "simple_str", lambda: simple_str)))
        _l_(436533)
    else:
        _c_(436538, _n_(436534, "print", lambda: print), _c_(436537, _a_(436535, 'The word {} was not found', "format"), _n_(436536, "simple_str", lambda: simple_str)))
        _l_(436539)

    _c_(436544, _a_(436542, _n_(436541, "parser_obj", lambda: parser_obj), "feed"), _n_(436543, "html_str", lambda: html_str))
    _l_(436545)

    if _a_(436547, _n_(436546, "parser_obj", lambda: parser_obj), "tag_flag"):
        _l_(436564)

        _c_(436555, _n_(436548, "print", lambda: print), _c_(436554, _a_(436549, 'Tag {0} was found at position {1}', "format"), _a_(436551, _n_(436550, "parser_obj", lambda: parser_obj), "tag_string"), _a_(436553, _n_(436552, "parser_obj", lambda: parser_obj), "tag_line_num")))
        _l_(436556)
    else:
        _c_(436562, _n_(436557, "print", lambda: print), _c_(436561, _a_(436558, 'Tag {} was not found', "format"), _a_(436560, _n_(436559, "parser_obj", lambda: parser_obj), "tag_string")))
        _l_(436563)