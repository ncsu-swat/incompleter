# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68188949/how-to-resolve-attributeerror-nonetype-object-has-no-attribute-find
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(620357)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(620359)

except ImportError:
    pass
try:
    import requests
    _l_(620361)

except ImportError:
    pass
try:
    from time import sleep
    _l_(620363)

except ImportError:
    pass
try:
    from datetime import date, timedelta
    _l_(620365)

except ImportError:
    pass

#create empty arrays for data we're collecting
dates=[]
_l_(620366)
url_list=[]
_l_(620367)
final = []
_l_(620368)

#map site

url = "https://spotifycharts.com/regional/au/weekly"
_l_(620369)
start_date= _c_(620371, _n_(620370, "date", lambda: date), 2016, 12, 29)
_l_(620372)
end_date= _c_(620374, _n_(620373, "date", lambda: date), 2020, 12, 24)
_l_(620375)

delta= _n_(620376, "end_date", lambda: end_date)-_n_(620377, "start_date", lambda: start_date)
_l_(620378)

for i in _c_(620382, _n_(620379, "range", lambda: range), _a_(620381, _n_(620380, "delta", lambda: delta), "days")+1):
    _l_(620397)

    day = _n_(620383, "start_date", lambda: start_date)+_c_(620386, _n_(620384, "timedelta", lambda: timedelta), days=_n_(620385, "i", lambda: i))
    _l_(620387)
    day_string= _c_(620390, _a_(620389, _n_(620388, "day", lambda: day), "strftime"), "%Y-%m-%d")
    _l_(620391)
    _c_(620395, _a_(620393, _n_(620392, "dates", lambda: dates), "append"), _n_(620394, "day_string", lambda: day_string))
    _l_(620396)

def add_url():
    _l_(620408)

    for date in _n_(620398, "dates", lambda: dates):
        _l_(620407)

        c_string = _n_(620399, "url", lambda: url)+_n_(620400, "date", lambda: date)
        _l_(620401)
        _c_(620405, _a_(620403, _n_(620402, "url_list", lambda: url_list), "append"), _n_(620404, "c_string", lambda: c_string))
        _l_(620406)

_c_(620410, _n_(620409, "add_url", lambda: add_url))
_l_(620411)

#function for going through each row in each url and finding relevant song info

def song_scrape(x):
    _l_(620464)

    pg = _n_(620412, "x", lambda: x)
    _l_(620413)
    for tr in _c_(620418, _a_(620417, _c_(620416, _a_(620415, _n_(620414, "songs", lambda: songs), "find"), "tbody"), "findAll"), "tr"):
        _l_(620463)

        artist= _a_(620424, _c_(620423, _a_(620422, _c_(620421, _a_(620420, _n_(620419, "tr", lambda: tr), "find"), "td", {"class": "chart-table-track"}), "find"), "span"), "text")
        _l_(620425)
        artist= _c_(620430, _a_(620429, _c_(620428, _a_(620427, _n_(620426, "artist", lambda: artist), "replace"), "by ",""), "strip"))
        _l_(620431)
  
        title= _a_(620437, _c_(620436, _a_(620435, _c_(620434, _a_(620433, _n_(620432, "tr", lambda: tr), "find"), "td", {"class": "chart-table-track"}), "find"), "strong"), "text")
        _l_(620438)
 
        songid= _c_(620445, _a_(620444, _c_(620443, _a_(620442, _c_(620441, _a_(620440, _n_(620439, "tr", lambda: tr), "find"), "td", {"class": "chart-table-image"}), "find"), "a"), "get"), "href")
        _l_(620446)
        songid= _c_(620449, _a_(620448, _n_(620447, "songid", lambda: songid), "split"), "track/")[1]
        _l_(620450)
    
        url_date= _c_(620453, _a_(620452, _n_(620451, "x", lambda: x), "split"), "daily/")[1]
        _l_(620454)
        
        _c_(620461, _a_(620456, _n_(620455, "final", lambda: final), "append"), [_n_(620457, "title", lambda: title), _n_(620458, "artist", lambda: artist), _n_(620459, "songid", lambda: songid), _n_(620460, "url_date", lambda: url_date)])
        _l_(620462)
#loop through urls to create array of all of our song info

for u in _n_(620465, "url_list", lambda: url_list):
    _l_(620487)

    read_pg= _c_(620469, _a_(620467, _n_(620466, "requests", lambda: requests), "get"), _n_(620468, "u", lambda: u))
    _l_(620470)
    _c_(620472, _n_(620471, "sleep", lambda: sleep), 2)
    _l_(620473)
    soup= _c_(620477, _n_(620474, "BeautifulSoup", lambda: BeautifulSoup), _a_(620476, _n_(620475, "read_pg", lambda: read_pg), "text"), "html.parser")
    _l_(620478)
    songs= _c_(620481, _a_(620480, _n_(620479, "soup", lambda: soup), "find"), "table", {"class":"chart-table"})
    _l_(620482)
    _c_(620485, _n_(620483, "song_scrape", lambda: song_scrape), _n_(620484, "u", lambda: u))
    _l_(620486)
 
#convert to data frame with pandas for easier data manipulation

final_df = _c_(620491, _a_(620489, _n_(620488, "pd", lambda: pd), "DataFrame"), _n_(620490, "final", lambda: final), columns= ["Title", "Artist", "Song ID", "Chart Date"])
_l_(620492)

#write to csv

with _c_(620494, _n_(620493, "open", lambda: open), 'spmooddata.csv', 'w') as f:
    _l_(620500)

    _c_(620498, _a_(620496, _n_(620495, "final_df", lambda: final_df), "to_csv"), _n_(620497, "f", lambda: f), header= True, index=False)
    _l_(620499)