# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71562113/filenotfounderror-errno-2-no-such-file-or-directory-9788427133310-urls-csv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fileName= _c_(612012, _n_(612011, "input", lambda: input), "Please enter the name of the file you'd like to use.")
_l_(612013)
fileScan= _c_(612016, _n_(612014, "open", lambda: open), _n_(612015, "fileName", lambda: fileName), 'r')  #Opens file
_l_(612017)  #Opens file