# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57750999/want-to-get-text-from-a-div-but-getting-typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
bs = _c_(460845, _n_(460843, "BeautifulSoup", lambda: BeautifulSoup), _n_(460844, "html", lambda: html), features="lxml")
_l_(460846)
reg = _c_(460849, _a_(460848, _n_(460847, "re", lambda: re), "compile"), r'u\/\[deleted\]')
_l_(460850)
main_elt = _c_(460853, _a_(460852, _n_(460851, "bs", lambda: bs), "find"), "button", {"data-main-id": "vote"})
_l_(460854)
_c_(460860, _n_(460855, "print", lambda: print), _c_(460859, _n_(460856, "str", lambda: str), _a_(460858, _n_(460857, "main_elt", lambda: main_elt), "parent")))
_l_(460861)
vote_div = _c_(460865, _a_(460864, _a_(460863, _n_(460862, "main_elt", lambda: main_elt), "parent"), "find"), 'div')
_l_(460866)
_c_(460871, _n_(460867, "print", lambda: print), _c_(460870, _n_(460868, "str", lambda: str), _n_(460869, "vote_div", lambda: vote_div)))
_l_(460872)
_c_(460877, _n_(460873, "print", lambda: print), "vote text:" + _c_(460876, _a_(460875, _n_(460874, "vote_div", lambda: vote_div), "text")))
_l_(460878)