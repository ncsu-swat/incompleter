# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47234130/typeerror-list-indices-must-be-integers-or-slices-not-str-when-using-nested-di
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import textract, math, os
    _l_(570242)

except ImportError:
    pass
docs=[]
_l_(570243)
#Read the files and store them in docs
folder = _c_(570246, _a_(570245, _n_(570244, "os", lambda: os), "listdir"), "./input/")
_l_(570247)
for file in _n_(570248, "folder", lambda: folder):
    _l_(570262)

    if _c_(570251, _a_(570250, _n_(570249, "file", lambda: file), "endswith"), "txt"):
        _l_(570261)

        _c_(570259, _a_(570253, _n_(570252, "docs", lambda: docs), "append"), [_n_(570254, "file", lambda: file),_c_(570258, _a_(570256, _n_(570255, "textract", lambda: textract), "process"), "./input/"+_n_(570257, "file", lambda: file))])
        _l_(570260)

inverted_index={}
_l_(570263)
for doc in _n_(570264, "docs", lambda: docs):
    _l_(570316)

    words=_c_(570267, _a_(570266, _n_(570265, "doc", lambda: doc)[1], "decode"))
    _l_(570268)
    words=_c_(570271, _a_(570270, _n_(570269, "words", lambda: words), "split"), " ")
    _l_(570272)

    #loop through and build the inverted index
    for word in _n_(570273, "words", lambda: words):
        _l_(570315)

        temp={}
        _l_(570274)
        #to remove initial white space
        if (_n_(570275, "word", lambda: word) == " ") or (_n_(570276, "word", lambda: word)==""):
            _l_(570278)

            continue
            _l_(570277)
        if _n_(570279, "word", lambda: word) not in _n_(570280, "inverted_index", lambda: inverted_index):
            _l_(570314)

            _n_(570281, "temp", lambda: temp)[_n_(570282, "doc", lambda: doc)[0]]=1
            _l_(570283)
            _n_(570284, "temp", lambda: temp)['0']=0 #idf
            _l_(570285) #idf
            _n_(570286, "temp", lambda: temp)['1']=1 #tf
            _l_(570287) #tf
            _n_(570288, "inverted_index", lambda: inverted_index)[_n_(570289, "word", lambda: word)]=_n_(570290, "temp", lambda: temp)
            _l_(570291)
        else:
            if _n_(570292, "doc", lambda: doc)[0] not in _c_(570296, _a_(570295, _n_(570293, "inverted_index", lambda: inverted_index)[_n_(570294, "word", lambda: word)], "keys")):
                _l_(570313)

                _n_(570297, "inverted_index", lambda: inverted_index)[_n_(570298, "word", lambda: word)][_n_(570299, "doc", lambda: doc)[0]]=1
                _l_(570300)
                _n_(570301, "inverted_index", lambda: inverted_index)[_n_(570302, "word", lambda: word)]['1']=_n_(570303, "inverted_index", lambda: inverted_index)[_n_(570304, "word", lambda: word)]['1']+1
                _l_(570305)
            else:
                _n_(570306, "inverted_index", lambda: inverted_index)[_n_(570307, "word", lambda: word)][_n_(570308, "doc", lambda: doc)[0]]=_n_(570309, "inverted_index", lambda: inverted_index)[_n_(570310, "word", lambda: word)][_n_(570311, "doc", lambda: doc)[0]]+1
                _l_(570312)

# to sort and print values with calculating the the tf and idf on the fly
for key, value in _c_(570321, _n_(570317, "sorted", lambda: sorted), _c_(570320, _a_(570319, _n_(570318, "inverted_index", lambda: inverted_index), "items"))):
    _l_(570344)

    _n_(570322, "inverted_index", lambda: inverted_index)[_n_(570323, "key", lambda: key)]=_c_(570327, _n_(570324, "sorted", lambda: sorted), _n_(570325, "inverted_index", lambda: inverted_index)[_n_(570326, "key", lambda: key)]) # to sort the filenames where the word occured.
    _l_(570328) # to sort the filenames where the word occured.
    _n_(570329, "inverted_index", lambda: inverted_index)[_n_(570330, "key", lambda: key)]['0']=_c_(570337, _a_(570332, _n_(570331, "math", lambda: math), "log2"), _c_(570335, _n_(570333, "len", lambda: len), _n_(570334, "docs", lambda: docs))/_n_(570336, "value", lambda: value)['1']) # the error in this line
    _l_(570338) # the error in this line
    _c_(570342, _n_(570339, "print", lambda: print), _n_(570340, "key", lambda: key), _n_(570341, "value", lambda: value))
    _l_(570343)