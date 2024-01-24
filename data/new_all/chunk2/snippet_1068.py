# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47124194/filenotfounderror-while-scraping-images
# A script to download pictures from reddit.com/r/HistoryPorn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(467407)

except ImportError:
    pass
try:
    from urllib.request import urlretrieve
    _l_(467409)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(467411)

except ImportError:
    pass
try:
    import re
    _l_(467413)

except ImportError:
    pass
try:
    import os
    _l_(467415)

except ImportError:
    pass
try:
    import sys
    _l_(467417)

except ImportError:
    pass

_c_(467419, _n_(467418, "print", lambda: print), 'Downloading images...')
_l_(467420)

# Create a directory for photographs
path_to_hist = '/home/tautvydas/Documents/histphoto'
_l_(467421)
_c_(467425, _a_(467423, _n_(467422, "os", lambda: os), "chdir"), _n_(467424, "path_to_hist", lambda: path_to_hist))
_l_(467426)
if not _c_(467430, _a_(467429, _a_(467428, _n_(467427, "os", lambda: os), "path"), "exists"), '/home/tautvydas/Documents/histphoto'):
    _l_(467436)

    _c_(467434, _a_(467432, _n_(467431, "os", lambda: os), "mkdir"), _n_(467433, "path_to_hist", lambda: path_to_hist))
    _l_(467435)

website = 'https://www.reddit.com/r/HistoryPorn'
_l_(467437)

# Go to the internet and connect to the subreddit, start a loop
for i in _c_(467439, _n_(467438, "range", lambda: range), 3):
    _l_(467507)

    subreddit = _c_(467442, _n_(467440, "urlopen", lambda: urlopen), _n_(467441, "website", lambda: website))
    _l_(467443)
    bs_subreddit = _c_(467446, _n_(467444, "BeautifulSoup", lambda: BeautifulSoup), _n_(467445, "subreddit", lambda: subreddit), 'lxml')
    _l_(467447)

    # Create a regex and find all the titles in the page
    remove_reddit_tag = _c_(467450, _a_(467449, _n_(467448, "re", lambda: re), "compile"), '(\s*\(i.redd.it\)(\s*))')
    _l_(467451)
    title_bs_subreddit = _c_(467454, _a_(467453, _n_(467452, "bs_subreddit", lambda: bs_subreddit), "findAll"), 'p', {'class': 'title'})
    _l_(467455)

    # Get text off the page
    pic_name = []
    _l_(467456)
    for item in _n_(467457, "title_bs_subreddit", lambda: title_bs_subreddit)[1:]:
        _l_(467472)

        item = _c_(467460, _a_(467459, _n_(467458, "item", lambda: item), "get_text"))
        _l_(467461)
        item = _c_(467465, _a_(467463, _n_(467462, "remove_reddit_tag", lambda: remove_reddit_tag), "sub"), '', _n_(467464, "item", lambda: item))
        _l_(467466)
        _c_(467470, _a_(467468, _n_(467467, "pic_name", lambda: pic_name), "append"), _n_(467469, "item", lambda: item))
        _l_(467471)

    # Get picture links
    pic_bs_subreddit = _c_(467478, _a_(467474, _n_(467473, "bs_subreddit", lambda: bs_subreddit), "findAll"), 'div', {'data-url' : _c_(467477, _a_(467476, _n_(467475, "re", lambda: re), "compile"), '.*')})
    _l_(467479)
    pic_img = []
    _l_(467480)
    for pic in _n_(467481, "pic_bs_subreddit", lambda: pic_bs_subreddit)[1:]:
        _l_(467487)

        _c_(467485, _a_(467483, _n_(467482, "pic_img", lambda: pic_img), "append"), _n_(467484, "pic", lambda: pic)['data-url'])
        _l_(467486)

    # Zip all info into one
    name_link = _c_(467491, _n_(467488, "zip", lambda: zip), _n_(467489, "pic_name", lambda: pic_name), _n_(467490, "pic_img", lambda: pic_img))
    _l_(467492)
    for i in _n_(467493, "name_link", lambda: name_link):
        _l_(467499)

        _c_(467497, _n_(467494, "urlretrieve", lambda: urlretrieve), _n_(467495, "i", lambda: i)[1],_n_(467496, "i", lambda: i)[0])
        _l_(467498)


    # Click next
    for link in _a_(467503, _c_(467502, _a_(467501, _n_(467500, "bs_subreddit", lambda: bs_subreddit), "find"), 'span', {'class' : 'next-button'}), "children"):
        _l_(467506)

        website = _n_(467504, "link", lambda: link)['href']
        _l_(467505)