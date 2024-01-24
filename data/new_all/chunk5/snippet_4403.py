# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58334923/why-python-gives-typeerror-when-trying-to-call-a-function-that-read-text
#open the file and read it as a list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
textlist = _c_(676981, _a_(676980, _c_(676979, _n_(676978, "open", lambda: open), 'testfile.text', 'r'), "readlines"))
_l_(676982)
#textlist = ['Build a machine\n', 'For the next generation']

#print the return_position as a lines
_c_(676989, _n_(676983, "print", lambda: print), _c_(676988, _a_(676984, '', "join"), _c_(676987, _n_(676985, "return_position", lambda: return_position), _n_(676986, "textlist", lambda: textlist), search_for=['a', 'b'])))
_l_(676990)