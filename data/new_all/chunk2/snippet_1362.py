# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70308925/getting-error-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
urls = [] 
_l_(445240) 
uni_names = [] 
_l_(445241) 
page_urls_new = [] 
_l_(445242) 
university_details = ["Name","Link","Location","Rank"]
_l_(445243)

#Determine 
#Colleges 

start_time = _c_(445250, _n_(445244, "int", lambda: int), _c_(445249, _n_(445245, "round", lambda: round), _c_(445248, _a_(445247, _n_(445246, "time", lambda: time), "time")))) 
_l_(445251) 

for i in _c_(445256, _n_(445252, "range", lambda: range), 0, _c_(445255, _n_(445253, "len", lambda: len), _n_(445254, "page_urls", lambda: page_urls))):
    _l_(445278)

    page_url = _n_(445257, "page_urls", lambda: page_urls)[_n_(445258, "i", lambda: i)] 
    _l_(445259) 
    page_text_soup = _c_(445264, _n_(445260, "BeautifulSoup", lambda: BeautifulSoup), _c_(445263, _n_(445261, "extract_source", lambda: extract_source), _n_(445262, "page_url", lambda: page_url)), "lxml") 
    _l_(445265) 
    entries = _c_(445271, _n_(445266, "int", lambda: int), _a_(445270, _c_(445269, _a_(445268, _n_(445267, "page_text_soup", lambda: page_text_soup), "find"), 'strong', attrs={'data-test-id': 'total-items'}), "text")) 
    _l_(445272) 
    entries = _c_(445276, _n_(445273, "int", lambda: int), (_n_(445274, "entries", lambda: entries) / 20) + (0 if 0 == _n_(445275, "entries", lambda: entries) % 20 else 1))
    _l_(445277)