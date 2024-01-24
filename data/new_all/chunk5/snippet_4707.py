# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51819971/tkinter-attributeerror-nonetype-object-has-no-attribute-insert
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(686233)

except ImportError:
    pass
try:
    import json
    _l_(686235)

except ImportError:
    pass
try:
    import requests
    _l_(686237)

except ImportError:
    pass


accessToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
_l_(686238)
query = r'xxxxxxx/?fields=posts.limit(20)'
_l_(686239)

window = _c_(686241, _n_(686240, "Tk", lambda: Tk))
_l_(686242)
_c_(686245, _a_(686244, _n_(686243, "window", lambda: window), "title"), 'The Sakht Launday')
_l_(686246)
pagePicture = _c_(686248, _n_(686247, "PhotoImage", lambda: PhotoImage), file= 'pagePicture.GIF')
_l_(686249)
_c_(686255, _a_(686254, _c_(686253, _n_(686250, "Label", lambda: Label), _n_(686251, "window", lambda: window), image = _n_(686252, "pagePicture", lambda: pagePicture)), "grid"), row = 0, column = 0, sticky = 'E')
_l_(686256)

#Text To Display Inside
listbox = _c_(686262, _a_(686261, _c_(686260, _n_(686257, "Text", lambda: Text), _n_(686258, "window", lambda: window), width = 50, height = 25, wrap = _n_(686259, "WORD", lambda: WORD), background ='White'), "grid"), row = 0, column = 1)
_l_(686263)

reQ = _c_(686268, _a_(686265, _n_(686264, "requests", lambda: requests), "get"), 'https://graph.facebook.com/v3.1/' + _n_(686266, "query", lambda: query), {'access_token': _n_(686267, "accessToken", lambda: accessToken)})
_l_(686269)
tempData = _c_(686272, _a_(686271, _n_(686270, "reQ", lambda: reQ), "json"))
_l_(686273)
_c_(686277, _a_(686275, _n_(686274, "json", lambda: json), "dumps"), _n_(686276, "tempData", lambda: tempData))
_l_(686278)
data = _n_(686279, "tempData", lambda: tempData)['posts']['data']
_l_(686280)
for results in _n_(686281, "data", lambda: data):
    _l_(686299)

    caption = _n_(686282, "results", lambda: results)['message']
    _l_(686283)
    timeUploaded = _n_(686284, "results", lambda: results)['created_time']
    _l_(686285)
    urlID = _n_(686286, "results", lambda: results)['id']
    _l_(686287)
    finalPost = _c_(686292, _a_(686288, 'Caption: {0}\nTime Uploaded: {1}\nURL: {2}\n\n', "format"), _n_(686289, "caption", lambda: caption), _n_(686290, "timeUploaded", lambda: timeUploaded), _n_(686291, "urlID", lambda: urlID))
    _l_(686293)
    _c_(686297, _a_(686295, _n_(686294, "listbox", lambda: listbox), "insert"), 0, _n_(686296, "finalPost", lambda: finalPost))
    _l_(686298)