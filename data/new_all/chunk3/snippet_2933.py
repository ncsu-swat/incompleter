# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57953013/typeerror-unorderable-types-int-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
json_file = _c_(544279, _n_(544278, "open", lambda: open), "./Labeled.json","r",encoding="utf-8")
_l_(544280)
data = _c_(544284, _a_(544282, _n_(544281, "json", lambda: json), "load"), _n_(544283, "json_file", lambda: json_file))
_l_(544285)

if _n_(544286, "__name__", lambda: __name__) == '__main__':
    _l_(544318)

    # logger setup
    log = _c_(544289, _a_(544288, _n_(544287, "logging", lambda: logging), "getLogger"), 'GiveMe5W')
    _l_(544290)
    _c_(544295, _a_(544292, _n_(544291, "log", lambda: log), "setLevel"), _a_(544294, _n_(544293, "logging", lambda: logging), "DEBUG"))
    _l_(544296)
    sh = _c_(544299, _a_(544298, _n_(544297, "logging", lambda: logging), "StreamHandler"))
    _l_(544300)
    _c_(544305, _a_(544302, _n_(544301, "sh", lambda: sh), "setLevel"), _a_(544304, _n_(544303, "logging", lambda: logging), "DEBUG"))
    _l_(544306)
    _c_(544310, _a_(544308, _n_(544307, "log", lambda: log), "addHandler"), _n_(544309, "sh", lambda: sh))
    _l_(544311)

    # giveme5w setup - with defaults
    extractor = _c_(544313, _n_(544312, "MasterExtractor", lambda: MasterExtractor))
    _l_(544314)
    _c_(544316, _n_(544315, "Document", lambda: Document)) 
    _l_(544317) 

for i in _c_(544320, _n_(544319, "range", lambda: range), 0,1000):
    _l_(544368)

    body = _n_(544321, "data", lambda: data)[_n_(544322, "i", lambda: i)]["body"]
    _l_(544323)
    #print(body)
    #for line in body:
    #print(line[0:line.find('\n')])
    #head = re.sub("[^A-Z\d]", "", "")
    head = _c_(544329, _a_(544328, _c_(544327, _a_(544325, _n_(544324, "re", lambda: re), "search"), "^[^\n]*", _n_(544326, "body", lambda: body)), "group"), 0)
    _l_(544330)
    head = _c_(544333, _n_(544331, "str", lambda: str), _n_(544332, "head", lambda: head))
    _l_(544334)

    title = _n_(544335, "data", lambda: data)[_n_(544336, "i", lambda: i)]["title"]
    _l_(544337)
    title = _c_(544340, _n_(544338, "str", lambda: str), _n_(544339, "title", lambda: title))
    _l_(544341)

    body = _n_(544342, "data", lambda: data)[_n_(544343, "i", lambda: i)]["body"]
    _l_(544344)
    body = _c_(544347, _n_(544345, "str", lambda: str), _n_(544346, "body", lambda: body))
    _l_(544348)

    published_at = _n_(544349, "data", lambda: data)[_n_(544350, "i", lambda: i)]["published_at"]
    _l_(544351)
    published_at = _c_(544354, _n_(544352, "str", lambda: str), _n_(544353, "published_at", lambda: published_at))
    _l_(544355)

    doc1 = _c_(544361, _n_(544356, "Document", lambda: Document), _n_(544357, "title", lambda: title),_n_(544358, "head", lambda: head),_n_(544359, "body", lambda: body),_n_(544360, "published_at", lambda: published_at))
    _l_(544362)


    doc = _c_(544366, _a_(544364, _n_(544363, "extractor", lambda: extractor), "parse"), _n_(544365, "doc1", lambda: doc1))
    _l_(544367)